from random import randint

def get_numbers_ticket(min:int, max:int, quantity:int) -> list:
    """
    The function generates the specified number of unique numbers in a given range
    
    :param min: Minimum possible number in the set (not less than 1)
    :type min: int
    :param max: Maximum possible number in the set (no more than 1000)
    :type max: int
    :param quantity: Amount of numbers you want to select (values between min and max)
    :type quantity: int
    :return: Returns a list of randomly selected numbers
    :rtype: list
    """
    if min >= 1 and max <= 1000 and max - min >= quantity:
        result = set()
        while len(result) <= quantity-1:
            result.add(randint(min, max))
        return sorted(list(result))
    else: return []

print(get_numbers_ticket(1,59,5))
print(get_numbers_ticket(1,4,3))