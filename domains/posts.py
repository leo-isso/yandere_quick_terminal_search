from domains.base import BaseDomain


class Posts(BaseDomain):
    @property
    def entity_url(self):
        return f'{self.base_url}post.json'

    def _handle_params(self, filters, page):
        return dict(
            tags=filters,
            page=page
        )
