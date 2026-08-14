# ==============================================================================
# Course: CST8279
# Assignment: Lab 9 - String Comparison
# Objective: Check whether two strings are equal using == and != operators
# ==============================================================================

# Request input strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

print("\n--- Comparison Results ---")

# Check whether the strings are equal using ==
if string1 == string2:
    print("Using '==': The strings are completely identical.")
else:
    print("Using '==': The strings are NOT identical.")

# Check whether the strings are different using !=
if string1 != string2:
    print("Using '!=': The strings are different.")
else:
    print("Using '!=': The strings are NOT different (they are equal).")