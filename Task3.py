import re

def normalize_phone(phone_number:str) -> str:
    """
    Normalizes phone numbers to standard format like +380671234567
    
    :param phone_number: Unformatted phone number
    :type phone_number: str
    :return: Normalized phone number
    :rtype: str
    """
    formating_1 = re.sub(r"[^\d]", '', phone_number) # delete symbols and empty space

    if formating_1.startswith('380') and len(formating_1) == 12:
        formating_final = '+' + formating_1
    elif formating_1.startswith('0') and len(formating_1) == 10:
        formating_final = '+38' + formating_1
    else: return 'Incorrect phone number'

    return formating_final

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)
