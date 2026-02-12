from datetime import datetime, date, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Gregoriy", "birthday": "1999.02.15"},
    {"name": "Vladyslav", "birthday": "1996.02.14"},
    {"name": "Volodymyr", "birthday": "1996.02.10"}
]


def get_upcoming_birthdays(people:list) -> list:
    """
    Return a people who has a birthday in the next 7 days
    
    :param people: List of the people with the name and DOB
    :type people: list
    :return: List of the people with upcoming birthday
    :rtype: list
    """
    current_date = date.today()
    result = []
    for person in people:    
        formated_date = datetime.strptime(person['birthday'], '%Y.%m.%d').date()     
        upcoming_bday_date = formated_date.replace(year=current_date.year)

        # if BD has already passed we take next year
        if upcoming_bday_date < current_date:
            upcoming_bday_date = upcoming_bday_date.replace(year=current_date.year + 1)

        # weekends handling
        if upcoming_bday_date.weekday() == 6: #sunday
            upcoming_bday_date += timedelta(days=1)
        elif upcoming_bday_date.weekday() == 5: # saturday
            upcoming_bday_date += timedelta(days=2)

        # define next 7 days
        congrat_range = (upcoming_bday_date - current_date).days

        # define a person with BD in range of next 7 days
        if 0 <= congrat_range <= 7:
            result.append({'name': person['name'], 'congratulation_date': upcoming_bday_date})

    return result


print(get_upcoming_birthdays(users))
