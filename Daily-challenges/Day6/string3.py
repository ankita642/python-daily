#Uses a dictionary to count how many times each character appears
text = "apple"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq) 