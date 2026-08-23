from calendar import monthrange
from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from .forms import ChurchScheduleForm
from .models import church_schedule

MONTHS = {
    1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень',
    5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень',
    9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'
}


def _month_days(year, month):
    first_day = date(year, month, 1)
    days_in_month = monthrange(year, month)[1]
    month_start_weekday = first_day.weekday()

    cells = []
    for _ in range(month_start_weekday):
        cells.append({'day': '', 'is_outside': True, 'is_today': False, 'events': []})

    for day_number in range(1, days_in_month + 1):
        day = date(year, month, day_number)
        day_events = church_schedule.objects.filter(date=day).order_by('time')
        cells.append({
            'day': day_number,
            'is_outside': False,
            'is_today': day == date.today(),
            'events': list(day_events),
        })

    while len(cells) % 7 != 0:
        cells.append({'day': '', 'is_outside': True, 'is_today': False, 'events': []})

    return cells


def home(request):
    today = date.today()
    month_name = _(MONTHS[today.month])
    month_events = church_schedule.objects.filter(
        date__year=today.year,
        date__month=today.month,
    ).order_by('date', 'time')[:6]

    context = {
        'month_name': month_name,
        'year': today.year,
        'calendar_days': _month_days(today.year, today.month),
        'events': month_events,
    }
    return render(request, 'home.html', context)


def information(request):
    return render(request, 'information.html')


def schedule(request):
    today = date.today()
    month_name = _(MONTHS[today.month])
    month_events = church_schedule.objects.filter(
        date__year=today.year,
        date__month=today.month,
    ).order_by('date', 'time')

    context = {
        'month_name': month_name,
        'year': today.year,
        'calendar_days': _month_days(today.year, today.month),
        'events': month_events,
    }
    return render(request, 'schedule.html', context)


@login_required(login_url='login')
def add_schedule_event(request):
    if request.method == 'POST':
        form = ChurchScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    else:
        form = ChurchScheduleForm()

    return render(request, 'add-event.html', {
        'form': form,
    })
