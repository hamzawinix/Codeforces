data = input().split()
n = int(data[0])
k= int(data[1])
adv = 0
scores = input()
scores = scores.split(" ")

for score in scores :
    if int(score) > 0:
        if int(score) >= int(scores[k-1]):
            adv = adv+1
        else:
            continue

print(adv)


 
    