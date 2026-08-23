from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class church_schedule(models.Model):

    WEEKDAYS = [
        (0, _("Понеділок")),
        (1, _("Вівторок")),
        (2, _("Середа")),
        (3, _("Четвер")),
        (4, _("П'ятниця")),
        (5, _("Субота")),
        (6, _("Неділя")),
    ]
    HOLIDAYS = [
        ("", _("Без свята")),
        ("christmas", _("Різдво Христове")),
        ("epiphany", _("Богоявлення")),
        ("annunciation", _("Благовіщення")),
        ("palm_sunday", _("Вербна неділя")),
        ("easter", _("Великдень")),
        ("ascension", _("Вознесіння Господнє")),
        ("pentecost", _("П'ятидесятниця")),
        ("transfiguration", _("Преображення Господнє")),
        ("dormition", _("Успіння Богородиці")),
        ("michaelmas", _("Собор Архангела Михаїла")),
    ]
    SERVICE_TYPES = [
        ("", _("Виберіть богослужіння")),
        ("divine_liturgy", _("Божественна літургія")),
        ("moleben_akathist", _("Молебень з акафістом")),
        ("moleben", _("Молебень")),
        ("vespers", _("Вечірня")),
        ("matins", _("Утреня")),
        ("confession", _("Сповідь")),
        ("panikhida", _("Панахида")),
        ("prayer_service", _("Молитовне правило")),
        ("parish_meeting", _("Парафіяльна зустріч")),
    ]

    date = models.DateField(
        verbose_name=_("Дата"),
        help_text=_("День, коли відзначається подія")
    )
    time = models.TimeField(
        verbose_name=_("Час"),
        help_text=_("Час проведення події"),
        blank=True,
        null=True,  # якщо час не завжди відомий
    )
    weekday = models.PositiveSmallIntegerField(
        choices=WEEKDAYS,
        blank=True,
        null=True,
        verbose_name=_("День тижня"),
    )
    holiday = models.CharField(
        max_length=32,
        choices=HOLIDAYS,
        blank=True,
        verbose_name=_("Свято"),
    )
    service_type = models.CharField(
        max_length=32,
        choices=SERVICE_TYPES,
        blank=True,
        verbose_name=_("Богослужіння"),
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Назва"),
        help_text=_("Наприклад: 'Новий рік', 'День народження' тощо")
    )
    description = models.TextField(
        verbose_name=_("Опис"),
        blank=True,
        help_text=_("Детальніший опис події (необов'язково)")
    )
    class Meta:
        verbose_name = _("Подія")
        verbose_name_plural = _("Події")
        ordering = ["date", "time"]

    def __str__(self):
        if self.time:
            return f"{self.title} — {self.date} о {self.time.strftime('%H:%M')}"
        return f"{self.title} — {self.date}"

    @property
    def localized_title(self):
        return (
            self.title
            or self.localized_service_type
            or self.localized_holiday
        )

    @property
    def localized_service_type(self):
        if not self.service_type:
            return ''
        return dict(self.SERVICE_TYPES).get(self.service_type, '')

    @property
    def localized_holiday(self):
        if not self.holiday:
            return ''
        return dict(self.HOLIDAYS).get(self.holiday, '')

    @property
    def localized_weekday(self):
        if self.weekday is None:
            return ''
        return dict(self.WEEKDAYS).get(self.weekday, '')

    @property
    def localized_description(self):
        return self.description

class Product(models.Model):
    photo = models.ImageField(upload_to='products/')    
