class Member:
    def __init__(self, name, contribution):
        self.name=name
        self.contribution=contribution
    def get_name(self):
        return self.name
    def get_contribution(self):
        return  self.contribution

names_list=[]
contributions_list=[]
count_of_members=int(input('Введите количество участников:'))
for i in range(1, count_of_members+1):
    Mem=Member(input('Введите имя:'), float(input('Введите взнос:')))
    names_list.append(Mem.name)
    contributions_list.append(Mem.contribution)

dic_members=dict(zip(names_list, contributions_list))
print(dic_members)

contribution_from_other=float(sum(contributions_list))/count_of_members

for k,v in dic_members.items():
    diff=abs(v-contribution_from_other)
    if v<contribution_from_other:
        if v>

