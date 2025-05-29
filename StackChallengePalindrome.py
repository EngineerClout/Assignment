def is_palindrome_using_stack(input_string):
    """
    Check if the input string is a palindrome using a stack.
    This version ignores spaces, commas, and capitalization.
    """

    # Step 1: Normalize the input
    # Remove spaces and punctuation, and make all letters lowercase
    cleaned = ""
    for char in input_string:
        if char.isalnum():  # Keep only letters and numbers
            cleaned += char.lower()

    # Step 2: Use a stack to reverse the cleaned string
    stack = []
    for char in cleaned:
        stack.append(char)  # Push each character

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()  # Pop and build reversed string

    # Step 3: Compare cleaned original and reversed
    print(f"Original cleaned string: {cleaned}")
    print(f"Reversed string:        {reversed_string}\n")

    return cleaned == reversed_string



# Example usage:
# test_str = "racecar"
# print(f"Is '{test_str}' a palindrome? {is_palindrome_using_stack(test_str)}")  # True

# test_str2 = "hello"
# print(f"Is '{test_str2}' a palindrome? {is_palindrome_using_stack(test_str2)}")  # False

# 3. A man, a plan, a canal, Panama!
# (Arguably the most famous one. A tribute to the construction of the Panama Canal.)

# test_str3 = "A man, a plan, a canal, Panama"
# print(f"\n Is '{test_str3}' a palindrome? {is_palindrome_using_stack(test_str3)}")
# 4. Doc, note I dissent. A fast never prevents a fatness. I diet on cod."
# (A rebellious eater's palindrome.)

# test_str4 = "Doc, note I dissent. A fast never prevents a fatness. I diet on cod."
# print(f"\n Is '{test_str4}' a palindrome? {is_palindrome_using_stack(test_str4)}")


# (Dark, poetic, and surprisingly coherent.)
# 5. "Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man — a prisoner up to new era."

# test_str5 = "Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man — a prisoner up to new era"
# print(f"\n Is '{test_str5}' a palindrome? {is_palindrome_using_stack(test_str5)}")

# "Was it a car or a cat I saw?"
#
# "Go hang a salami, I’m a lasagna hog."
# (Truly a pasta-lover’s eternal dilemma.)

# "Evil is a name of a foeman as I live."
