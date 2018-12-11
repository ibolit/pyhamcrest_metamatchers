import pytest
from hamcrest import equal_to, assert_that


@pytest.fixture
def hello():
    return "hello"

class TestNothing:
    """Just to check that we can run tests on the free travis-ci.org account"""

    def test_nothin(self, hello):
        assert_that(hello, equal_to("hello"))
