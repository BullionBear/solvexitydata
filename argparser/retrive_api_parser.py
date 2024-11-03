import argparse
import json
from helper.cipher import get_api_key

def get_api_key_parser():
    parser = argparse.ArgumentParser(description="Get an API key")
    parser.add_argument("--name", required=True, help="API name")
    return parser


if __name__ == "__main__":
    parser = get_api_key_parser()
    args = parser.parse_args()
    
    api_detail = get_api_key(args.name)
    print(json.dumps(api_detail))