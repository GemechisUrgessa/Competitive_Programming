def countSwaps(a):
    temp =0
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                temp+=1
    print(f"Array is sorted in {temp} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")