n=int(input())
if n==0 or n==1:
    print "1"
else:
    fact=1
    for i in range (1,n+1):
        fact=fact*i
        i+=1
    print fact   
    
    
    
    
