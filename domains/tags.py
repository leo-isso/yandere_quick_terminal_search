from domains.base import BaseDomain


class Tags(BaseDomain):
    @property
    def ENTITY_URL(self):
        return f'{self.base_url}tag.json'

    def _handle_params(self, filters, page):
        return dict(
            name=filters,
            page=page
        )
