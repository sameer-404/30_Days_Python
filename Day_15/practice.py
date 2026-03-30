#Python Error Types:
# ============================================================
# PYTHON ERRORS - QUICK REFERENCE
# ============================================================

# ── 1. SyntaxError ──────────────────────────────────────────
# Happens before code runs — bad structure
# if x > 5       ← missing colon, Python won't even start
if True:
    pass  # correct


# ── 2. IndentationError ─────────────────────────────────────
# Wrong or missing indentation
def greet():
    print("hello")  # must be indented


# ── 3. NameError ────────────────────────────────────────────
# Variable used before being defined
try:
    print(some_variable)  # not defined
except NameError as e:
    print(f"NameError: {e}")


# ── 4. IndexError ───────────────────────────────────────────
# List index out of range (remember: starts at 0)
try:
    fruits = ["apple", "banana"]
    print(fruits[5])  # only 0 and 1 exist
except IndexError as e:
    print(f"IndexError: {e}")


# ── 5. KeyError ─────────────────────────────────────────────
# Dictionary key doesn't exist
try:
    person = {"name": "Alice"}
    print(person["email"])  # no email key
except KeyError as e:
    print(f"KeyError: {e}")

# Safe way — use .get()
print(person.get("email", "not found"))  # returns default


# ── 6. TypeError ────────────────────────────────────────────
# Wrong data type in an operation
try:
    result = "Age: " + 25  # can't add str and int
except TypeError as e:
    print(f"TypeError: {e}")

# Fix: convert first
result = "Age: " + str(25)


# ── 7. ValueError ───────────────────────────────────────────
# Right type, but bad value
try:
    number = int("abc")  # "abc" can't become an int
except ValueError as e:
    print(f"ValueError: {e}")

# Safe way
value = "abc"
if value.isdigit():
    number = int(value)
else:
    print("Not a valid number")


# ── 8. AttributeError ───────────────────────────────────────
# Method or attribute doesn't exist on object
try:
    name = "alice"
    name.push("bob")  # strings don't have .push()
except AttributeError as e:
    print(f"AttributeError: {e}")

# Tip: check available methods with dir()
# print(dir(name))


# ── 9. ImportError ──────────────────────────────────────────
# Module found but the name inside it doesn't exist
try:
    from math import square_root  # doesn't exist
except ImportError as e:
    print(f"ImportError: {e}")

from math import sqrt  # correct


# ── 10. ModuleNotFoundError ─────────────────────────────────
# Module not installed or doesn't exist
try:
    import some_fake_module
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}")
# Fix: pip install module-name


# ============================================================
# GOLDEN RULE — wrap risky code always
# ============================================================
def safe_convert(value):
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        print(f"Conversion failed: {e}")
        return None

print(safe_convert("42"))   # 42
print(safe_convert("abc"))  # None