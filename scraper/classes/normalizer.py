from typing import Any, Dict, List

from bs4.element import Tag

from base import BaseHandler


class Normalizer(BaseHandler):
    def handle(self, data: Any):
        raw = self._extract_raw_fields(data)
        cleaned = {
            "text": raw.get("text", "").strip(),
            "author": raw.get("author", "").strip(),
            "tags": self._normalize_tags(raw.get("tags", [])),
        }

        return self.run_next(cleaned)

    def _extract_raw_fields(self, data: Any) -> Dict[str, Any]:
        if isinstance(data, dict):
            return data

        if not isinstance(data, Tag):
            raise ValueError("Normalizer expects a BeautifulSoup Tag or dict-like object.")

        text_node = data.find("span", class_="text")
        author_node = data.find("small", class_="author")
        tags_container = data.find("div", class_="tags")

        tags: List[str] = []
        if tags_container:
            tag_links = tags_container.find_all("a", class_="tag")
            tags = [tag.get_text(strip=True) for tag in tag_links]

            if not tags:
                meta = tags_container.find("meta", class_="keywords")
                if meta and meta.has_attr("content"):
                    tags = [keyword.strip() for keyword in meta["content"].split(",") if keyword.strip()]

        return {
            "text": text_node.get_text(strip=True) if text_node else "",
            "author": author_node.get_text(strip=True) if author_node else "",
            "tags": tags,
        }

    @staticmethod
    def _normalize_tags(tags: List[str]) -> List[str]:
        return [tag.strip() for tag in tags if tag and tag.strip()]
