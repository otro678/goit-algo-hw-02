from collections import deque

def is_palindrome(s: str) -> bool:
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    char_deque = deque(cleaned_string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

input_string = "Я несу гусеня"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
