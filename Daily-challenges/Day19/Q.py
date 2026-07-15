class Student:
    def __init__(self, name, scores=None):
        self.name = name
        # Initialize with an empty list if no scores are provided
        if scores is None:
            self.scores = []
        else:
            self.scores = scores

    def add_score(self, score):
        self.scores.append(score)

    def get_average(self):
        # Prevent division by zero if the student has no scores yet
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

# --- Verification Test ---
# 1. Create a student with initial scores
student1 = Student("Alex", [85, 90, 78])

# 2. Add a new score
student1.add_score(92)

# 3. Calculate and display the average
print(f"Student: {student1.name}")
print(f"All Scores: {student1.scores}")
print(f"Average Score: {student1.get_average():.2f}")
