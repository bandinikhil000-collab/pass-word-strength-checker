"""
Password Strength Checker Application
-------------------------------------
A clean, modular, and beginner-friendly Python program to evaluate the strength
of passwords based on security best practices.

Requirements Evaluated:
1. Minimum 8 characters in length
2. At least one uppercase letter (A-Z)
3. At least one lowercase letter (a-z)
4. At least one numeric digit (0-9)
5. At least one special character (!@#$%^&* etc.)

Ratings:
- Very Weak
- Weak
- Medium
- Strong
- Very Strong

Security Notice:
- The actual password is never displayed, logged, or permanently stored.
- Standard Python libraries only (no third-party dependencies required).
"""

import getpass
import string
import sys

# Define standard set of special punctuation characters
SPECIAL_CHARACTERS = string.punctuation


# =====================================================================
# INDIVIDUAL REQUIREMENT CHECK FUNCTIONS
# Each function inspects the password for one specific condition
# and returns a boolean (True if satisfied, False otherwise).
# =====================================================================

def check_minimum_length(password: str, min_length: int = 8) -> bool:
    """Check if the password meets the minimum character length."""
    return len(password) >= min_length


def check_uppercase(password: str) -> bool:
    """Check if the password contains at least one uppercase letter (A-Z)."""
    for char in password:
        if char.isupper():
            return True
    return False


def check_lowercase(password: str) -> bool:
    """Check if the password contains at least one lowercase letter (a-z)."""
    for char in password:
        if char.islower():
            return True
    return False


def check_number(password: str) -> bool:
    """Check if the password contains at least one numeric digit (0-9)."""
    for char in password:
        if char.isdigit():
            return True
    return False


def check_special_character(password: str) -> bool:
    """
    Check if the password contains at least one special character.
    Special characters include symbols like: ! @ # $ % ^ & * ( ) _ + - = etc.
    """
    for char in password:
        if char in SPECIAL_CHARACTERS:
            return True
    return False


# =====================================================================
# CORE EVALUATION LOGIC
# Combines all checks, computes the score, and assigns a rating.
# =====================================================================

def evaluate_password(password: str) -> dict:
    """
    Evaluates the password against all five criteria.

    Returns a dictionary containing:
    - 'results': Dictionary mapping each requirement to True/False
    - 'score': Numeric score from 0 to 5
    - 'rating': Text rating ('Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong')
    - 'missing': List of user-friendly descriptions for missing criteria
    - 'length': Length of the evaluated password (without keeping the actual text)
    """
    # 1. Run all condition checks
    results = {
        "length": check_minimum_length(password, min_length=8),
        "uppercase": check_uppercase(password),
        "lowercase": check_lowercase(password),
        "number": check_number(password),
        "special": check_special_character(password),
    }

    # 2. Identify missing requirements with clear explanations
    missing_explanations = {
        "length": "Must have at least 8 characters (longer passwords are harder to crack).",
        "uppercase": "Add at least one uppercase letter (A-Z).",
        "lowercase": "Add at least one lowercase letter (a-z).",
        "number": "Add at least one number (0-9).",
        "special": f"Add at least one special character (e.g. ! @ # $ % ^ & *).",
    }

    missing = [
        missing_explanations[key]
        for key, passed in results.items()
        if not passed
    ]

    # 3. Calculate score (1 point per satisfied requirement, range 0 to 5)
    score = sum(1 for passed in results.values() if passed)

    # 4. Determine rating based on score
    # Security Rule: If length is less than 8, a password cannot exceed 'Weak'
    # because short passwords can easily be cracked via brute-force regardless of variety.
    if len(password) < 8:
        if score <= 1:
            rating = "Very Weak"
        else:
            rating = "Weak"
    else:
        # Standard grading when minimum length (8 chars) is satisfied
        if score <= 1:
            rating = "Very Weak"
        elif score == 2:
            rating = "Weak"
        elif score == 3:
            rating = "Medium"
        elif score == 4:
            rating = "Strong"
        else:
            rating = "Very Strong"

    # Store only the metadata, not the actual password
    evaluation = {
        "results": results,
        "score": score,
        "rating": rating,
        "missing": missing,
        "length": len(password),
    }

    return evaluation


# =====================================================================
# USER INTERFACE & DISPLAY FUNCTIONS
# Formats output cleanly without revealing or storing sensitive data.
# =====================================================================

def get_meter_bar(score: int, max_score: int = 5) -> str:
    """Generate a visual progress meter bar for the score (100% cross-platform)."""
    total_blocks = 10
    # Map score (0-5) to 10 visual blocks
    filled_blocks = int((score / max_score) * total_blocks)
    empty_blocks = total_blocks - filled_blocks
    bar = "=" * filled_blocks + "-" * empty_blocks
    percentage = int((score / max_score) * 100)
    return f"[{bar}] {percentage}%"


