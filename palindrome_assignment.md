# Palindrome Check Using Stack and Queue (Sourced from HackerRank Day 18)

## Problem Description

A **palindrome** is a word, phrase, number, or other sequence of characters that reads the same backward as forward.  
Examples include `"madam"`, `"racecar"`, and `"level"`.

Your task is to determine whether a given string `s` is a palindrome by using both a **stack** and a **queue**.

---

## Assignment Deliverables

You are required to:

- Implement a function named `is_palindrome_using_stack`.
- The function should receive a string as input and return `True` if the string is a palindrome, or `False` otherwise.
- Use both a **stack** and a **queue** in your implementation to verify the palindrome.
- A set of test cases will be used to validate the correctness of your implementation.

---

## Function Signature

```python
def is_palindrome_using_stack(s: str) -> bool:
    pass  # Your implementation here
```

---

## How to Solve the Problem

To check if the string is a palindrome:

1. Initialize a **stack** and a **queue**.
2. For each character in the string `s`:
   - Push it onto the stack.
   - Enqueue it into the queue.
3. Pop characters from the stack and dequeue from the queue one by one.
4. Compare the popped and dequeued characters:
   - If all the characters match, then the string is a palindrome.
   - If any character does not match, then the string is not a palindrome.

---

## Constraints

- `1 <= len(s) <= 50`
- The input string `s` contains **only lowercase English letters**.

---
## Sample Output
```
For the input `"racecar"`:
```
True
```

For the input `"hello"`:

```
False
## Final Step – Push to GitHub Repository

This is an important part of the assignment.

After completing your `is_palindrome_using_stack` function, you **must** push your changes to the **GitHub Classroom repository**.

Make sure your repository contains the following files:

- `circular_dll.py`
- `palindrome.py`

You are expected to **create and commit `palindrome.py`**, and ensure that both files appear in the GitHub repository view.

See the following image of the expected visual end.

![FILE SUBMISSION OVERVIEW](https://github.com/user-attachments/assets/99c0d692-bca6-4c61-9bb9-7e762525c3e0)

Make sure your final commit has both files clearly visible before submission.
