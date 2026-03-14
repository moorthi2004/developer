data={}
for _ in range(int(input())):
    name=input()
    score=int(input())
    data[name]=score 
print(pop(max(data)))    