#nums = [2,3,1]
nums = [2,3,1,5,4]

a= max(nums)
b=min(nums)
i=nums.index(a)

j=nums.index(b)
if abs(i-j)==1:
    b=min(nums)



