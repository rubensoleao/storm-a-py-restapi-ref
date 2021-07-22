import re


def validate_email(compared_str: str):
    """Email validation src: https://emailregex.com/"""
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, compared_str) and True


# TODO: Validate what phone number formats are allowed and based on this validate regex, or even
#       remove this validation if necessary
def validate_phone(compared_str: str):
    """Regex that matches various phone types and doesn't have size limits
    examples: (412) 9999-9999, (16) 8888-8888, +55 (16) 8888-8888, +55168888-8888, 01699999999
    """
    phone_regex = r"(^([+]|[0])*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$)"
    return re.match(phone_regex, compared_str) and True
