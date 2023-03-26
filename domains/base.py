import requests

class BaseDomain:
    base_url = 'https://yande.re/'
    requests = requests

    @property
    def ENTITY_URL(self):
        return NotImplementedError()
    
    def handle_params():
        return NotImplementedError()

    def get(self, filter, page):
        params = self.handle_params(filter, page)

        request = self.requests.get(
            url=self.ENTITY_URL,
            params=params,
        )

        return request.json()