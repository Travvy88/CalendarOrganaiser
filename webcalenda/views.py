from django.shortcuts import render
from django.utils import timezone
import calendar


def show_calendar(request, m=1, y=2020):
    c = calendar.LocaleHTMLCalendar(locale='eng_gb')
    with open('webcalenda/templates/webcalenda/month.html', "w") as f:
        print(c.formatmonth(themonth=m, theyear=y, ), file=f)
    return render(request, 'webcalenda/month.html', {})


def show_month(request, y, m):
    c = calendar.LocaleHTMLCalendar(locale='eng_gb')
    with open('webcalenda/templates/webcalenda/month.html', "w") as f:
        print(c.formatmonth(themonth=m, theyear=y, ), file=f)
    return render(request, 'webcalenda/month.html', {})

