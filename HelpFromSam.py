def HelpFromSam(target):
    currentScore=0
    count=0
    if target>=1:
        count+=1
        currentScore+=1
    while (currentScore*2)<=target:
        currentScore*=2

    return count+(target-currentScore)

target=int(input())
print(HelpFromSam(target))
