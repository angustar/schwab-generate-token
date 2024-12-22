# Schwab Token Generator

## Overview
`schwab-generate-token` is a tool to fetch a new token from the Schwab API and write it to a file. The tool can be run using command-line arguments or by prompting the user for input.

## Usage

You can run the script directly with the required arguments:
```bash
pip install -r requirements.txt
python schwab-generate-token.py --api_key YOUR_API_KEY --app_secret YOUR_APP_SECRET --callback_url CALLBACK_URL --token_file TOKEN_FILE_NAME
```

Alternatively, you can run the script using the `schwab-generate-token.exe` in Releases on Windows platform. This will open a command prompt window and prompt you for the required arguments. To compile this executable file, you can use PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile --clean --distpath=temp\dist --workpath=temp\build --console schwab-generate-token.py
```

## Arguments
- `--api_key`: The API Key for the Schwab API.
- `--app_secret`: The App Secret for the Schwab API.
- `--callback_url`: The callback URL, default is `https://127.0.0.1:8182`.
- `--token_file`: The path to the token file, default is `_schwab_token.json`.

## Example
Here is a complete example of how to run the script using command-line arguments:
```bash
python schwab-generate-token.py --api_key 123456789 --app_secret abcdefghijklmnopqrstuvwxyz --callback_url https://127.0.0.1:8182 --token_file _schwab_token.json
```

## Notes
- Ensure that the provided `API Key` and `App Secret` are valid.
- The `Callback URL` must match the callback URL configured in the Charles Schwab Developer Portal.
