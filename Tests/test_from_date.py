import pytest
from framework.from_date import For_date
from smart_assertions import soft_assert, verify_expectations


def teardown():
    verify_expectations()


@pytest.mark.parametrize('date_1', ['2002,08,5'])
@pytest.mark.parametrize('date_2', ['2020,07,22'])
@pytest.mark.parametrize('date_3', ['2005,05,21'])
def test_interval(date_1, date_2, date_3):
    soft_assert(For_date._ininterval(date_1, date_2, date_3))


@pytest.mark.parametrize('date_1', ['2002,08,5'])
@pytest.mark.parametrize('date_2', ['2000,07,22'])
@pytest.mark.parametrize('date_3', ['2005,05,21'])
# negative
def test2_interval(date_1, date_2, date_3):
    soft_assert(For_date._ininterval(date_1, date_2, date_3))


@pytest.mark.parametrize('date_11', ['2029,07,22'])
def test_indiff(date_11):
    soft_assert(For_date._datedifference(date_11))


# negative
@pytest.mark.parametrize('dat1', ['202'])
def test2_indiff(dat1):
    soft_assert(For_date._datedifference(dat1))


@pytest.mark.parametrize('date_1', ['2029,05,22'])
@pytest.mark.parametrize('date_2', ['2029,05,22'])
def test_comparsdate(date_1, date_2):
    soft_assert(For_date._comparsdate(date_1, date_2))


# negative

@pytest.mark.parametrize('date_1', ['2029,05,22'])
@pytest.mark.parametrize('date_2', ['244144'])
def test_2comparsdate(date_1, date_2):
    soft_assert(For_date._comparsdate(date_1, date_2))
