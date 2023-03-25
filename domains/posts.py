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
    

class PostInterface:
    domain_name = 'Images'
    selected_message = '\nImages selected'
    input_message = 'Search for tags: '

    def _format_output(self, json_response):
        output = ''

        for item in json_response:
            id = item['id']
            file_url = item['file_url']
            tags = item['tags']

            output = f'{output}\nID: {id}\nFile URL: {file_url}\nTags: {tags}\n'

        return output