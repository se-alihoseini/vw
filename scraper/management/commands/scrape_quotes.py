import asyncio
import requests
from scraper.schema import PageContext
from typing import Iterable, List
from urllib.parse import urlparse, urlunparse
from django.core.management import BaseCommand, CommandError

from scraper.classes import Normalizer, Hashing




class Command(BaseCommand):
    help = "Fetches paginated quote pages and processes each item through the chain."

    def __init__(self):
        super().__init__()
        self.base_url = "https://quotes.toscrape.com/page/"
        self.start_page = 1
        self.session = requests.Session()


    def handle(self, *args, **options):
        page_param = options["page_param"]

        try:
            self.crawl(base_url=self.base_url, page_param=page_param, start_page=self.start_page)
        except Exception as exc:
            raise CommandError(str(exc)) from exc



    def crawl(self, base_url: str, page_param: str, start_page: int = 1):
        handler = self.build_chain()
        page = start_page

        while True:
            context = PageContext(
                url=self.build_page_url(base_url=self.base_url, page=page),
                number=page,
            )
            self.stdout.write(f"Fetching page {context.number}: {context.url}")
            html = self.fetch_page(context.url)
            if html is None:
                raise CommandError()

            objects = self.parse_objects(html, context)
            self.process_objects(objects, handler)
            page += 1



    def build_chain(self):
        normalize = Normalizer()
        hash_step = Hashing()

        normalize.set_next(hash_step)
        return normalize


    def fetch_page(self, url: str) -> str | None:
        response = self.session.get(url)
        if response.status_code == 404:
            return None

        response.raise_for_status()
        return response.text



    def parse_objects(self, html: str, context: PageContext) -> List[dict]:
        self.stdout.write(self.style.WARNING(f"No parser implemented yet for page {context.number}."))
        return []




    def process_objects(self, objects: Iterable[dict], handler):
        for index, obj in enumerate(objects, start=1):
            try:
                result = asyncio.run(handler.handle(obj))
            except Exception :
                continue

            self.stdout.write(self.style.SUCCESS(f"Object #{index} processed: {result}"))



    def build_page_url(self, base_url: str, page: int) -> str:
        parsed = base_url+f"{page}"
        return parsed
