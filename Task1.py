from datetime import datetime

def get_days_from_today(date:str) -> int:
    """
    Docstring for get_days_from_today
    
    :param date: Date in format '2000-10-20'
    :type date: str
    :return: Difference in day between current date and sent date argument
    :rtype: int
    """
    converted = datetime.strptime(date, "%Y-%m-%d").date()
    date_now = datetime.today().date()
    result_days = date_now - converted
    return result_days.days

print(get_days_from_today('2030-10-20'))
assert isinstance(get_days_from_today('2000-10-20'), int)
