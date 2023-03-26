from domains.base import BaseDomain

class Posts(BaseDomain):
    @property
    def ENTITY_URL(self):
        return f'{self.base_url}post.json'
    
    def handle_params(filter, page):
        return dict(
            tags=filter,
            page=page
        )