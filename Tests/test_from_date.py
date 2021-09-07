import pytest
from framework.from_date import For_date
from smart_assertions import soft_assert, verify_expectations


def teardown():
    verify_expectations()


@pytest.mark.parametrize('d1', ['2002,08,5'])
@pytest.mark.parametrize('d2', ['2020,07,22'])
@pytest.mark.parametrize('d3', ['2005,05,21'])
def test_interval(d1, d2, d3):
    soft_assert(For_date._ininterval(d1, d2, d3))


@pytest.mark.parametrize('dat1', ['2029,07,22'])
def test_indiff(dat1):
    soft_assert(For_date._datedifference(dat1))


@pytest.mark.parametrize('d1', ['2029,05,22'])
@pytest.mark.parametrize('d2', ['2029,05,22'])
def test_comparsdate(d1, d2):
    soft_assert(For_date._comparsdate(d1, d2))
