#find the counts
n=int(input())
temp=n
rem=0
count=0
sq=0
while temp>0:
    r=temp/10
    count+=1
    temp/=10
while n>0:
    rem=n%10
    sq+=rem**count
    n/=10
print sq
