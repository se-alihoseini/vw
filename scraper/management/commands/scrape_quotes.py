from django.core.management import BaseCommand
from scraper.classes import Normalizer, Hashing


class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.client = ...

    def handle(self, *args, **options):
        self.run_chain()

    def run_chain(self):
        normalize = Normalizer()
        hash_step = Hashing()

        normalize.set_next(hash_step)

        item = {
            "text": "   The world as we have created it ... ",
            "author": " Albert Einstein ",
            "tags": ["thinking", "change"]
        }

        result = normalize.handle(item)
        self.stdout.write(self.style.SUCCESS(str(result)))
