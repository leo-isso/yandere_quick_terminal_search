import requests

class BaseDomain:
    base_url = 'https://yande.re/'
    requests = requests

    @property
    def ENTITY_URL(self):
        return NotImplementedError()
    
    def _handle_params(self):
        return NotImplementedError()

    def get(self, filter, page):
        params = self._handle_params(filter, page)

        request = self.requests.get(
            url=self.ENTITY_URL,
            params=params,
        )

        return request.json()