from scraper.models import Author


class AuthorRepository:

    @staticmethod
    def get_by_id(id: int) -> Author:
        ...