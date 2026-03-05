age = [22, 19, 24, 25, 26, 24, 25, 24]
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
len_list = len(age)
age = set(age)
print(age)
len_set = len(age)
print(f"The length of list: {len_list} and length of set: {len_set}")

#Explain the difference between the following data types: string, list, tuple and set


# ============================================================
# Python Data Types: String, List, Tuple and Set
# ============================================================


# ── 1. STRING ───────────────────────────────────────────────
# - Ordered sequence of characters
# - Immutable: cannot be changed after creation
# - Allows duplicate characters
# - Supports indexing and slicing
# - Defined with " " or ' '
# - Best used for: storing and manipulating text


# ── 2. LIST ─────────────────────────────────────────────────
# - Ordered sequence of any data type
# - Mutable: elements can be added, removed, or changed
# - Allows duplicate values
# - Supports indexing and slicing
# - Defined with [ ]
# - Best used for: collections of items that may need to change


# ── 3. TUPLE ────────────────────────────────────────────────
# - Ordered sequence of any data type
# - Immutable: cannot be changed after creation
# - Allows duplicate values
# - Supports indexing and slicing
# - Defined with ( )
# - Best used for: fixed data that should not change (e.g. coordinates, RGB values)


# ── 4. SET ──────────────────────────────────────────────────
# - Unordered collection of any data type
# - Mutable: elements can be added or removed
# - Does NOT allow duplicates (automatically removes them)
# - Does NOT support indexing (no order)
# - Defined with { }
# - Best used for: storing unique values and performing set operations (union, intersection)


# ── COMPARISON SUMMARY ──────────────────────────────────────
# Feature       String      List        Tuple       Set
# ---------------------------------------------------------
# Ordered       Yes         Yes         Yes         No
# Mutable       No          Yes         No          Yes
# Duplicates    Yes         Yes         Yes         No
# Indexing      Yes         Yes         Yes         No
# Syntax        " "         [ ]         ( )         { }