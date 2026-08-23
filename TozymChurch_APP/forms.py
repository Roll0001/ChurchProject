from django import forms
from django.utils.translation import gettext_lazy as _

from .models import church_schedule


class ChurchScheduleForm(forms.ModelForm):
    class Meta:
        model = church_schedule
        fields = [
            'date', 'time', 'weekday', 'service_type', 'holiday', 'title', 'description',
        ]
        labels = {
            'date': _('Дата'),
            'time': _('Час'),
            'weekday': _('День тижня'),
            'service_type': _('Богослужіння'),
            'holiday': _('Свято'),
            'title': _('Назва'),
            'description': _('Опис'),
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'weekday': forms.Select(),
            'service_type': forms.Select(),
            'holiday': forms.Select(),
            'title': forms.TextInput(attrs={'placeholder': _('Необов’язково, якщо вибрано свято або богослужіння')}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': _('Додаткова інформація (необов’язково)')}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('title') and not cleaned_data.get('holiday') and not cleaned_data.get('service_type'):
            self.add_error('title', _('Введіть назву або виберіть богослужіння чи свято.'))
        return cleaned_data
