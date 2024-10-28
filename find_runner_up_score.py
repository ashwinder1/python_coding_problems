'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print  as the runner-up score.
5
Print the runner-up score.
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

# unique_arr = set(list(arr))
# max_score = max(unique_arr)
# unique_arr.remove(max_score)
# runner_up_score = max(unique_arr)

# print(runner_up_score)

runner_up_score = max_score = float('-inf')

for score in arr:
    if score > max_score:
        runner_up_score = max_score
        max_score = score
    elif score > runner_up_score and score != max_score:
        runner_up_score = score
        
print(runner_up_score)        
