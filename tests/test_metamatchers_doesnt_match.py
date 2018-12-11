from hamcrest import assert_that, anything, is_, equal_to
from hamcrest.core.string_description import StringDescription

from pyhamcrest_metamatchers.metamatchers import doesnt_match, matches
from tests.conftest import always_matches


class TestMetamatchersMatches:
    def test_doesnt_match(self, never_matches):
        assert_that(
            never_matches("hello"),
            doesnt_match(
                anything())
                    .with_description("This is a description")
                    .with_mismatch_description("This is a mismatch description")
        )


    def test_matches(self, never_matches):
        assert_that(
            doesnt_match(anything()),
            matches(
                never_matches("dude")
            )
                    .with_description("A matcher that does not match the item.")
        )


    def test_simple_matches_but_mismatch_provided(self, always_matches):
        # m1 = matches(anything())
        # match_result_1 = m1._matches(always_matches())
        # assert_that(match_result_1, is_(True))
        #
        m = matches(anything()).with_mismatch_description("wrong")
        match_result = m._matches(always_matches())
        assert_that(match_result, is_(False))

        md = StringDescription()
        m.describe_mismatch(always_matches(), md)
        md = str(md)
        assert_that(md, equal_to(
            "The matcher matched, but a mismatch description was provided"
        ))



    def test_matches_but_mismatch_provided(self, always_matches):
        assert_that(
            matches(anything()).with_mismatch_description("Some description"),
            doesnt_match(
                always_matches("dude")
            )
                    .with_description(
                        "A matcher that matches the item. "
                        "With mismatch_description: <Some description>")
                    .with_mismatch_description(
                        "The matcher matched, but a mismatch description was provided")
        )


    def test_wrong_description(self, never_matches):
        """
        Check that the doesnt_match matcher doesn't match a matcher that
        does not indeed match, but it has a mismatch description that is
        not correct.
        """
        assert_that(
            doesnt_match(anything()).with_description("Wrong description"),
            doesnt_match(never_matches("dude"))
                .with_description(
                    "A matcher that does not match the item. "
                    "With the description: <Wrong description>")
                .with_mismatch_description(
                    "The description was <This is a description>. ")
        )

    def test_correct_description_wrong_mismatch_description(self, never_matches):
        assert_that(
            doesnt_match(anything())
                .with_description("This is a description")
                .with_mismatch_description("A wrong mismatch description"),
            doesnt_match(never_matches("dude")).with_description(
                "A matcher that does not match the item. With the description: "
                "<This is a description> "
                "With mismatch_description: <A wrong mismatch description>")
            .with_mismatch_description(
                "The mismatch_description was <This is a mismatch description>. ")
        )


    def test_no_description_wrong_mismatch_description(self, never_matches):
        assert_that(
            doesnt_match(anything())
                .with_mismatch_description("A wrong mismatch description"),
            doesnt_match(never_matches("dude")).with_description(
                "A matcher that does not match the item. "
                "With mismatch_description: <A wrong mismatch description>")
            .with_mismatch_description(
                "The mismatch_description was <This is a mismatch description>. ")
        )




    # def test_never_matching_correct_mismatch_descr(self, never_matches):
    #     assert_that(
    #         matches(never_matches("dude"))
    #             .with_description("This is a description")
    #             .with_mismatch_description("This is a mismatch description"),
    #         doesnt_match(never_matches("dude"))
    #             .with_description(
    #                 "A matcher that matches the item. "
    #                 "With the description: <This is a description>")
    #             .with_mismatch_description("The matcher did not match. ")
    #     )
    #
    #
    # def test_never_matching_wrong_mismatch_descr(self, never_matches):
    #     assert_that(
    #         matches(never_matches("dude"))
    #             .with_description("This is a description")
    #             .with_mismatch_description("Wrong mismatch description"),
    #         doesnt_match(never_matches("dude"))
    #             .with_description(
    #                 "A matcher that matches the item. "
    #                 "With the description: <This is a description>")
    #             .with_mismatch_description("The matcher did not match. ")
    #     )
