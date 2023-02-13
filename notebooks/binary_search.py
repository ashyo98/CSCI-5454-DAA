#!/usr/bin/python3

A=[1,5,10,12,15,16,18,45]
x=37

n=len(A)
l,u=0,n-1
a=-1
while l<u-1:
    m=(l+u)//2
    if not (A[l] <= x and x < A[u]):
        print(f"Invariant fails at start of loop for l={l} and u={u}")
    if A[m] == x:
        print(m)
        break
    elif A[m] < x:
        l=m
        a=l
    else:
        u=m
    if not (A[l] <= x and x < A[u]):
        print(f"Invariant fails at end of loop for l={l} and u={u}")

print(f"index at {l} with value {A[l]}")
    
