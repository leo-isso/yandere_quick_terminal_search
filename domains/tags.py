from domains.base import BaseDomain

class Tags(BaseDomain):
    @property
    def ENTITY_URL(self):
        return f'{self.base_url}tag.json'
    
    def handle_params(filter, page):
        return dict(
            name=filter,
            page=page
        )