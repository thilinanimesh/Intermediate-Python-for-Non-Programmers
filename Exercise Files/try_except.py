print("Before Exception")

class HumanError(Exception):
    pass

def to_lowercase(word):
    if word is None:
        raise HumanError("This is not a valid entry, please enter a word and do not keep this entry BLANK")
    else:
        return word.lower()

try:
    print("Before")

    print(to_lowercase(None))

except HumanError as e:
    print (e)

print("After")


# Python code​​​​​​‌‌‌​‌‌​​‌​‌​‌​‌​​​‌‌‌​​​‌ below
# Use print("messages...") to debug your solution.

#
# Code challange......................
# Write a method to get a student's average score
# You're given a "Student" class with a "scores" property that is a list of scores from tests they have taken.
# Your task: Create a method named "average_score" that returns the average of all their scores 
# (you can do that by adding all the scores together and dividing by the numbers of scores they have.
#

show_expected_result = False

class Student:
    scores = [65,75,85,95]

    def average_score(self):
        total = 0  
        for s in self.scores:
            total += s
        return total/(len(self.scores))

student = Student()
result = student.average_score()
print(result)