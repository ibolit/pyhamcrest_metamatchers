.. pyhamcrest_metamatchers documentation master file, created by
   sphinx-quickstart on Tue Dec 11 09:34:02 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyhamcrest_metamatchers
===================================================

So that you can match your matchers with matchers, while you are writing matchers!

*But seriously:* Hamcrest and hamcrest-style matchers help in writing modular
and reusable tests, but for that the matchers themselves must be reliable.
Now you can develop your own custom matchers and be sure that they are.
All you need to do is to test them using metamatchers.


.. toctree::
   documentation

.. image:: https://travis-ci.com/ibolit/pyhamcrest_metamatchers.svg?branch=master
    :target: https://travis-ci.com/ibolit/pyhamcrest_metamatchers

The goal of this project is to write a number of utility entities to facilitate the development of proper `hamcrest` style
matchers.

For now we have a metamatcher, that is a matcher that can check that a matcher under development behaves
properly, that is it matches whatever it is supposed to match, and it doesn't match whatever it isn't suppsed to, and
that it produces the correct descriptions and mismatch descriptions. Here is a code example to that effect:

.. code-block:: python

     def test_is_twice_as_big_as(...)
         assert_that(
             is_twice_as_big_as(2),
             matches(4).with_description("An int twice as big as <2>")
         )

     def test_is_twice_as_big_as_not_matching(...)
         assert_that(
             is_twice_as_big_as(2),
             doesnt_match(7)\
                 .with_description("An int twice as big as <2>")\
                 .with_mismatch_description("was <7>")
         )


