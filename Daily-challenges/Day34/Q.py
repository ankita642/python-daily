'''write a program in python to check if a given string reads 
the same forward and backward'''

def is_palindrome(text):
    # Remove spaces and convert to lowercase for accurate checking
    cleaned_text = "".join(text.split()).lower()
    
    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]

# Example usage
test_string = "A nut for a jar of a tuna"

if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome!")
else:
    print(f"'{test_string}' is not a palindrome.")
