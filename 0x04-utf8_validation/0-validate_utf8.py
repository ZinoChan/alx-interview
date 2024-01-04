#!/usr/bin/python3
"""UTF-8 validation function"""


def transformToByte(num, num_bytes=2, byte_order='big'):
    return num.to_bytes(num_bytes, byteorder=byte_order)


def validUTF8(data):
    """Validate utf8"""
    for num in data:
        byte_repr = transformToByte(num)
        if byte_repr[0] == 0:
            pass
        else:
            return False

    return True
