.. pyhamcrest_metamatchers documentation master file, created by
   sphinx-quickstart on Tue Dec 11 09:34:02 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyhamcrest_metamatchers's documentation!
===================================================

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

    def test_wrong_status_with_wrong_headers(response_200):
        assert_that(
            status(300).with_headers({"Hello-Dude": "application/json"}),
            doesnt_match(response_200)
                .with_description(
                    "An HttpResponse object with status_code <300>, "
                    "with headers: \"Hello-Dude: 'application/json'\".")
                .with_mismatch_description(
                    "Status code was: <200>. Does not contain header "
                    "<Hello-Dude>.")
        )

