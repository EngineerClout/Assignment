# Simple Stack class implementation
class SimpleStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop from empty stack")
        return self.items.pop()

    def size(self):
        return len(self.items)

# Push all characters, pop, then compare with original
def is_palindrome(s):
    cleaned_chars = [char.lower() for char in s if char.isalnum()]
    stack = SimpleStack()
    [stack.push(char) for char in cleaned_chars] # List comprehension technique
    return all([True if stack.pop() == char else False for char in cleaned_chars]) if not stack.is_empty() else False # Binary logic for List comprehension with all in-built function



if __name__ == "__main__":
    # Test approaches
    user_input = input("Enter a word to check if it's a palindrome: ")

    print("The word is a palindrome.") if is_palindrome(user_input) else print("The word is not a palindrome.")
    # Test cases
    print("\n--- Testing with various examples ---")
    test_cases = [
        "racecar",
        "A man, a plan, a canal: Panama",
        "race a car",
        "hello",
        "Madam",
        "Was it a car or a cat I saw?",
        "12321",
        "12345"
    ]

    print("\nMethod 1 (Full-stack):")
    for test in test_cases:
        result = "palindrome" if is_palindrome(test) else "not a palindrome"
        print(f"'{test}' is {result}")