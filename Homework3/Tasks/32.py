list_of_candidates=[]
votes_list=[]
var = [ "Таракан Григорьевич",
        "Тугарин Змей",
        "Таракан Григорьевич",
        "Давыд Городецкий",
        "Давыд Городецкий",
        "Давыд Городецкий",
        "Давыд Городецкий"]

n=len(var)//2
for i in var:
    if i not in list_of_candidates:
        list_of_candidates.append(i)
candidate_1=list_of_candidates[0]
candidate_2=list_of_candidates[1]
candidate_3=list_of_candidates[2]
votes_1=var.count(candidate_1)
votes_list.append(votes_1)
votes_2=var.count(candidate_2)
votes_list.append(votes_2)
votes_3=var.count(candidate_3)
votes_list.append(votes_3)
dc=dict((zip(list_of_candidates, votes_list)))
print(list_of_candidates)
print(votes_list)
print(dc)

lider=sorted(votes_list)[-1]
second=sorted(votes_list)[-2]
if max(votes_list)>n:
    for k,v in dc.items():
        if v==lider:
            print('win',k)
elif lider==second:
    for k, v in dc.items():
        if v==lider==second:
            print('во второй тур проходит',k)
else:
    for k, v in dc.items():
        if v==lider:
            print('во второй тур проходит',k)
        if v==second:
            print('во второй тур проходит',k)




