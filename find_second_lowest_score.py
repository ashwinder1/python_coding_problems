#Print the name(s) of any student(s) having the second lowest grade in. 
#If there are multiple students, order their names alphabetically and print each one on a new line.

# There are 5 students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, 
# so we order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    students = []
    # Step 1: Read input data
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

# Solution #1 --> O(nlogn)

# # Sort the students list
# # by the score in ascending order
# students.sort(key=lambda x: x[1])

# # Find the second lowest score
# second_lowest = sorted(set([score for name, score in students]))[1]

# # Print the name of students with the second lowest score
# for name, score in students:
#     if score == second_lowest:
#         print(name)

# Solution #2 --> O(nlogn)
# Step 2: Find the second lowest score
lowest_score = float('inf')
second_lowest = float('inf')

for name, score in students:
    if score < lowest_score:
        second_lowest = lowest_score
        lowest_score = score
    if score < second_lowest and score != lowest_score:
        second_lowest = score
        
# Step 3: Collect names of students with the second lowest score
second_lowest_names = [name for name, score in students if score == second_lowest]

# Step 4: Sort the names in alphabetical order
second_lowest_names.sort()

for name in second_lowest_names:
    print(name)
    
# # Solution #3 --> O(nlogn)

# # Step 2: find the second lowest score

# scores = {score for name, score in students} # Create a set of unique scores

# sorted_scores = sorted(scores) # Sort the unique scores

# second_lowest = sorted_scores[1] # The second lowest score


# # Print the names of students with the second lowest score
# for name, score in sorted(students, key=lambda x: x[0]):  # Sort names alphabetically
#     if score == second_lowest:
#         print(name)
