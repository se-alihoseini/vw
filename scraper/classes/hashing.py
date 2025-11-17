import hashlib
import json
from base import BaseHandler


class Hashing(BaseHandler):
    def handle(self, data):
        raw = json.dumps(data, sort_keys=True, ensure_ascii=False)
        data["hash"] = hashlib.sha256(raw.encode()).hexdigest()

        return self.run_next(data)
