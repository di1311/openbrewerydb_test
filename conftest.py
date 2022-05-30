import pytest
import requests


class RequestsClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path='/', params=None):
        url = f'{self.base_url}{path}'
        return requests.get(url=url, params=params)

    def post(self, path='/', params=None, json=None):
        url = f'{self.base_url}{path}'
        return requests.post(url=url, params=params, json=json)

    def delete(self, path='/', params=None):
        url = f'{self.base_url}{path}'
        return requests.delete(url=url, params=params)


@pytest.fixture()
def requester():
    return RequestsClient('https://api.openbrewerydb.org')


class TestData:

    breweries_id = (
        '515-brewing-co-clive',
        'motor-city-brewing-works-detroit',
        'outland-farm-brewery-pittsfield',
    )
    city = (
        'Washington',
        'Berthoud',
        'Oakdale'
    )
    postal_code = (
        '15021',
        '80501',
        '37403',
    )
    brewery = {'id': '515-brewing-co-clive',
               'name': '515 Brewing Co',
               'brewery_type': 'micro',
               'street': '7700 University Ave',
               'address_2': None,
               'address_3': None,
               'city': 'Clive',
               'state': 'Iowa',
               'county_province': None,
               'postal_code': '50325-1271',
               'country': 'United States',
               'longitude': '-93.7228408',
               'latitude': '41.599992',
               'phone': '5156614615',
               'website_url': 'http://www.515brewing.com',
               'updated_at': '2021-10-23T02:24:55.243Z',
               'created_at': '2021-10-23T02:24:55.243Z'}
