from framework.utils import Utils
from  smart_assertions import soft_assert, verify_expectations

from framework.listmet import ListMet
from framework.db import Db
import pytest
listass=[]

def teardown():
    verify_expectations()


@pytest.mark.parametrize("list1",[(1,2,3)])
@pytest.mark.parametrize("list2",[(1,2,4)])
def test_mas(list1,list2):
     soft_assert(ListMet._compars_mass(list1,list2))


@pytest.mark.parametrize("filename",[('log.txt')])
@pytest.mark.parametrize("url",[('https://stepik.org')])
@pytest.mark.parametrize("level",[(2)])


def test_logger(filename,url,level):
     soft_assert(Utils._logger(filename,url,level))





@pytest.mark.parametrize('dict',[{}])
def test_sqldict(dict):
    soft_assert(Db._dictfrombd(dict))


