# -*- coding: utf-8 -*-

# Copyright (c) 2013-2016 Matthew Zipay <mattz@ninthtest.net>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Test case and runner for
:func:`autologging._find_last_line_number`.

"""

__author__ = "Matthew Zipay <mattz@ninthtest.net>"
__version__ = "1.0.0"

import unittest

from autologging import _find_last_line_number

from test import has_co_lnotab


def sample_function():
    x = "test"
    return x


class SampleClass(object):
    
    def method(self):
        x = "test"
        return x


class FindLastLineNumberTest(unittest.TestCase):
    """Test the :func:`autologging._find_last_line_number` function."""

    def test_finds_last_line_number_of_function(self):
        self.assertEqual(
            40 if has_co_lnotab else 38,
            _find_last_line_number(sample_function.__code__))

    def test_finds_last_line_number_of_method(self):
        self.assertEqual(
            47 if has_co_lnotab else 45,
            _find_last_line_number(SampleClass.__dict__["method"].__code__))


def suite():
    return unittest.makeSuite(FindLastLineNumberTest)


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())