def display_results(evaluation: dict) -> None:
    """
    Renders a friendly, easy-to-read evaluation report.
    Crucial: The actual password is NEVER printed or saved.
    """
    results = evaluation["results"]
    score = evaluation["score"]
    rating = evaluation["rating"]
    missing = evaluation["missing"]
    length = evaluation["length"]

    print("\n" + "=" * 55)
    print("               PASSWORD STRENGTH REPORT")
    print("=" * 55)

    # Display overall rating and visual meter
    print(f" Password Length : {length} characters")
    print(f" Overall Rating  : {rating.upper()}")
    print(f" Strength Score  : {score}/5")
    print(f" Visual Meter    : {get_meter_bar(score)}")
    print("-" * 55)

    # Criteria checklist
    print(" Requirement Breakdown:")
    labels = {
        "length": "Minimum 8 characters",
        "uppercase": "At least one uppercase letter (A-Z)",
        "lowercase": "At least one lowercase letter (a-z)",
        "number": "At least one number (0-9)",
        "special": "At least one special character (!@#$%...)",
    }

    for key, label in labels.items():
        status = "[PASS]" if results[key] else "[FAIL]"
        print(f"  {status.ljust(8)} : {label}")

    print("-" * 55)

    # Feedback on missing requirements or congratulations
    if missing:
        print(" How to Improve Your Password:")
        for idx, tip in enumerate(missing, 1):
            print(f"  {idx}. {tip}")
    else:
        print(" Excellent! Your password satisfies all security criteria.")

    print("=" * 55 + "\n")


# =====================================================================
# EXAMPLE DEMONSTRATIONS
# Runs predefined test inputs showing output for each strength tier.
# =====================================================================

def run_examples() -> None:
    """
    Demonstrates the checker using example inputs for each rating tier.
    Useful for verifying behavior and learning how the scoring works.
    """
    examples = [
        ("hi", "Very short lowercase word"),
        ("mypassword", "8+ characters but all lowercase letters"),
        ("Password1", "Uppercase, lowercase, numbers, but no special characters"),
        ("Passw0rd!", "Uppercase, lowercase, numbers, and special characters (8 chars)"),
        ("Str0ng!P@ssw0rd#2026", "Well above 8 chars, mixed case, numbers, special characters"),
    ]

    print("\n" + "#" * 60)
    print("       DEMONSTRATION: EXAMPLE INPUTS AND OUTPUTS")
    print("#" * 60)

    for idx, (sample_pw, note) in enumerate(examples, 1):
        print(f"\n--- Example {idx}: '{sample_pw}' ({note}) ---")
        evaluation = evaluate_password(sample_pw)
        display_results(evaluation)

    print("#" * 60)
    print("       END OF DEMONSTRATION")
    print("#" * 60 + "\n")


# =====================================================================
# MAIN APPLICATION LOOP
# Prompts the user, executes checks, and ensures safe variable cleanup.
# =====================================================================

def prompt_password() -> str:
    """
    Asks the user for a password.
    Offers standard visible typing or hidden masked entry for privacy.
    """
    print("\nChoose input mode:")
    print("  [1] Standard input (visible as you type)")
    print("  [2] Hidden input (masked for privacy)")

    mode = input("Select mode (1 or 2, default is 1): ").strip()

    if mode == "2":
        try:
            # getpass masks the password in standard terminal environments
            entered = getpass.getpass("Enter password to check (input is hidden): ")
        except Exception:
            # Fallback if getpass is not supported in the active terminal
            entered = input("Enter password to check: ")
    else:
        entered = input("Enter password to check: ")

    return entered


def main() -> None:
    """Main interactive application loop."""
    print("=" * 50)
    print("       WELCOME TO PASSWORD STRENGTH CHECKER")
    print("=" * 50)
    print("Check if your password is safe, strong, and resilient.")
    print("Privacy guarantee: Passwords are never saved or displayed.")

    while True:
        print("\nMain Menu:")
        print("  [1] Check a password")
        print("  [2] View example inputs and outputs")
        print("  [3] Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            user_password = prompt_password()

            # Handle empty input case gracefully
            if not user_password:
                print("\n[!] Error: No password entered. Please enter a valid password.")
                continue

            # Evaluate password
            evaluation = evaluate_password(user_password)

            # Security requirement 6:
            # Overwrite and delete the raw password variable from memory immediately
            del user_password

            # Display the formatted report
            display_results(evaluation)

        elif choice == "2":
            run_examples()

        elif choice == "3":
            print("\nThank you for using Password Strength Checker. Stay safe online!\n")
            sys.exit(0)

        else:
            print("\n[!] Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
