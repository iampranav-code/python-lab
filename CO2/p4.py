def Even_Perfectsq(start,end):
    evensq=[]
    for num in range(start,end+1):
        if all(int(digit)%2==0
               for digit in str(num)):
            sqrt=int(num**0.5)
            if sqrt*sqrt==num:
                evensq.append(num)
    return evensq
start=1000
end=9999
result=Even_Perfectsq(start,end)
print(result)
