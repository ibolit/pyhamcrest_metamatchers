from hamcrest import assert_that, equal_to, is_

from pyhamcrest_metamatchers.metamatchers import matches
from tests.util import get_mismatch_description, get_description


def assert_description(matcher, expected_description):
    description = get_description(matcher)
    assert_that(description, equal_to(expected_description))


def assert_mismatch_description(matcher, item, expected):
    md = get_mismatch_description(matcher, item)
    assert_that(md, equal_to(expected))


class TestMetamatchersMatches:
    def test_simple_matches(self, always_matches):
        assert_that(
            always_matches("hello"),
            matches("hello").with_description("This is a description")
        )


    def test_simple_matches_but_mismatch_provided(self, always_matches, anything):
        """
        Check that when we call `matches` with a mismatch description we should get an error.
        """

        matcher = matches(anything).with_mismatch_description("wrong")
        match_result = matcher._matches(always_matches())

        assert_mismatch_description(
            matcher, always_matches(),
            "The matcher matched, but a mismatch description was provided")

        assert_that(match_result, is_(False))


    def test_matches(self, always_matches, anything):
        """assert_that(anything(), always_matches())
        We check that when we
        """
        matcher = matches(anything)
        match_result = matcher._matches(always_matches())
        assert_description(matcher, "A matcher that matches the item.")
        assert_that(match_result, is_(True))


    def test_matches_with_description(self, always_matches, anything):
        """assert_that(anything(), always_matches())
        We check that when we
        """
        matcher = matches(anything).with_description("This is a description")
        match_result = matcher._matches(always_matches())
        assert_description(matcher, "A matcher that matches the item. "
            "With the description: <This is a description>")
        assert_that(match_result, is_(True))


    def test_not_matches_with_wrong_description(self, always_matches, anything):
        """The .with_description() clause should be the description
        that the `always_matches()` matcher gives out."""

        matcher = matches(anything).with_description("Wrong description")
        match_result = matcher._matches(always_matches())

        assert_description(
            matcher, "A matcher that matches the item. "
            "With the description: <Wrong description>")

        assert_mismatch_description(
            matcher, always_matches(),
            "The description was <This is a description>. ")

        assert_that(match_result, is_(False))


    def test_not_matches__no_description(self, never_matches, anything):
        """
        Dude

        Here we pass a matcher that never matches and check that the description is correct"""

        matcher = matches(anything)
        match_result = matcher._matches(never_matches())
        assert_mismatch_description(
            matcher, never_matches(), "The matcher did not match. ")
        assert_that(match_result, is_(False))


    def test_not_matches__correct_description(self, never_matches, anything):
        """
        Dude

        Here we pass a matcher that never matches and check that the description is correct"""

        matcher = matches(anything).with_description("This is a description")
        match_result = matcher._matches(never_matches())

        assert_description(
            matcher, "A matcher that matches the item. "
            "With the description: <This is a description>")

        assert_mismatch_description(
            matcher, never_matches(), "The matcher did not match. ")

        assert_that(match_result, is_(False))


    def test_not_matches__wrong_description(self, never_matches, anything):
        """
        Dude

        Here we pass a matcher that never matches and check that the description is correct"""

        matcher = matches(anything).with_description("Wrong description")
        match_result = matcher._matches(never_matches())

        assert_description(
            matcher, "A matcher that matches the item. "
            "With the description: <Wrong description>")

        assert_mismatch_description(
            matcher, never_matches(),
            "The matcher did not match. The description was <This is a description>. ")

        assert_that(match_result, is_(False))


    def test_not_matches__wrong_description_correct_mismatch(
            self, never_matches, anything):
        """
        Dude

        Here we pass a matcher that never matches and check that the description is correct"""

        matcher = matches(anything)\
            .with_description("Wrong description")\
            .with_mismatch_description("This is a mismatch description")
        match_result = matcher._matches(never_matches())

        assert_description(
            matcher,
            "A matcher that matches the item. "
            "With the description: <Wrong description> "
            "With tne mismatch_description: <This is a mismatch description>")

        assert_mismatch_description(
            matcher, never_matches(),
            "The matcher did not match. The description was <This is a description>. ")

        assert_that(match_result, is_(False))


    def test_not_matches__wrong_description_wrong_mismatch(
            self, never_matches, anything):
        """
        Dude

        Here we pass a matcher that never matches and check that the description is correct"""

        matcher = matches(anything)\
            .with_description("Wrong description")\
            .with_mismatch_description("Wrong mismatch description")
        match_result = matcher._matches(never_matches())

        assert_description(
            matcher,
            "A matcher that matches the item. "
            "With the description: <Wrong description> "
            "With tne mismatch_description: <Wrong mismatch description>")

        assert_mismatch_description(
            matcher, never_matches(),
            "The matcher did not match. "
            "The description was <This is a description>. "
            "The mismatch_description was <This is a mismatch description>. ")

        assert_that(match_result, is_(False))
