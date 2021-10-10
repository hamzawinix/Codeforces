def voter(votes):
    votes_count = 0
    for vote in votes:
        if vote == "1":
            votes_count = votes_count + 1
        elif vote == " ":
            continue
    if votes_count > 1 :
        return 1
    else:
        return 0
prob_num = int(input())
solvable =0
for prob in range(prob_num):
    solvable = solvable + voter(str(input()))
print (solvable) 
