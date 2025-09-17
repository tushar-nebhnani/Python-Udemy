"""
    Build a caesar cipher. Create a python script that helps you send secret messages to your friend using simple encryption.
"""

def encrypt(message, key):
    result = ""
    for char in message:
        base = ord('A') if char.isUpper() else ord('a')
        (ord(char) - base + key)