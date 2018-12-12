==================
Code Documentation
==================

Metamatcher is a matcher that checks that another matcher behaves correctly.

When new matchers are developed, it is vital to check that they match
as expected and produce helpful desriptions and mismatch_descriptions.

This metamatcher does exactly that.

Say, you have written a matcher called ``is_twice_as_big_as``, and you want it
to compare ints. You intend to use it like this::

    assert_that(4, is_twice_as_big_as(2))

Under the hood, the following is called::

    is_twice_as_big_as(2)._matches(4)

Keeping that in mind, here's how you can check your matcher with the
metamatcher::

    def test_is_twice_as_big_as(...)
        assert_that(
            # Your initialized matcher
            is_twice_as_big_as(2),
            # The metamatcher specifying the value for matching
            matches(4)
        )

This will fail if your ``is_twice_as_big_as`` matcher doesn't match.

To check that your matcher produces the correct description::

    def test_is_twice_as_big_as(...)
        assert_that(
            is_twice_as_big_as(2),
            matches(4).with_description("An int twice as big as <2>")
        )

This will fail if your ``is_twice_as_big_as`` matcher doesn't match,
if the description it produces is wrong, or both.

You can also check that your matcher doesn't match in certain situations.
To do that, use the ``doesnt_match`` function, and to check the mismatch
description, call the ``with_mismatch_description`` method.

Note, that you can use the ``with_description`` method with the
``doesnt_match`` metamatcher, but calling ``with_mismatch_description``
with the ``matches`` flavour of the metamatcher, will throw an exception.


matches
^^^^^^^

.. autofunction:: pyhamcrest_metamatchers.metamatchers.matches


doesnt_match
^^^^^^^^^^^^

.. autofunction:: pyhamcrest_metamatchers.metamatchers.doesnt_match


with_description
^^^^^^^^^^^^^^^^
.. automethod:: pyhamcrest_metamatchers.metamatchers.MetaMatcher.with_description

with_mismatch_description
^^^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: pyhamcrest_metamatchers.metamatchers.MetaMatcher.with_mismatch_description
