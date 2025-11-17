from base import BaseHandler

class Normalizer(BaseHandler):

    async def handle(self, data):
        cleaned = {
            "text": data["text"].strip(),
            "author": data["author"].strip(),
            "tags": data.get("tags", []),
        }

        return await self.run_next(cleaned)
