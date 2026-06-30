text = "Hello World"
vowels = "aeiouAEIOU"
v_count = sum(1 for char in text if char in vowels)
print(f"Vowels: {v_count}") 