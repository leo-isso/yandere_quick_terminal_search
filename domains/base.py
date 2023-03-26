import requests

class BaseDomain:
    base_url = 'https://yande.re/'
    requests = requests

    @property
    def ENTITY_URL(self):
        return NotImplementedError()

    def get(self, **kwargs):
        params = dict(**kwargs)

        request = self.requests.get(
            url=self.ENTITY_URL,
            params=params,
        )

        return request.json()