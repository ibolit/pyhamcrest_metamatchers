import pytest
from hamcrest import assert_that
from hamcrest.core.base_matcher import BaseMatcher

from pyhamcrest_metamatchers.metamatchers import doesnt_match, matches


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


class TestMetamatchers:
    def test_matches(self, always_matches):
        assert_that(
            always_matches("hello"),
            matches("hello").with_description("This is a description")
        )


    def test_metamatcher_matches(self, always_matches):
        assert_that(
            matches(always_matches("dude")),
            matches(always_matches(
                "dude")).with_description("A matcher that matches the item.")
        )


    def test_wrong_description(self, always_matches):
        assert_that(
            matches(always_matches("dude")).with_description("Wrong description"),
            doesnt_match(always_matches("dude"))
                .with_description(
                    "A matcher that matches the item. "
                    "With the description: <Wrong description>")
                .with_mismatch_description("The description was <This is a description>. ")
        )


    def test_never_matching_correct_mismatch_descr(self, never_matches):
        assert_that(
            matches(never_matches("dude"))
                .with_description("This is a description")
                .with_mismatch_description("This is a mismatch description"),
            doesnt_match(never_matches("dude"))
                .with_description(
                    "A matcher that matches the item. "
                    "With the description: <This is a description>")
                .with_mismatch_description("The matcher did not match. ")
        )


    def test_never_matching_wrong_mismatch_descr(self, never_matches):
        assert_that(
            matches(never_matches("dude"))
                .with_description("This is a description")
                .with_mismatch_description("Wrong mismatch description"),
            doesnt_match(never_matches("dude"))
                .with_description(
                    "A matcher that matches the item. "
                    "With the description: <This is a description>")
                .with_mismatch_description("The matcher did not match. ")
        )
