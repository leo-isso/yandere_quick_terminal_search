from domains.base import BaseDomain
from utils import split_tags

class Posts(BaseDomain):
    def __init__(self, tags):
        super().__init__()
        self.ENTITY_URL = f'{self.base_url}post.json'
        self.tags = tags
        self.page = 0

    def get(self):
        params = dict(
            tags=split_tags(self.tags),
            page=self.page
        )

        request = self.requests.get(
            url=self.ENTITY_URL,
            params=params,
        )

        return request.json()
    