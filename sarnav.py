n=input()
l=[]
s=""
for i in range(len(n)-1,-1,-1):
    l.append(n[i])
for i in l:
    s+=i
print(s)