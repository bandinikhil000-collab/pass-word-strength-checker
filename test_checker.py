"""
Unit Tests for Password Strength Checker Application
---------------------------------------------------
Tests all individual check functions, scoring logic, and edge cases.
Uses Python's built-in unittest module (no external dependencies).
"""

import unittest
from password_checker import (
    check_minimum_length,
    check_uppercase,
    check_lowercase,
    check_number,
    check_special_character,
    evaluate_password,
    get_meter_bar,
)


class TestPasswordChecker(unittest.TestCase):
    """Test suite for individual conditions and overall evaluation."""

    # 1. Length checks
    def test_minimum_length(self):
        self.assertFalse(check_minimum_length(""))
        self.assertFalse(check_minimum_length("1234567"))
        self.assertTrue(check_minimum_length("12345678"))
        self.assertTrue(check_minimum_length("1234567890abcdef"))

    # 2. Uppercase checks
    def test_uppercase(self):
        self.assertFalse(check_uppercase("password"))
        self.assertFalse(check_uppercase("123456!@#"))
        self.assertTrue(check_uppercase("Password"))
        self.assertTrue(check_uppercase("pAssWORD"))

    # 3. Lowercase checks
    def test_lowercase(self):
        self.assertFalse(check_lowercase("PASSWORD"))
        self.assertFalse(check_lowercase("123456!@#"))
        self.assertTrue(check_lowercase("Password"))
        self.assertTrue(check_lowercase("p"))

    # 4. Number checks
    def test_number(self):
        self.assertFalse(check_number("Password"))
        self.assertFalse(check_number("!@#$%^&*"))
        self.assertTrue(check_number("Password1"))
        self.assertTrue(check_number("999"))

    # 5. Special character checks
    def test_special_character(self):
        self.assertFalse(check_special_character("Password123"))
        self.assertTrue(check_special_character("Password123!"))
        self.assertTrue(check_special_character("@"))
        self.assertTrue(check_special_character("test#test$"))

    # 6. Overall Evaluation & Rating Tiers
    def test_rating_very_weak(self):
        # Empty or very few criteria met
        res_empty = evaluate_password("")
        self.assertEqual(res_empty["rating"], "Very Weak")
        self.assertEqual(res_empty["score"], 0)
        self.assertEqual(len(res_empty["missing"]), 5)

        res_short = evaluate_password("abc")
        self.assertEqual(res_short["rating"], "Very Weak")
        self.assertEqual(res_short["score"], 1)

    def test_rating_weak(self):
        # Meets 2 criteria: length + lowercase
        res = evaluate_password("mypassword")
        self.assertEqual(res["rating"], "Weak")
        self.assertEqual(res["score"], 2)
        self.assertEqual(len(res["missing"]), 3)

        # Short password with multiple features is capped at Weak
        res_short_combo = evaluate_password("A1!b")
        self.assertEqual(res_short_combo["rating"], "Weak")

    def test_rating_medium(self):
        # Meets 3 criteria: length + lowercase + uppercase
        res = evaluate_password("MyPassword")
        self.assertEqual(res["rating"], "Medium")
        self.assertEqual(res["score"], 3)
        self.assertEqual(len(res["missing"]), 2)

    def test_rating_strong(self):
        # Meets 4 criteria: length + lowercase + uppercase + number (missing special)
        res = evaluate_password("MyPassword123")
        self.assertEqual(res["rating"], "Strong")
        self.assertEqual(res["score"], 4)
        self.assertEqual(len(res["missing"]), 1)
        self.assertIn("special character", res["missing"][0])

    def test_rating_very_strong(self):
        # Meets all 5 criteria
        res = evaluate_password("MyP@ssw0rd!2026")
        self.assertEqual(res["rating"], "Very Strong")
        self.assertEqual(res["score"], 5)
        self.assertEqual(len(res["missing"]), 0)

    # 7. Privacy check - Ensure actual password string is NOT stored in evaluation dict
    def test_no_password_stored(self):
        secret = "SecretP@ssword123!"
        res = evaluate_password(secret)
        self.assertNotIn("password", res)
        for val in res.values():
            self.assertNotEqual(val, secret)

    # 8. Visual meter bar
    def test_meter_bar(self):
        bar_0 = get_meter_bar(0)
        self.assertIn("0%", bar_0)
        bar_5 = get_meter_bar(5)
        self.assertIn("100%", bar_5)


if __name__ == "__main__":
    unittest.main()
