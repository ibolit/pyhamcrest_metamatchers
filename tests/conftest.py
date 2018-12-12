import pytest
from hamcrest.core.base_matcher import BaseMatcher


class MockAlwaysMatchingMatcher(BaseMatcher):
    def __init__(self, *args, **kwargs):
        super().__init__()


    def _matches(self, item):
        return True


    def describe_to(self, description):
        description.append_text("This is a description")


    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text("This is a mismatch description")


class MockNeverMatchingMatcher(MockAlwaysMatchingMatcher):
    def _matches(self, item):
        return False


@pytest.fixture
def always_matches():
    return MockAlwaysMatchingMatcher


@pytest.fixture
def never_matches():
    return MockNeverMatchingMatcher

@pytest.fixture
def anything():
    return "this is just a value"
