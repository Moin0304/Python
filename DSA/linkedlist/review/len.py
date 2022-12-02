l=[1,2,3,4,5,6,7]
i=0
count=0
while True:
    try:
        val=l[i]
        i+=1
        count+=1
    except:
        break
print(count)
print(i)