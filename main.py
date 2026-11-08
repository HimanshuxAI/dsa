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

'''
def two_n_bit_add(a,b):
   n=len(a)
   c=[]*(n+1)
   carry=0
   for i in range(len(a)-1,-1,-1):
      total_sum=a[i]+b[i]+carry
      c.append(total_sum%2)
      carry = total_sum//2
   c.append(carry)
   return print(c[::-1])



two_n_bit_add([1, 0, 0],[1, 1, 1])'''


'''

def selection_sort(a):
   for i in range(len(a)-1):
      min_index=i
      for j in range(i+1,len(a)):
         if a[min_index]>a[j]:
            min_index=j
      if i != min_index:
        a[i],a[min_index]=a[min_index],a[i]

   print(a)

selection_sort([31,41,59,26,41,58])'''

'''

def merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    left=[0]*(n1+1)
    right=[0]*(n2+1)

    for i in range(n1):
        left[i]=A[p+i]
    for j in range(n2):
        right[j]=A[q+1+j]

    left[n1]=float("inf")
    right[n2]=float("inf")

    i=j=0

    for k in range(p,r+1):
        if left[i]<=right[j]:
            A[k]=left[i]
            i+=1
        else:
            A[k]=right[j]   
            j+=1
        k+=1
def merge_sort(A,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
    return A


num=[31,41,59,26,41,58]
print(merge_sort(num,0,len(num)-1))'''



'''
#without sentinels 

def merge_sort(A):
   if len(A)<=1:
      return A
   q=(len(A))//2

   left=A[:q]
   right=A[q:]

   merge_sort(left)
   merge_sort(right)

   i = j = k = 0 


   while i < len(left) and j < len(right):
      if left[i] <= right[j]:
         A[k]=left[i]
         i+=1
      else: 
         A[k]=right[j]
         j+=1
      k+=1
   while i < len(left):
      A[k]=left[i]
      i+=1
      k+=1
   while j < len(right):
      A[k]=right[j]
      j+=1
      k+=1


   print(A)


merge_sort([32,41,23,5,6,2,1])
'''


def merge_sort(a):
   if len(a)>1:
      mid = len(a)//2
      left = a[:mid]
      right=a[mid:]

      merge_sort(left)
      merge_sort(right)

      i = j = k = 0

      while i < len(left) and j < len(right):
         if left[i]<=right[j]:
            a[k]=left[i]
            i+=1
         else:
            a[k]=right[j]
            j+=1
         k+=1
      while i < len(left):
         a[k]=left[i]
         i+=1
         k+=1
      while j < len(right):
               a[k]=right[j]
               j+=1
               k+=1
   return print(a)

         
merge_sort([32,41,23,5,6,2,1])

