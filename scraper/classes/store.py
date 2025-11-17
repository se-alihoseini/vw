import hashlib
import json
from base import BaseHandler
from scraper.models import Quote, Author, Tag, Log

class Store(BaseHandler):
    def handle(self, data):
        try:
            log, created = Log.objects.get_or_create(
                hash=data.get('hash'),
            )
            if not created:
                raise Exception

            author, _ = Author.objects.get_or_create(
                name=data.get('author'),
            )

            quote = Quote.objects.create(
                content=data.get('text'),
                author=author,
            )

            for tag in data.get('tags'):
                tag, _ = Tag.objects.get_or_create(
                    content=tag,
                )
                quote.tag.add(tag)

            return self.run_next(data)
        except Exception as e:
            print(e)


#9 processed: {'text': "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", 'author': 'Eleanor Roosevelt', 'tags': ['misattributed-eleanor-roosevelt'], 'hash': '48d6501ec0c037381ac103c6911d5039c3714578ea069e024c22782cd8017d9d'}
