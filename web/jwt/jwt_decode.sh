#!/usr/bin/env bash

# Function to pad base64URL encoded string to base64
pad_base64() {
    local input="$1"
    while [ $((${#input} % 4)) -ne 0 ]; do
        input+="="
    done
    echo "$input"
}

# Function to decode JWT
decode_jwt() {
    local jwt="$1"
    IFS='.' read -r header payload signature <<< "$jwt"

    header=$(pad_base64 "${header//-/+}")
    header=$(pad_base64 "${header//_/+}")

    payload=$(pad_base64 "${payload//-/+}")
    payload=$(pad_base64 "${payload//_/+}")

    echo "Header:"
    echo "$header" | base64 -d | jq '.' || echo "Error: Failed to parse header"

    echo -e "\nPayload:"
    echo "$payload" | base64 -d | jq '.' || echo "Error: Failed to parse payload"
}

# Function to print usage information
print_usage() {
    echo "Usage: $0 <JWT>"
    echo "  or pipe a JWT to stdin: echo <JWT> | $0"
    echo
    echo "This script decodes a JWT (JSON Web Token) and outputs the header and payload."
    echo "The JWT should be provided as a command-line argument or via stdin."
}

# Main script
if [ $# -eq 1 ]; then
    # Input from command line argument
    jwt="$1"
elif [ ! -t 0 ]; then
    # Input from stdin (pipe)
    jwt=$(cat)
else
    # No input provided, print usage and exit
    print_usage
    exit 1
fi

if [ -z "$jwt" ]; then
    echo "Error: No JWT provided"
    print_usage
    exit 1
fi

decode_jwt "$jwt"