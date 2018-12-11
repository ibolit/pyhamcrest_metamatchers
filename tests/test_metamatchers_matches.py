import pytest
from hamcrest import assert_that

from pyhamcrest_metamatchers.metamatchers import doesnt_match, matches

@pytest.mark.skip
class TestMetamatchersMatches:
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
