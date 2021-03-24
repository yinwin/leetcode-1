rating=[2,5,3,4,1]
l=[]
m=0
n=0
a=0
b=0
       
for i in range(1,len(rating)-1):
    for j in range(i):
        for k in range(i+1,len(rating)):
        
            if rating[j]<rating[i] and rating[k]>rating[i]:
            m+=1
            

           
        #else:
            a+=1
    for k in range(i+1,len(rating)):
        if rating[k]>rating[i]:
            n+=1
        #else:
            b+=1

print(m,n)
