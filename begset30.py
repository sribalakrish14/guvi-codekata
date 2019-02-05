h,m=map(int,raw_input().split())
h1,m1=map(int,raw_input().split())
min=(h*60)+m
min1=(h1*60)+m1
s=abs(min-min1)
print s/60,s%60
