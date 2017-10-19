#!/usr/bin/env python3

u"""
Reference:
    http://download.nccst.nat.gov.tw/attachfilehandout/%E8%AD%B0%E9%A1%8C%E4%B8%80%EF%BC%9A%E8%B3%87%E8%A8%8A%E7%B3%BB%E7%B5%B1%E5%A7%94%E5%A4%96%E5%AE%89%E5%85%A8%E9%9C%80%E6%B1%82%E8%88%87%E9%A9%97%E8%AD%89%E5%AF%A6%E5%8B%99.pdf

    Page 29, 3. 規範密碼強度(2/2)
    要求列表:
        1.  至少一個小寫
        2.  至少一個大寫
        3.  至少一個數字
        4.  要求長度 12 字元以上
"""

import re
import string

PASSWORD_LENGTH = 12

# NCCST_PASSWORD_REGEX = "^(?=.*[A-Z])(?=.[a-z])(?=.*\d)[a-zA-Z\d]{12,}$"

# Some minor tweaks to make lookahead work: https://stackoverflow.com/a/28334645/761478
NCCST_PASSWORD_REGEX = "(?=.*?[A-Z])(?=.*?[a-z])(?=.*?\d)[a-zA-Z\d]{12,}$"


def check_nccst_password_strength(password):
    """ Return True if password strength match NCCST password requirement and False if not. """

    if len(password) < PASSWORD_LENGTH:
        print("password {} has insufficient password length".format(password))
        return False

    if all([state not in string.ascii_lowercase for state in password]):
        print("password {} has no lower case ascii code in password".format(password))
        return False

    if all([state not in string.ascii_uppercase for state in password]):
        print("password {} has no upper case ascii code in password".format(password))
        return False

    if all([state not in string.digits for state in password]):
        print("password {} has no digits in password".format(password))
        return False

    print("strength of password {} is sufficient for nccst.".format(password))
    return True


def validate_nccst_password_strength(password):
    """ Use NCCST suggested regex to validate if password is validated or not. """

    compiled_pattern = re.compile(NCCST_PASSWORD_REGEX)
    result = compiled_pattern.match(password)

    if result is None:
        print("invalid password: {}".format(password))
        return False

    print("password {} is valid".format(password))
    return True


def test_nccst_password_functions():
    """ Test function for NCCST password functions. """

    INVALID_PASSWORD_01 = "1234"
    INVALID_PASSWORD_02 = "AA1234567890"
    INVALID_PASSWORD_03 = "aa1234567890"
    INVALID_PASSWORD_04 = "aabbccAABBCC"
    VALID_PASSWORD_05 = "aA1234567890"  # Hope no one else use this as real password.
    VALID_PASSWORD_06 = "aA1234567890B"  # Hope no one else use this as real password.
    VALID_PASSWORD_07 = "aA12345678901"  # Hope no one else use this as real password.

    for password in (INVALID_PASSWORD_01, INVALID_PASSWORD_02, INVALID_PASSWORD_03,
            INVALID_PASSWORD_04, VALID_PASSWORD_05, VALID_PASSWORD_06, VALID_PASSWORD_07):

        check_nccst_password_strength(password)
        validate_nccst_password_strength(password)


if __name__ == "__main__":
    test_nccst_password_functions()
