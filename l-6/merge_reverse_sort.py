array=[4,8,100,13,1,45]

def merge(array):
    if len(array)>1:
        m=len(array)//2
        l= array[:m]
        r= array[m:]
        merge(l)
        merge(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]>r[j]:
                array[k]=l[i]
                i=i+1
            else:
                array[k]=r[j]
                j=j+1
            k=k+1
        #picking up the reamining elements and putting them into the list
        while i<len(l):
            array[k]=l[i]
            i=i+1
            k=k+1
        while j<len(r):
            array[k]=r[j]
            j=j+1
            k=k+1

def output(array):
    for n in range(len(array)):
        print(array[n],end=" ")

merge(array)
output(array)
    