from smart_assertions import soft_assert, verify_expectations
import requests_mock
from framework.from_get_post import Get_Post


def teardown():
    verify_expectations()


def test_get_request():
    with requests_mock.Mocker() as m:
        m.get(url='http://example.com/get_status', status_code=200)
        r = Get_Post._gethttp('http://example.com/get_status', {'accept': '*/*'}, {'key1': 'value1'})
        soft_assert(r.status_code == 200)


def test_post_request():
    with requests_mock.Mocker() as m:
        m.post(url='http://example.com/get_status', status_code=404)
        r = Get_Post._posthttp('http://example.com/get_status', {'accept': '*/*'}, {'key1': 'value1'}, {'key1': 'value1'})
        soft_assert(r.status_code == 404)
