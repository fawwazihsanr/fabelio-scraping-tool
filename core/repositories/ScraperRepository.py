import pdb

from ..models import Scraper
from django.forms.models import model_to_dict


class ScraperRepository:
    @staticmethod
    def create(data):
        scraper, created = Scraper.objects.update_or_create(
            url=data['url'],
            defaults={
                'name': data['name'],
                'price': data['price'],
                'description': data['description'][0].get_text(),
                'image': data['image']
            }
        )
        return scraper.id

    @staticmethod
    def read_by_id(id):
        data = Scraper.objects.get(pk=id)
        return model_to_dict(data)

    @staticmethod
    def read():
        data = Scraper.objects.all().values()
        return data
