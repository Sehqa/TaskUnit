import requests.cookies
from  smart_assertions import soft_assert, verify_expectations
from methods import Met
import pytest
listass=[]

@pytest.mark.parametrize('url',['https://httpbin.org/get'])
@pytest.mark.parametrize('headerss',[{'accept':'*/*'}])
@pytest.mark.parametrize('paramss',[{'key1':'value1'}])
@pytest.mark.parametrize('answercode',['290'])
def test_check_status_code(url,headerss,paramss,answercode):
    soft_assert(Met._gethttp(url,headerss,paramss).status_code)
    verify_expectations()



@pytest.mark.parametrize('d1',['2002,08,5'])
@pytest.mark.parametrize('d2',['2020,07,22'])
@pytest.mark.parametrize('d3',['2005,05,21'])

def test_interval(d1,d2,d3):
    soft_assert(Met._ininterval(d1,d2,d3))
    verify_expectations()

@pytest.mark.parametrize('dat1',['2029,07,22'])

def test_indiff(dat1):
    assert  Met._datedifference(dat1)

@pytest.mark.parametrize("list1",[(1,2,3)])
@pytest.mark.parametrize("list2",[(1,2,4)])
def test_mas(list1,list2):
     assert Met._compars_mass(list1,list2)

@pytest.mark.parametrize("filename",[('log.txt')])
@pytest.mark.parametrize("url",[('https://stepik.org')])
@pytest.mark.parametrize("level",[(2)])

def test_logger(filename,url,level):
     assert Met._logger(filename,url,level)

@pytest.mark.parametrize('d1',['2029,05,22'])
@pytest.mark.parametrize('d2',['2029,05,22'])

def test_comparsdate(d1,d2):
    assert  Met._comparsdate(d1,d2)

@pytest.mark.parametrize('dict',[{}])
def test_sqldict(dict):
    assert Met._dictfrombd(dict)

#@pytest.mark.parametrize(
