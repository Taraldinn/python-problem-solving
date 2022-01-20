d = {}
for i in range(int(input())):
        name = input()        
        score = float(input())        
        d.update({name:score})
        
print(d)
s = sorted(d.items(),key=lambda x:x[1])
print(s)

        
        