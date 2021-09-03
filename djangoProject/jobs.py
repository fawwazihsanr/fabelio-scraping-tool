from core.views import create_submission
from core.models import Scraper
from django_cron import CronJobBase, Schedule
from rest_framework.test import APIRequestFactory


class Jobs(CronJobBase):
    RUN_EVERY_MINS = 60
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'djangoProject.jobs'

    def do(self):
        factory = APIRequestFactory()
        scrapers = Scraper.objects.all()
        for scraper in scrapers:
            data = {
                'url': scraper.url
            }
            factory.post('/submission', data)
