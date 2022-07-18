
import re
from datetime import datetime
from datetime import time
from datetime import date
import time


"""MESSAGE={'STATUS': 'SUCCESS', 'DATE': {'year': 2021, 'month': 12, 'day': 13, 'hour': 16, 'minute': 15},
 'TEXT': 'Подписать служебку у начальника'}"""


def main():
    minute = None
    hour = None
    day = None
    month = None
    year = None
    Day_of_week = None
    Repeat_always = None
    Text = None

    Status = 'Success'
    print("О чём Вам напомнить ?")
    text = input()


    Time = re.findall(r"[0-2]\d:[0-5]\d", text)
    mes = re.sub('[0-2]\d:[0-5]\d', '', text)
    rem = re.sub('\d{2}.\d{2}.\d{4}', '', mes)

    match = re.search(r'\d{2}.\d{2}.\d{4}', text)
    date = datetime.strptime(match.group(), '%d.%m.%Y').date()
    day_month_year = str(date)
    year = day_month_year[:4]
    month = day_month_year[5:7]
    day = day_month_year[-2:]

    Year = int(year)
    Month = int(month)
    Day = int(day)


    time1 = str(Time)
    hour = time1[2:4]
    minute = time1[5:7]

    Hour = int(hour)
    Minute = int(minute)

    current_date = datetime.now().replace(microsecond=0)
    text_date = datetime(Year,Month,Day,Hour,Minute)
    delta = text_date - current_date
    sec = delta.total_seconds()
    seconds = int(sec)
    #print(seconds)


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

    if 'завтра' in text:
        day+=1

    if 'через неделю' in text:
        day+=7

    if 'через месяц' in text:
        month+=1

    if 'через полгода' in text:
        month+=6

    if 'через год' in text:
        year+=1



    print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':", Month, ",", "'day':", Day, ",", "'hour':", hour, ",", "'minute':", Minute, "}", ",", "'TEXT':",rem, "}", sep='')

    time.sleep(seconds)

    print(rem)

if __name__ == '__main__':
    main()


