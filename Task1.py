from datetime import datetime

def get_days_from_today(date:str) -> int:
    """
    Function calculates the number of days between a given date and the current date
    
    :param date: Date in format '2000-10-20'
    :type date: str
    :return: Difference in day between current date and sent date argument
    :rtype: int
    """
    try:
        converted = datetime.strptime(date, "%Y-%m-%d").date()
        date_now = datetime.today().date()
        result_days = date_now - converted
        return result_days.days
    except Exception as e:
        return f"{e} Please, input data in format 'YYYY-MM-DD'"

print(get_days_from_today('2030-10-20'))
print(get_days_from_today('2030^10f20'))
assert isinstance(get_days_from_today('2000-10-20'), int)
