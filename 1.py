# Define a lookup table for converting bytes to base64 characters
BASE64_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Prompt the user for a hex string and read it from the terminal
hex_string = input("Enter a hex string: ")

# Convert the hex string to bytes
hex_bytes = bytes.fromhex(hex_string)

# print('bytes: ')
# print(hex_bytes)
# Initialize the base64-encoded string
base64_string = ""

# Loop through the input bytes in groups of three
for i in range(0, len(hex_bytes), 3):
    # Extract three bytes from the input
    chunk = hex_bytes[i:i+3]
    # Pad the chunk with null bytes if necessary
    if len(chunk) < 3:
        chunk += bytes([0] * (3 - len(chunk)))
    # Convert the three bytes to a single 24-bit number
    num = chunk[0] << 16 | chunk[1] << 8 | chunk[2]
    # Split the 24-bit number into four 6-bit numbers
    indices = [(num >> (18 - i * 6)) & 0x3f for i in range(4)]
    # Convert the 6-bit numbers to base64 characters
    chars = [BASE64_TABLE[index] for index in indices]
    # Add the base64 characters to the output string
    base64_string += "".join(chars)

# Add padding characters if necessary
if len(hex_bytes) % 3 == 1:
    base64_string += "=="
elif len(hex_bytes) % 3 == 2:
    base64_string += "="

# Print the base64-encoded string
print('Base64: ')
print(base64_string)
