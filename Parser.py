import re
from datetime import datetime
from datetime import time
from datetime import date
import time

"""MESSAGE={'STATUS': 'SUCCESS', 'DATE': {'year': 2021, 'month': 12, 'day': 13, 'hour': 16, 'minute': 15},
 'TEXT': 'Подписать служебку у начальника'}"""

global find_delayed_minute, find_delayed_hour, rem


def delayed_action(a,b):
    delayed_minute = int(find_delayed_minute)

    delayed_hour = int(find_delayed_hour)

    try:

        sec = delayed_hour * 3600 + delayed_minute * 60
        seconds = int(sec)
        time.sleep(seconds)
        print(rem)

    except OverflowError:

        print('Неправильный ввод')




def main():
    Status = 'Success'
    print("О чём Вам напомнить ?")
    text = input()
    my_list = text.split()

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

    try:
        current_date = datetime.now().replace(second=0, microsecond=0)
        text_date = datetime(Year, Month, Day, Hour, Minute)
        delta = text_date - current_date
        sec = delta.total_seconds()

        seconds = int(sec)
        time.sleep(seconds)
    except OverflowError:
        print('Неправильный ввод даты')

    else: print(rem)


    try:

            if 'сегодня в ' or 'сегодня на ' or 'Сегодня в ' or 'Сегодня на ' in text:

                time.sleep(0)

            if 'завтра в ' or 'завтра на ' or 'Завтра в ' or 'Завтра на ' in text:
                Day += 1
                time.sleep(86400)

            if 'послезавтра в ' or 'послезавтра на' or 'Послезавтра в ' or 'Послезавтра на' in text:
                Day += 2
                time.sleep(2 * 86400)

            if 'через неделю в ' or 'через неделю на' or 'Через неделю в ' or 'Через неделю на' in text:
                Day += 7
                time.sleep(7 * 86400)

            if 'через месяц в ' or 'через неделю на' or 'Через месяц в ' or 'Через неделю на' in text:
                Month += 1
                time.sleep(31 * 86400)

            if 'через год в ' or 'через год на' or 'Через год в ' or 'Через год на ' in text:
                Year +=1
                time.sleep(365 * 86400)

    except AttributeError:
        pass

    try:

        for i in range(len(my_list)):

            if my_list[i] == 'Через' or my_list[i] == 'через':
                if 0 < int(my_list[i + 1]) < 60 and (
                        my_list[i + 2] == 'минуту' or my_list[i + 2] == 'минуты' or my_list[i + 2] == 'минут'):
                    find_delayed_minute = my_list[i + 1]
                    find_delayed_hour = 0

            if 0 < int(my_list[i + 1]) < 24 and (
                    my_list[i + 2] == 'час' or my_list[i + 2] == 'часа' or my_list[i + 2] == 'часов'):
                find_delayed_minute = 0
                find_delayed_hour = my_list[i + 1]

            if 0 < int(my_list[i + 1]) < 24 and (
                    my_list[i + 2] == 'час' or my_list[i + 2] == 'часа' or my_list[i + 2] == 'часов') and \
                    0 < int(my_list[i + 3]) < 60 and (
                    my_list[i + 4] == 'минуту' or my_list[i + 4] == 'минуты' or my_list[i + 4] == 'минут'):
                find_delayed_hour = my_list[i + 1]
                find_delayed_minute = my_list[i + 3]

    except IndexError:

        print(
            'Необходимо ввести в формате: Через (число) часов (число) минут ИЛИ Через (число) часов ИЛИ Через (число) минут')

    else:

        delayed_action(find_delayed_hour)

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

    print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':", Month, ",", "'day':", Day,
          ",", "'hour':", Hour, ",", "'minute':", Minute, "}", ",", "'TEXT':", rem, "}", sep='')

    print(rem)


if __name__ == '__main__':
    main()
