#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('16-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([98, 402, 510, 1]), 510)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_assert_true(self):
        self.assertTrue(max_integer([98, 402, 510, 1]), 510)
        self.assertTrue(max_integer([1, 3, 4, 2]), 4)

    def test_list_None(self):
        self.assertEqual(max_integer([]), None)

    def test_not_None(self):
        self.assertIsNotNone(max_integer([98, 402, 510, 1]))
        self.assertIsNotNone(max_integer([1, 3, 4, 2]))

    def test_strings_list(self):
        self.assertEqual(max_integer(["1", "2", "3", "4"]), "4")
        self.assertEqual(max_integer(["1", "3", "4", "2"]), "4")

    def test_letters_strings_list(self):
        self.assertEqual(max_integer(["d", "b", "a", "r"]), "r")
        self.assertEqual(max_integer(["a", "l", "c", "r"]), "r")

    def test_floats_list(self):
        self.assertEqual(max_integer([102.0, 20.0, 63.0, 44.0]), 102.0)
        self.assertEqual(max_integer([1.0, 3.0, 4.0, 2.0]), 4.0)

    def test_big_values_list(self):
        self.assertEqual(max_integer([4110, 2080, 3050, 42730]), 42730)
        self.assertEqual(max_integer([100, 3200, 203]), 3200)

    def test_neg_list(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_list(self):
        self.assertEqual(max_integer(["-1", "1", "c", "m"]), "m")


if __name__ == "__main__":
    unittest.main()
