''' Take a fixed list of scores: scores = [88, 92, 79, 95, 85].
Write a single for loop that calculates both the total sum and 
the average of the list elements, then prints them with clear
labels.'''

scores = [88, 92, 79, 95, 85]
total_sum = 0
for score in scores:
    total_sum += score
    average = total_sum/len(scores)
    print(total_sum)
    print(average)
    