import re
import math
import string

# ── Common weak passwords list ─────────────────────────────────────────────
COMMON_PASSWORDS = [
    "password", "123456", "password123", "admin", "letmein",
    "qwerty", "abc123", "monkey", "1234567", "12345678",
    "iloveyou", "sunshine", "princess", "dragon", "master",
    "hello", "welcome", "shadow", "superman", "michael",
    "football", "charlie", "donald", "password1", "qwerty123"
]

# ── Analyze password ───────────────────────────────────────────────────────
def analyze_password(password: str) -> dict:
    """Full analysis of a password — returns a result dictionary."""

    results = {
        "password":        password,
        "score":           0,        # 0 to 100
        "strength":        "",       # Weak / Fair / Strong / Very Strong
        "entropy":         0,        # how unpredictable the password is
        "checks":          {},       # individual check results
        "suggestions":     [],       # improvement tips
        "crack_time":      ""        # estimated time to crack
    }

    checks = {}
    suggestions = []
    score = 0

    # ── Basic checks ───────────────────────────────────────────────────────

    # Length
    length = len(password)
    checks["length_8"]  = length >= 8
    checks["length_12"] = length >= 12
    checks["length_16"] = length >= 16

    if length >= 16:
        score += 25
    elif length >= 12:
        score += 20
    elif length >= 8:
        score += 10
    else:
        score += 0
        suggestions.append("Use at least 8 characters (12+ is ideal)")

    # Uppercase letters
    checks["has_uppercase"] = bool(re.search(r"[A-Z]", password))
    if checks["has_uppercase"]:
        score += 15
    else:
        suggestions.append("Add uppercase letters (A-Z)")

    # Lowercase letters
    checks["has_lowercase"] = bool(re.search(r"[a-z]", password))
    if checks["has_lowercase"]:
        score += 15
    else:
        suggestions.append("Add lowercase letters (a-z)")

    # Numbers
    checks["has_numbers"] = bool(re.search(r"\d", password))
    if checks["has_numbers"]:
        score += 15
    else:
        suggestions.append("Add numbers (0-9)")

    # Special characters
    checks["has_special"] = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=\[\]\\;'/`~]", password))
    if checks["has_special"]:
        score += 20
    else:
        suggestions.append("Add special characters (!@#$%^&*...)")

    # ── Advanced checks ────────────────────────────────────────────────────

    # Common password check
    checks["not_common"] = password.lower() not in COMMON_PASSWORDS
    if not checks["not_common"]:
        score -= 40
        suggestions.append("This is one of the most common passwords — change it immediately!")

    # Repeated characters (e.g. "aaaa", "1111")
    checks["no_repeats"] = not bool(re.search(r"(.)\1{2,}", password))
    if not checks["no_repeats"]:
        score -= 10
        suggestions.append("Avoid repeating the same character 3+ times in a row")

    # Sequential characters (e.g. "abc", "123")
    sequences = ["abcdefghijklmnopqrstuvwxyz", "0123456789", "qwertyuiop", "asdfghjkl"]
    has_sequence = False
    for seq in sequences:
        for i in range(len(seq) - 2):
            if seq[i:i+3] in password.lower():
                has_sequence = True
                break
    checks["no_sequences"] = not has_sequence
    if not checks["no_sequences"]:
        score -= 10
        suggestions.append("Avoid sequential characters like 'abc' or '123'")

    # Only one character type
    checks["mixed_types"] = sum([
        checks["has_uppercase"],
        checks["has_lowercase"],
        checks["has_numbers"],
        checks["has_special"]
    ]) >= 3
    if not checks["mixed_types"]:
        suggestions.append("Mix at least 3 types: uppercase, lowercase, numbers, symbols")

    # ── Entropy calculation ────────────────────────────────────────────────
    charset_size = 0
    if checks["has_lowercase"]:  charset_size += 26
    if checks["has_uppercase"]:  charset_size += 26
    if checks["has_numbers"]:    charset_size += 10
    if checks["has_special"]:    charset_size += 32

    if charset_size > 0 and length > 0:
        entropy = length * math.log2(charset_size)
    else:
        entropy = 0

    results["entropy"] = round(entropy, 1)

    # ── Crack time estimate ────────────────────────────────────────────────
    # Assuming 10 billion guesses per second (modern GPU attack)
    guesses_per_second = 10_000_000_000
    combinations = charset_size ** length if charset_size > 0 else 1
    seconds = combinations / guesses_per_second

    if seconds < 1:
        crack_time = "Instantly"
    elif seconds < 60:
        crack_time = f"{int(seconds)} seconds"
    elif seconds < 3600:
        crack_time = f"{int(seconds/60)} minutes"
    elif seconds < 86400:
        crack_time = f"{int(seconds/3600)} hours"
    elif seconds < 31536000:
        crack_time = f"{int(seconds/86400)} days"
    elif seconds < 3153600000:
        crack_time = f"{int(seconds/31536000)} years"
    else:
        crack_time = "Centuries ✅"

    results["crack_time"] = crack_time

    # ── Final score clamp and strength label ──────────────────────────────
    score = max(0, min(100, score))
    results["score"] = score

    if score >= 80:
        results["strength"] = "Very Strong 💪"
    elif score >= 60:
        results["strength"] = "Strong ✅"
    elif score >= 40:
        results["strength"] = "Fair ⚠️"
    else:
        results["strength"] = "Weak ❌"

    results["checks"]      = checks
    results["suggestions"] = suggestions

    return results

