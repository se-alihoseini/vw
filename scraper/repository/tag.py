from scraper.models import Tag


class TagRepository:

    @staticmethod
    def get_by_id(id: int) -> Tag:
        ...