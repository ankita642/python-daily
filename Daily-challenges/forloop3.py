'''Write a program that iterates through numbers from 1 to 20. If a
number is divisible by 5, skip it entirely using continue. Print
all other numbers.'''

for i in range(1, 21):
    if i % 5 == 0:
      continue
    print(i, end=" ")



