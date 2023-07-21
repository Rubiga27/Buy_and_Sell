def max_price(A):
    max=float('-inf')
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            rem=A[j]-A[i]
            if rem>0 and rem>max:
                max=rem
    return max

A=list(map(int,input().split()))
print(max_price(A))

