def is_palindrome_using_stack(input_string):
    # Create an empty stack (list)
    stack = []

    # Push all characters onto the stack
    for char in input_string:
        stack.append(char)

    # Pop characters to build the reversed string
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()  # Pop from stack and append to reversed_string

    # Compare original and reversed strings
    return input_string == reversed_string


# Example usage:
test_str = "racecar"
print(f"Is '{test_str}' a palindrome? {is_palindrome_using_stack(test_str)}")  # True

test_str2 = "hello"
print(f"Is '{test_str2}' a palindrome? {is_palindrome_using_stack(test_str2)}")  # False

# 3. A man, a plan, a canal, Panama!
# (Arguably the most famous one. A tribute to the construction of the Panama Canal.)

# 4. Doc, note I dissent. A fast never prevents a fatness. I diet on cod."
# (A rebellious eater's palindrome.)

# 5. "Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man — a prisoner up to new era."
# (Dark, poetic, and surprisingly coherent.)

# "Was it a car or a cat I saw?"
#
# "Go hang a salami, I’m a lasagna hog."
# (Truly a pasta-lover’s eternal dilemma.)

# "Evil is a name of a foeman as I live."
