from scraper.models import Quote


class QuoteRepository:

    @staticmethod
    def get_by_id(id: int) -> Quote:
        ...