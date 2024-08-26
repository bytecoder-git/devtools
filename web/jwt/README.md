# JWT Decoding Script

This Bash script provides a simple and efficient way to decode JSON Web Tokens (JWTs) directly from the command line.

## Features

- Decodes JWT header and payload
- Supports input via command-line argument or stdin (pipe)
- Handles JWTs of any practical length
- Provides clear usage instructions
- Formats output using `jq` for improved readability

## Requirements

- Bash
- `jq` (for JSON formatting)
- `base64` (usually pre-installed on most Unix-like systems)

## Installation

1. Clone this repository or download the `jwt_decode.sh` script.
2. Make the script executable:
   ```
   chmod +x jwt_decode.sh
   ```

## Usage

You can run the script directly as an executable:

```
./jwt_decode.sh <JWT>
```

Or you can pipe a JWT to the script:

```
echo <JWT> | ./jwt_decode.sh
```

### Arguments

- `<JWT>`: The JWT string to decode

### Examples

1. Decode a JWT provided as an argument:
   ```
   ./jwt_decode.sh eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
   ```

2. Decode a JWT provided via stdin:
   ```
   echo "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c" | ./jwt_decode.sh
   ```

## How It Works

1. The script accepts a JWT either as a command-line argument or via stdin.
2. It splits the JWT into its component parts (header, payload, and signature).
3. The script decodes the base64Url-encoded header and payload.
4. It uses `jq` to format the JSON output for improved readability.
5. The decoded header and payload are displayed in the console.

## Important Notes

- This script only decodes JWTs; it does not verify signatures or validate tokens.
- The script requires `jq` for JSON formatting. Ensure it's installed on your system.
- While the script can handle JWTs of any practical length, extremely long tokens may impact performance.
- The script does not process or display the signature part of the JWT.

## Contributing

Contributions to improve the script are welcome. Please submit a pull request or open an issue to discuss proposed changes.

## License

This script is released under the MIT License. See the LICENSE file for details.

Copyright 2024, Bill Heyman (bill@bytecoder.com)
