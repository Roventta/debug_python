def raiseScoresBy5(arr):
    for s in arr:
        s+=1

scores = [80,90,100]

# Program starts here
print("origin scores: ", scores)
raiseScoresBy5(scores);
print("post scores: ", scores)