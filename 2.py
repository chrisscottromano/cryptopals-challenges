def xor_hex_strings(hex_string1, hex_string2):
    """
    XOR two equal-length hex strings and return the result as a hex string.
    """
    # Convert the hex strings to bytes
    bytes1 = bytes.fromhex(hex_string1)
    bytes2 = bytes.fromhex(hex_string2)
    # print(bytes1)
    # print(bytes2)   
    # XOR the byte sequences
    result = bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])
    
    # Convert the result to a hex string
    hex_result = result.hex()
    
    return hex_result

hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"
result = xor_hex_strings(hex_string1, hex_string2)
print(result)
# Output: "216c766e6c7c626c6e2067797c696a62796d"
