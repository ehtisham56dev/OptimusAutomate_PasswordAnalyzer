# ============================================================
# PROJECT 1: Password Strength Analyzer
# Internship Project for Optimus Automate | Beginner Friendly
# Uses ONLY built-in Python libraries — no pip install needed!
# ============================================================

import re        # Built-in: lets us search for patterns in text (like "does it have a number?")
import string    # Built-in: gives us ready-made lists of letters, digits, punctuation

# ── FUNCTION 1 ──────────────────────────────────────────────
def analyze_password(password):
    """
    Checks a password and returns a score + list of feedback tips.
    Think of it like a teacher grading your homework with comments.
    """
    score = 0           # Start at 0; we'll add points for each good rule passed
    feedback = []       # Empty list; we'll add tip messages as we find problems

    # RULE 1 — Length check
    # A longer password is harder to guess, like a longer lock combination
    if len(password) >= 12:
        score += 2                          # Bonus: 12+ chars is great
    elif len(password) >= 8:
        score += 1                          # OK: 8-11 chars is acceptable
    else:
        feedback.append("❌ Too short! Use at least 8 characters.")

    # RULE 2 — Uppercase letters (A-Z)
    # re.search looks for ANY uppercase letter in the password string
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one UPPERCASE letter (A-Z).")

    # RULE 3 — Lowercase letters (a-z)
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z).")

    # RULE 4 — Digits (0-9)
    if re.search(r'\d', password):          # \d means "any digit"
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # RULE 5 — Special characters like !@#$%
    # string.punctuation is a ready-made string of all special symbols
    if re.search(r'[' + re.escape(string.punctuation) + r']', password):
        score += 2                          # Bonus: special chars are very strong
    else:
        feedback.append("❌ Add a special character like ! @ # $ % & *")

    # RULE 6 — Penalise common/weak passwords (a tiny blacklist)
    common = ["password", "123456", "qwerty", "abc123", "letmein"]
    if password.lower() in common:          # .lower() makes check case-insensitive
        score = 0                           # Reset score — this is dangerously weak
        feedback.append("🚨 This is one of the most common passwords ever! Change it NOW.")

    # Decide a label based on the final score
    if score >= 6:
        strength = "🟢 STRONG"
    elif score >= 4:
        strength = "🟡 MODERATE"
    else:
        strength = "🔴 WEAK"

    return score, strength, feedback        # Return all three results at once

# ── FUNCTION 2 ──────────────────────────────────────────────
def show_result(password):
    """ Calls analyze_password() and prints the results nicely. """
    score, strength, feedback = analyze_password(password)   # Unpack the 3 return values

    print("\n" + "=" * 45)
    print(f"  Password : {'*' * len(password)}")             # Hide the actual password
    print(f"  Score    : {score} / 7")
    print(f"  Strength : {strength}")
    print("=" * 45)

    if feedback:                            # Only print tips if there are any
        print("  💡 Suggestions to improve:")
        for tip in feedback:               # Loop through each tip in the list
            print(f"     {tip}")
    else:
        print("  ✅ Great password! No suggestions.")
    print()

# ── MAIN MENU ───────────────────────────────────────────────
def main():
    """ The main menu loop. Keeps running until the user chooses to quit. """
    print("\n🔐 Welcome to the Password Strength Analyzer")
    print("   Internship Project — Optimus Automate\n")

    while True:                             # Loop forever until we break out
        print("  [1] Analyze a password")
        print("  [2] Quit")
        choice = input("\n  Enter choice (1 or 2): ").strip()   # .strip() removes accidental spaces

        if choice == "1":
            try:
                # getpass hides typing — but we use input() so beginners can see it clearly
                pwd = input("  Enter password to test: ")
                if pwd == "":              # Guard against empty input
                    print("  ⚠️  You didn't type anything. Try again.\n")
                else:
                    show_result(pwd)
            except KeyboardInterrupt:      # Handles Ctrl+C gracefully
                print("\n  Exiting...\n")
                break

        elif choice == "2":
            print("\n  👋 Goodbye! Stay secure.\n")
            break                          # Exit the while loop → program ends

        else:
            print("  ⚠️  Invalid choice. Please enter 1 or 2.\n")   # Handle bad input

# ── ENTRY POINT ─────────────────────────────────────────────
# This block only runs when you execute THIS file directly,
# not if another file imports it — standard Python best practice.
if __name__ == "__main__":
    main()
