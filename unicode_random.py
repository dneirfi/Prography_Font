import random

f= open("C:/Users/dneir/PycharmProjects/Prography_Font/zi2zi/unicode/unicode_list.txt","r")
lines = f.readlines()
u=[]
i=0
while i<200:
    r=random.randrange(0,2496)
    val=lines[r]
    u.append(val)
    i=i+1


fw=open('unicode200.txt','w')


fw.writelines(u)