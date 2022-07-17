
import re
from datetime import datetime

"""MESSAGE={'STATUS': 'SUCCESS', 'DATE': {'year': 2021, 'month': 12, 'day': 13, 'hour': 16, 'minute': 15},
 'TEXT': 'Подписать служебку у начальника'}"""


def main():
    time_minute = None
    time_hour = None
    day = None
    month = None
    year = None
    Day_of_week = None
    Repeat_always = None

    Status = 'Error'
    print("О чём Вам напомнить ?")
    text = input()

    time = re.findall(r"[0-2]\d:[0-5]\d", text)
    mes = re.sub('[0-2]\d:[0-5]\d', '', text)

    match = re.search(r'\d{2}.\d{2}.\d{4}', text) #находим дату
    date = datetime.strptime(match.group(), '%d.%m.%Y').date()
    day_month_year = str(date)
    year =  day_month_year[:4]
    month = day_month_year[5:7]
    day = day_month_year[-2:]
    print(year)
    print(month)
    print(day)

    time1 = str(time)
    time_hour = time1[2:4]
    time_minute = time1[5:7]




    if ('в понедельник' or 'каждый понедельник' or 'понедельник' or 'Понедельник' or 'по понедельникам') in text:
        day = 'Monday'

    if ('во вторник' or 'каждый вторник' or 'вторник' or 'Вторник' or 'по вторникам') in text:
        day = 'Tuestday'

    if ('в среду' or 'каждую среду' or 'среда' or 'Среда' or 'по средам') in text:
        day = 'Wednsday'

    if ('в четверг' or 'каждый четверг' or 'четверг' or 'Четверг' or 'по четвергам') in text:
        day = 'Thursday'

    if ('в пятницу' or 'каждую пятницу' or 'пятница' or 'Пятница' or 'по пятницам') in text:
        day = 'Friday'

    if ('в субботу' or 'каждую субботу' or 'суббота' or 'Суббота' or 'по субботам') in text:
        day = 'Saturday'

    if ('в воскресенье' or 'каждое воскресенье' or 'воскресенье' or 'Воскресенье' or 'по воскресеньям') in text:
        day = 'Sunday'



    print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", year, ",", "'month':", month, ",", "'day':", day, ",", "'hour':", time_hour, ",", "'minute':", time_minute, "}", ",", "'TEXT':", mes, "}", sep='')

if __name__ == '__main__':
    main()


