#!/usr/bin/python3
"""UTF-8 validation function"""

def validUTF8(data):
    """validate utf8"""
    def is_continuation(byte):
        """helper"""
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        leading_ones = 0
        while (data[i] >> (7 - leading_ones)) & 1:
            leading_ones += 1

        if leading_ones == 1 or leading_ones > 4:
            return False

        for j in range(1, leading_ones):
            if i + j >= len(data) or not is_continuation(data[i + j]):
                return False

        i += leading_ones

    return True
