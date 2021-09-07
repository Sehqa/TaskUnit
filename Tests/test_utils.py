from framework.utils import Utils
from smart_assertions import soft_assert, verify_expectations
from framework.listmet import ListMet
from framework.db import Db
import pytest


def teardown():
    verify_expectations()


@pytest.mark.parametrize("list1", [(1, 2, 3)])
@pytest.mark.parametrize("list2", [(0, 2, 4)])
@pytest.mark.parametrize("typeinobj", ['str'])
def test_mas(list1, list2, typeinobj):
    soft_assert(ListMet._compars_mass(list1, list2, typeinobj))


@pytest.mark.parametrize("list1", [('bool')])
@pytest.mark.parametrize("list2", [('ddddd')])
@pytest.mark.parametrize("typeinobj", ['ssaasdrw,fsdfsd,fdsfsd,111111111'])
# negative
def test2_mas(list1, list2, typeinobj):
    soft_assert(ListMet._compars_mass(list1, list2, typeinobj))


@pytest.mark.parametrize("filename", [('log.txt')])
@pytest.mark.parametrize("url", [('https://stepik.org')])
@pytest.mark.parametrize("level", [(2)])
def test_logger(filename, url, level):
    soft_assert(Utils._logger(filename, url, level))


@pytest.mark.parametrize('zapr', ["SELECT * FROM users;"])
def test_sqldict(zapr):
    soft_assert(Db._dictfrombd(zapr))


@pytest.mark.parametrize('zapr', ['ssssss'])
# negative
def test2_sqldict(zapr):
    soft_assert(Db._dictfrombd(zapr))
