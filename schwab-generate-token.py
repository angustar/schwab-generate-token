import argparse
import sys
import schwab

def get_user_input(prompt, default=None):
    if default:
        return input(f"{prompt} (default: {default}): ") or default
    else:
        return input(f"{prompt}: ")

def main(api_key, app_secret, callback_url, token_path):
    try:
        schwab.auth.client_from_manual_flow(api_key, app_secret, callback_url, token_path)
        print("\nToken successfully generated and written to file!")
        return 0
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        return 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch a new token and write it to a file')

    required = parser.add_argument_group('required arguments')
    required.add_argument('--api_key', required=False)
    required.add_argument('--app_secret', required=False)
    required.add_argument('--callback_url', required=False,
                          type=str, help='Callback URL (suggestion: https://127.0.0.1:8182)')
    required.add_argument('--token_file', required=False,
                          help='Path to token file. Any existing file will be overwritten (suggestion: _schwab_token.json)')

    args = parser.parse_args()

    # Check if the required arguments are provided, if not, prompt the user
    if not args.api_key:
        args.api_key = input(f"Enter the API Key: ")
    if not args.app_secret:
        args.app_secret = input(f"Enter the App Secret: ")
    if not args.callback_url:
        args.callback_url = input(f"Enter the Callback URL (suggestion: https://127.0.0.1:8182): ")
    if not args.token_file:
        args.token_file = input(f"Enter the Token file name (suggestion: _schwab_token.json): ")

    exit_code = main(args.api_key, args.app_secret, args.callback_url, args.token_file)

    # Pause the script to view error messages
    input("\nPress Enter to exit...")

    sys.exit(exit_code)