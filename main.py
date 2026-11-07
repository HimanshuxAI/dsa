'''def insertion(a):
    for i in range(1,len(a)):
       key = a[i]
       j=i-1
       while j>=0 and a[j]>key:
          a[j+1]=a[j]
          j-=1
       a[j+1]=key
    print(a)


insertion([31,41,59,26,41,58])'''


'''

def insertion_sort_decreasing(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key>a[j]:
          a[j+1]=a[j]
          j-=1
        a[j+1]=key
    print(a)

insertion_sort_decreasing([31,41,59,26,41,58])

   '''
'''

def linear_search(arr,target): 
    for i in range(len(arr)):
         if arr[i]==target:
             return print(i)
    return print("not found")

linear_search([31,41,59,26,41,58],26)
linear_search([31,41,59,26,41,58],0)
'''