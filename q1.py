# //Test-Case:1 => Input— D = 12020-01-01%4, '2020-01-02% 4, '2020-01-03% 6, '2020-01-04% 8,'202001-05': 2,
# //'2020-01-05 -6, '2020-01-07% 2, 2026-01-08.: -2)
# //Output — 0 = ['Mon': -6, 'Tue.: 2, 'Wed: 2, 'Thu': 4, 'Fff: 8, 'Sat': 8, 'Sun': 2}


import calendar
from datetime import datetime

days = [('2020/01/01', '4 '), ('2020/01/02', '4 '), ('2020/01/03', '6 '),('2020/01/04', '8 '), ('2020/01/05', '2 '), ('2020/01/06', '-6 '),('2020/01/07', '2 '),('2020/01/08', '2 ')]

totals = dict(zip(calendar.day_name, [0] * 7))
for date_str, value_str in days:
    totals[datetime.strptime(date_str, "%Y/%m/%d").strftime("%A")] += int(value_str)


print(totals)


