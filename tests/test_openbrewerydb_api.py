from conftest import TestData
from validation import Brewery, ListOfBreweries, AutocompleteBreweries
import pytest


def test_status_code(requester):
    """ GET https://api.openbrewerydb.org """

    response = requester.get()
    assert response.status_code == 200


@pytest.mark.parametrize("obdb_id", TestData.breweries_id)
def test_single_brewery_with_id(requester, obdb_id):
    """ Get a single brewery.
        GET https://api.openbrewerydb.org/breweries/{obdb-id}
    """

    response = requester.get(path=f'/breweries/{obdb_id}')
    assert response.status_code == 200
    brewery_json = Brewery.parse_raw(response.text, content_type='application/json')
    assert brewery_json.id == obdb_id


@pytest.mark.parametrize('city', TestData.city)
def test_brewery_by_city(requester, city):
    """ Filter breweries by city.
        GET https://api.openbrewerydb.org/breweries?by_city={city}&per_page=1
    """

    params = {'by_city': city,
              'per_page': 1}
    response = requester.get(path='/breweries', params=params)
    assert response.status_code == 200
    breweries_json = ListOfBreweries.parse_raw(response.text, content_type='application/json')
    list_of_breweries = breweries_json.dict().get('__root__')
    # using the key '__root__' you can get a list of breweries
    assert list_of_breweries[0].get('city') == city


@pytest.mark.parametrize('postal_code', TestData.postal_code)
def test_brewery_by_postal_code(requester, postal_code):
    """ Filter breweries by short postal code.
        GET https://api.openbrewerydb.org/breweries?by_postal={postal}&per_page=1
    """

    params = {'by_postal': postal_code,
              'per_page': 1}
    response = requester.get(path='/breweries', params=params)
    assert response.status_code == 200
    breweries_json = ListOfBreweries.parse_raw(response.text, content_type='application/json')
    list_of_breweries = breweries_json.dict().get('__root__')
    # using the key '__root__' you can get a list of breweries
    assert postal_code in list_of_breweries[0].get('postal_code')


@pytest.mark.parametrize("per_page", (0, 1, 10, 20, 30, 50))
def test_list_breweries(requester, per_page):
    """ Returns a list of breweries
        GET https://api.openbrewerydb.org/breweries?per_page={id}
    """

    params = {'per_page': per_page}
    response = requester.get(path='/breweries', params=params)
    assert response.status_code == 200
    breweries_json = ListOfBreweries.parse_raw(response.text, content_type='application/json')
    assert len(breweries_json.dict().get('__root__')) == per_page
    # using the key '__root__' you can get a list of breweries


def test_random_brewery(requester):
    """ Get a random brewery.
        GET https://api.openbrewerydb.org/breweries/random
    """

    response = requester.get(path='/breweries/random')
    assert response.status_code == 200
    ListOfBreweries.parse_raw(response.text, content_type='application/json')


def test_autocomplete_breweries(requester):
    """ Return a list of names and ids of breweries based on a search term. This endpoint is typically used for a
        drop-down selection. The maximum number of breweries returned is 15.
        GET https://api.openbrewerydb.org/breweries/autocomplete?query={search}
    """

    params = {'query': 'cat'}
    response = requester.get(path='/breweries/autocomplete', params=params)
    assert response.status_code == 200
    AutocompleteBreweries.parse_raw(response.text, content_type='application/json')


def test_create_brewery(requester):
    """ POST request with brewery data
        POST https://api.openbrewerydb.org/breweries
    """

    response = requester.post(path='/breweries', json=TestData.brewery)
    assert response.status_code == 404


def test_delete_brewery(requester):
    """ DELETE request
        DELETE https://api.openbrewerydb.org/breweries/madtree-brewing-cincinnati
    """
    response = requester.delete(path='/breweries/madtree-brewing-cincinnati')
    assert response.status_code == 404


def test_single_brewery_with_incorrect_id(requester):
    """ Returns 404 code and message "Couldn't find Brewery"
        GET https://api.openbrewerydb.org/breweries/abcd
    """

    response = requester.get(path='/breweries/abcd')
    assert response.status_code == 404
    assert response.json().get('message') == 'Couldn\'t find Brewery'
