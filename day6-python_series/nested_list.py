records=[]
name_list=[]
score_list=[]
n=int(input())
for i in range (n):
    name=input()
    score=float(input())
    records.append([name,score])
    name_list.append(name)
    score_list.append(score)

score_list=list(set(score_list))
score_list.sort()
lowest_score=score_list[1]
output=[j[0] for j in records if j[1]==lowest_score]
output.sort()
for i in output:
    print(i)