#find the sum of square
n=int(input())
rem=0
sq=0
while(n>0):
    rem=n%10
    sq+=rem*rem
    n/=10
print sq
