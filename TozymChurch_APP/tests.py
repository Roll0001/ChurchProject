from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import override

from .models import church_schedule

# Create your tests here.


class ScheduleCreationTests(TestCase):
	def test_guest_is_redirected_to_login(self):
		response = self.client.get(reverse('add_schedule_event'))

		self.assertRedirects(
			response,
			f"{reverse('login')}?next={reverse('add_schedule_event')}",
		)

	def test_authenticated_user_can_create_event(self):
		user = User.objects.create_user(username='parishioner', password='test-pass-123')
		self.client.force_login(user)

		response = self.client.post(reverse('add_schedule_event'), {
			'date': '2026-08-30',
			'time': '10:00',
			'title': 'Святкова літургія',
			'description': 'Недільне богослужіння',
		})

		self.assertRedirects(response, reverse('schedule'))
		self.assertTrue(church_schedule.objects.filter(title='Святкова літургія').exists())

	def test_event_keeps_simple_title_and_description(self):
		event = church_schedule.objects.create(
			date='2026-08-30',
			title='Святкова літургія',
			description='Недільне богослужіння',
		)

		with override('pl'):
			self.assertEqual(event.localized_title, 'Святкова літургія')
			self.assertEqual(event.localized_description, 'Недільне богослужіння')

	def test_holiday_is_localized_without_manual_title(self):
		event = church_schedule.objects.create(
			date='2026-12-25',
			holiday='christmas',
			weekday=4,
		)

		with override('en'):
			self.assertEqual(event.localized_title, 'Nativity of Christ')
			self.assertEqual(event.localized_weekday, 'Friday')

	def test_service_type_is_localized_without_manual_title(self):
		event = church_schedule.objects.create(
			date='2026-08-30',
			service_type='moleben_akathist',
		)

		with override('pl'):
			self.assertEqual(event.localized_title, 'Nabożeństwo z akatystem')
