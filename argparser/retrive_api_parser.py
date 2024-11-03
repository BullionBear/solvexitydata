import argparse
from helper.cipher import get_api_key

def get_api_key_parser():
    parser = argparse.ArgumentParser(description="Get an API key")
    parser.add_argument("--name", required=True, help="API name")
    parser.add_argument("--exchange", required=True, help="Exchange name")
    return parser


if __name__ == "__main__":
    parser = get_api_key_parser()
    args = parser.parse_args()
    
    get_api_key(args.name, args.exchange)