# ── Display results ────────────────────────────────────────────────────────
def display_results(r: dict):
    """Print the analysis results in the terminal."""

    score    = r["score"]
    strength = r["strength"]

    # Score bar
    filled = int(score / 5)
    bar    = "█" * filled + "░" * (20 - filled)

    print("\n" + "═" * 55)
    print("  🔐  PASSWORD STRENGTH ANALYZER")
    print("═" * 55)
    print(f"  Password   : {'*' * len(r['password'])}")
    print(f"  Score      : {score}/100  [{bar}]")
    print(f"  Strength   : {strength}")
    print(f"  Entropy    : {r['entropy']} bits")
    print(f"  Crack Time : {r['crack_time']}")
    print("─" * 55)

    # Checks
    print("  Checks:")
    c = r["checks"]
    print(f"    {'✅' if c.get('length_8')       else '❌'}  At least 8 characters")
    print(f"    {'✅' if c.get('length_12')      else '❌'}  At least 12 characters")
    print(f"    {'✅' if c.get('has_uppercase')  else '❌'}  Contains uppercase letters")
    print(f"    {'✅' if c.get('has_lowercase')  else '❌'}  Contains lowercase letters")
    print(f"    {'✅' if c.get('has_numbers')    else '❌'}  Contains numbers")
    print(f"    {'✅' if c.get('has_special')    else '❌'}  Contains special characters")
    print(f"    {'✅' if c.get('not_common')     else '❌'}  Not a common password")
    print(f"    {'✅' if c.get('no_repeats')     else '❌'}  No repeated characters")
    print(f"    {'✅' if c.get('no_sequences')   else '❌'}  No sequential characters")
    print(f"    {'✅' if c.get('mixed_types')    else '❌'}  Uses 3+ character types")

    # Suggestions
    if r["suggestions"]:
        print("─" * 55)
        print("  💡 Suggestions:")
        for tip in r["suggestions"]:
            print(f"    → {tip}")
    else:
        print("─" * 55)
        print("  🎉 Excellent password! No suggestions.")

    print("═" * 55 + "\n")

# ── Password generator ─────────────────────────────────────────────────────
def generate_strong_password(length: int = 16) -> str:
    """Generate a cryptographically strong random password."""
    import secrets

    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}?"

    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(length))
        # Make sure it passes all checks
        if (re.search(r"[A-Z]", pwd) and
            re.search(r"[a-z]", pwd) and
            re.search(r"\d",    pwd) and
            re.search(r"[!@#$%^&*()_+\-=\[\]{}?]", pwd)):
            return pwd

# ── Main ──────────────────────────────────────────────────────────────────
def main():
    print("\n🔐  Password Strength Analyzer")
    print("Commands: type a password to analyze | 'generate' for a strong password | 'quit' to exit\n")

    while True:
        user_input = input("Enter password (hidden): ").strip()

        if user_input.lower() in ("quit", "exit", "q"):
            print("Stay safe! 👋")
            break

        if not user_input:
            print("Please enter a password.\n")
            continue

        if user_input.lower() == "generate":
            pwd = generate_strong_password(16)
            print(f"\n  ✨ Generated password: {pwd}")
            print(f"  (Copy it somewhere safe!)\n")
            result = analyze_password(pwd)
            display_results(result)
            continue

        result = analyze_password(user_input)
        display_results(result)

if __name__ == "__main__":
    main()