def are_brackets_balanced(string):
    open_paren = open_brace = open_bracket = 0

    for char in string:
        if char == '(':
            open_paren += 1
        elif char == ')':
            open_paren -= 1
        elif char == '{':
            open_brace += 1
        elif char == '}':
            open_brace -= 1
        elif char == '[':
            open_bracket += 1
        elif char == ']':
            open_bracket -= 1

        # If count goes negative, brackets are unbalanced
        if open_paren < 0 or open_brace < 0 or open_bracket < 0:
            return False

    # Check if all brackets are balanced
    return open_paren == open_brace == open_bracket == 0

# Test cases
print(are_brackets_balanced("))))(((("))  # Output: True
print(are_brackets_balanced(")))))){[(])}"))    # Output: False
print(are_brackets_balanced(")))({[({})]})"))  # Output: True
