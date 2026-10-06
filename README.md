# Password Strength Checker (Python)

A clean, modular, and beginner-friendly Python application that evaluates the strength of a password based on security standards and provides clear, actionable feedback to the user.

---

## Features

- **Standard Library Only**: Runs directly in Python 3 without installing any third-party dependencies (`pip`).
- **5 Security Criteria Checked**:
  1. Minimum 8 characters
  2. At least one uppercase letter (`A-Z`)
  3. At least one lowercase letter (`a-z`)
  4. At least one number (`0-9`)
  5. At least one special character (`!@#$%^&*...`)
- **Clear Rating Tiers**:
  - `Very Weak` (Score 0-1)
  - `Weak` (Score 2, or passwords under 8 characters)
  - `Medium` (Score 3)
  - `Strong` (Score 4)
  - `Very Strong` (Score 5 / all criteria satisfied)
- **Actionable Guidance**: Highlights precisely which requirements are missing when a password is weak.
- **Privacy & Security Focused**: The raw password is never stored, logged, or displayed on screen after input. It is removed from memory right after analysis.
- **Flexible Input Modes**: Choose between standard visible input or hidden input (using Python's `getpass`).
- **Built-in Demo Mode**: Includes an interactive example runner showing inputs and detailed outputs for each rating level.
- **Unit Tested**: Includes comprehensive tests covering all criteria and edge cases.

---

## Project Structure

```text
pass word strength checker/
│
├── password_checker.py   # Main application containing all modular functions and CLI
├── test_checker.py       # Unit test suite verifying all conditions and edge cases
└── README.md             # Documentation, setup guide, and example inputs/outputs
```

---

## How to Run

### 1. Run the Main Application
Open your terminal (PowerShell, Command Prompt, or bash) in the project directory and run:

```bash
python password_checker.py
```

You will see the interactive menu:
```text
==================================================
       WELCOME TO PASSWORD STRENGTH CHECKER
==================================================
Check if your password is safe, strong, and resilient.
Privacy guarantee: Passwords are never saved or displayed.

Main Menu:
  [1] Check a password
  [2] View example inputs and outputs
  [3] Exit
Enter your choice (1/2/3):
```

### 2. Run the Automated Unit Tests
To verify all functions and scoring rules:

```bash
python test_checker.py
```

---

## Example Inputs & Outputs

### Example 1: Very Weak
- **Input**: `hi`
- **Output Report**:
```text
=======================================================
               PASSWORD STRENGTH REPORT
=======================================================
 Password Length : 2 characters
 Overall Rating  : VERY WEAK
 Strength Score  : 1/5
 Visual Meter    : [==--------] 20%
-------------------------------------------------------
 Requirement Breakdown:
  [FAIL]   : Minimum 8 characters
  [FAIL]   : At least one uppercase letter (A-Z)
  [PASS]   : At least one lowercase letter (a-z)
  [FAIL]   : At least one number (0-9)
  [FAIL]   : At least one special character (!@#$%...)
-------------------------------------------------------
 How to Improve Your Password:
  1. Must have at least 8 characters (longer passwords are harder to crack).
  2. Add at least one uppercase letter (A-Z).
  3. Add at least one number (0-9).
  4. Add at least one special character (e.g. ! @ # $ % ^ & *).
=======================================================
```

---

### Example 2: Weak
- **Input**: `mypassword`
- **Output Report**:
```text
=======================================================
               PASSWORD STRENGTH REPORT
=======================================================
 Password Length : 10 characters
 Overall Rating  : WEAK
 Strength Score  : 2/5
 Visual Meter    : [====------] 40%
-------------------------------------------------------
 Requirement Breakdown:
  [PASS]   : Minimum 8 characters
  [FAIL]   : At least one uppercase letter (A-Z)
  [PASS]   : At least one lowercase letter (a-z)
  [FAIL]   : At least one number (0-9)
  [FAIL]   : At least one special character (!@#$%...)
-------------------------------------------------------
 How to Improve Your Password:
  1. Add at least one uppercase letter (A-Z).
  2. Add at least one number (0-9).
  3. Add at least one special character (e.g. ! @ # $ % ^ & *).
=======================================================
```

---

### Example 3: Medium
- **Input**: `Password1`
- **Output Report**:
```text
=======================================================
               PASSWORD STRENGTH REPORT
=======================================================
 Password Length : 9 characters
 Overall Rating  : MEDIUM
 Strength Score  : 4/5
 Visual Meter    : [========--] 80%
-------------------------------------------------------
 Requirement Breakdown:
  [PASS]   : Minimum 8 characters
  [PASS]   : At least one uppercase letter (A-Z)
  [PASS]   : At least one lowercase letter (a-z)
  [PASS]   : At least one number (0-9)
  [FAIL]   : At least one special character (!@#$%...)
-------------------------------------------------------
 How to Improve Your Password:
  1. Add at least one special character (e.g. ! @ # $ % ^ & *).
=======================================================
```

---

### Example 4: Strong
- **Input**: `Passw0rd!`
- **Output Report**:
```text
=======================================================
               PASSWORD STRENGTH REPORT
=======================================================
 Password Length : 9 characters
 Overall Rating  : VERY STRONG
 Strength Score  : 5/5
 Visual Meter    : [==========] 100%
-------------------------------------------------------
 Requirement Breakdown:
  [PASS]   : Minimum 8 characters
  [PASS]   : At least one uppercase letter (A-Z)
  [PASS]   : At least one lowercase letter (a-z)
  [PASS]   : At least one number (0-9)
  [PASS]   : At least one special character (!@#$%...)
-------------------------------------------------------
 Excellent! Your password satisfies all security criteria.
=======================================================
```

---

### Example 5: Very Strong (Longer complex passphrase)
- **Input**: `Str0ng!P@ssw0rd#2026`
- **Output Report**:
```text
=======================================================
               PASSWORD STRENGTH REPORT
=======================================================
 Password Length : 19 characters
 Overall Rating  : VERY STRONG
 Strength Score  : 5/5
 Visual Meter    : [==========] 100%
-------------------------------------------------------
 Requirement Breakdown:
  [PASS]   : Minimum 8 characters
  [PASS]   : At least one uppercase letter (A-Z)
  [PASS]   : At least one lowercase letter (a-z)
  [PASS]   : At least one number (0-9)
  [PASS]   : At least one special character (!@#$%...)
-------------------------------------------------------
 Excellent! Your password satisfies all security criteria.
=======================================================
```

---

## Code Organization

The code in [`password_checker.py`](file:///c:/Users/CFS/Downloads/pass%20word%20strength%20checker/password_checker.py) is modularized into single-responsibility functions:

| Function | Purpose |
|---|---|
| [`check_minimum_length`](file:///c:/Users/CFS/Downloads/pass%20word%20strength%20checker/password_checker.py#L31) | Verifies if `len(password) >= 8` |
| [`check_uppercase`](file:///c:/Users/CFS/Downloads/pass%20word%20strength%20checker/password_checker.py#L36) | Checks for at least one uppercase letter (`isupper()`) |
| [`check_lowercase`](file:///c:/Users/CFS/Downloads/pass%20word%20strength%20checker/password_checker.py#L44) | Checks for at least one lowercase letter (`islower()`) |
| [`check_number`](file:///c:/Users/CFS/Downloads/pass%20word%20strength%20checker/password_checker.py#L52) | Checks for at least one digit (`isdigit()`) |
| [`check_special_character`](file:///c:/Users/CFS/Downloads/pass%20word%20strength%20checker/password_checker.py#L60) | Checks against `string.punctuation` symbols |
| [`evaluate_password`](file:///c:/Users/CFS/Downloads/pass%20word%20strength%20checker/password_checker.py#L76) | Coordinates all checks, calculates the score (0-5), identifies missing requirements, and sets the rating |
| [`get_meter_bar`](file:///c:/Users/CFS/Downloads/pass%20word%20strength%20checker/password_checker.py#L161) | Generates a 10-block visual progress bar |
| [`display_results`](file:///c:/Users/CFS/Downloads/pass%20word%20strength%20checker/password_checker.py#L172) | Outputs a clean report without exposing the password |
| [`run_examples`](file:///c:/Users/CFS/Downloads/pass%20word%20strength%20checker/password_checker.py#L225) | Demonstrates outputs across all rating tiers |
| [`prompt_password`](file:///c:/Users/CFS/Downloads/pass%20word%20strength%20checker/password_checker.py#L251) | Handles user input with visible or hidden options |
| [`main`](file:///c:/Users/CFS/Downloads/pass%20word%20strength%20checker/password_checker.py#L274) | Interactive application loop with memory cleanup |
