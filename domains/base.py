import requests


class BaseDomain:
    base_url = 'https://yande.re/'
    requests = requests

    @property
    def ENTITY_URL(self):
        return NotImplementedError()

    def _handle_params(self, filters, page):
        return NotImplementedError()

    def get(self, filters, page):
        params = self._handle_params(filters, page)

        request = self.requests.get(
            url=self.ENTITY_URL,
            params=params,
            timeout=30
        )

        return request.json()
