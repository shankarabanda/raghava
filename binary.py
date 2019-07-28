arr = [None]*2
def bin(n):
    if (n<1):
        print(arr)
    else:
        #for i in range(0,k):
        #    arr[n-1]=i
         #   bin(n-1,k)
#bin(2,2)

        arr[n-1]=0
        bin(n-1)
        arr[n-1]=1
        bin(n-1)
bin(2)
