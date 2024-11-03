import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import psycopg2
import argparse

# Load environment variables from .env file
load_dotenv()

# Get database URL and secret key from environment variables
DATABASE_URL = os.getenv("DB_URL")
SECRET_KEY = os.getenv("SECRET").encode()  # Encode the secret key for Fernet

cipher_suite = Fernet(SECRET_KEY)

def encrypt(text: str) -> str:
    return cipher_suite.encrypt(text.encode()).decode()

def decrypt(encrypted_text: str) -> str:
    return cipher_suite.decrypt(encrypted_text.encode()).decode()

def insert_api_key(name: str, exchange: str, api_key: str, api_secret: str, passphrase: str = ''):
    # Encrypt api_secret and passphrase if they exist
    encrypted_api_secret = encrypt(api_secret)
    encrypted_passphrase = encrypt(passphrase) if passphrase else None

    # Connect to PostgreSQL
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS read_api (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) UNIQUE NOT NULL,
            exchange VARCHAR(255) NOT NULL,
            api_key VARCHAR(255) NOT NULL,
            api_secret TEXT NOT NULL,
            passphrase TEXT
        )
    ''')

    # Insert the API key and secrets into the database
    cursor.execute('''
        INSERT INTO read_api (name, exchange, api_key, api_secret, passphrase)
        VALUES (%s, %s, %s, %s, %s)
    ''', (name, exchange, api_key, encrypted_api_secret, encrypted_passphrase))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"API key for {name} on {exchange} inserted successfully.")

def get_api_key(name: str, exchange: str):
    # Retrieve and decrypt api_secret and passphrase
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT api_key, api_secret, passphrase
        FROM read_api
        WHERE name = %s AND exchange = %s
    ''', (name, exchange))
    
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        api_key, encrypted_api_secret, encrypted_passphrase = result
        decrypted_api_secret = decrypt(encrypted_api_secret)
        decrypted_passphrase = decrypt(encrypted_passphrase) if encrypted_passphrase else None
        return {"api_key": api_key, "api_secret": decrypted_api_secret, "passphrase": decrypted_passphrase}
    else:
        print("API key not found.")
        return None