def encode(arr):
    out =""
    count = 1
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            count += 1
        else:
            out+=arr[i]+str(count)
            count = 1
    i = len(arr)-1
    out+=arr[i]+str(count)
    return out

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
