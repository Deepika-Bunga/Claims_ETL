from datetime import datetime
import hashlib
 
def trim_spaces(value):
 
    if value is None:
        return None
 
    return str(value).strip()
 
 
def standardize_id(value):
 
    if value is None:
        return None
 
    return str(value).strip().zfill(8)
 
 
def clean_phone(value):
 
    if value is None:
        return None
 
    digits = ''.join(
        ch for ch in str(value)
        if ch.isdigit()
    )
 
    return digits[:10]
 
 
def clean_email(value):
 
    if value is None:
        return None
 
    email = str(value).strip().lower()
 
    allowed = set(
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
        "@._+-"
    )
 
    email = ''.join(
        ch for ch in email
        if ch in allowed
    )
 
    return email
 
 
def standardize_date(value):
 
    if value is None:
        return None
 
    return str(value)


def clean_boolean(value):
 
    if value is None:
        return None
    
    if value is True:
        return "Y"
    
    if value is False:
        return "N"
 
    value = str(value).strip().lower()
 
    if value in ["true", "1", "yes", "y"]:
        return "Y"
 
    if value in ["false", "0", "no", "n"]:
        return "N"
 
    return value

def generate_checksum(values):
 
    row_string = "|".join(
        "" if v is None else str(v)
        for v in values
    )
 
    return hashlib.md5(
        row_string.encode("utf-8")
    ).hexdigest()

import uuid
 
def add_surrogate_and_checksum(row, table_name, checksum_values):
 
    surrogate_key = str(uuid.uuid4())
 
    checksum = generate_checksum(
        checksum_values
    )
 
    row.append(surrogate_key)
    row.append(checksum)
 
    return row
 