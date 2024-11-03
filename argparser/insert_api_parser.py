import argparse
from helper.cipher import insert_api_key

def insert_api_key_parser():
    parser = argparse.ArgumentParser(description="Insert an API key")
    parser.add_argument("--name", required=True, help="API name")
    parser.add_argument("--exchange", required=True, help="Exchange name")
    parser.add_argument("--api_key", required=True, help="API key")
    parser.add_argument("--api_secret", required=True, help="API secret")
    parser.add_argument("--passphrase", help="API passphrase (optional)", default='')
    return parser

if __name__ == "__main__":
    parser = insert_api_key_parser()
    args = parser.parse_args()
    
    insert_api_key(args.name, args.exchange, args.api_key, args.api_secret, args.passphrase)
