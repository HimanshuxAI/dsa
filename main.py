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
'''
'''
def binary_search(x,v):
    left=0
    right=len(x)-1
    while left<=right:
        mid = (left+right)//2
        if x[mid]==v:
            return print(mid)
        elif x[mid]>v:
            right=mid-1
        elif x[mid]<v:
            left=mid+1
        else:
            return(print("not found"))

        
binary_search([1,2,3,5,6,7],3)
binary_search([1,2,3,5,6,7],6)
''''''

def two_sum(a,x):
    seen={}
    for i in range(len(a)):
        seen[a[i]]=i
    for j in range(len(a)):
        rest=x-a[j]
        if rest in seen and seen[rest] != j:
            return [j,seen[rest]]
print(two_sum([4, 1, 2], 8))'''
'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
'''

'''
def horners_rule(x,a):
    y=0
    for c in a:
        y=c+x*y
    return y

print(horners_rule(2,[1,2,3,4]))'''
'''

def inversion_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, left_inv = inversion_count(arr[:mid])
    right_half, right_inv = inversion_count(arr[mid:])
    
    sorted_arr, merge_inv = merge_and_count(left_half, right_half)
    
    return sorted_arr, left_inv + right_inv + merge_inv

def merge_and_count(left, right):
    i = j = 0
    merged = []
    inv_count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count

arr = [2, 4, 1, 3, 5]
sorted_arr, total_inversions = inversion_count(arr)
print(sorted_arr)
print(total_inversions)  
'''

'''
def inversion_count_small(x):
    inversion=0
    n=len(x)
    for i in range(n):
        for j in range(i+1,n):
            if x[i]>x[j]:
                inversion+=1
    return inversion

print(inversion_count_small([2, 4, 1, 3, 5]))'''





'''

#find maximum crossing subarray 

def find_max_crossing_subarray(A,low,mid,high):
    left_sum=float('-inf')
    sum=0 
    for i in range(mid,low-1,-1):
        sum+=A[i]
        if sum>left_sum:
            left_sum=sum
            max_left=i
    right_sum=float('-inf')
    sum=0
    for j in range(mid+1,high+1):
        sum+=A[j]
        if sum>right_sum:
            right_sum=sum
            max_right=j
    return (max_left,max_right,left_sum+right_sum)


def find_maximum_subarray(A,low,high):
    if high==low:
        return (low,high,A[low])
    else:
        mid = (low+high)//2
        left_low,left_high,left_sum=find_maximum_subarray(A,low,mid)
        right_low,right_high,right_sum=find_maximum_subarray(A,mid+1,high)
        cross_low,cross_high,cross_sum=find_max_crossing_subarray(A,low,mid,high)
        if left_sum>=right_sum and left_sum>=cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>=left_sum and right_sum>=cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)
            
print(find_maximum_subarray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7],0,15))



'''



'''
# brute force in finding the maximum sum in subarray
'''

def brute_fr(num):
    max_sum=float('-inf')
    for i in range(len(num)):
        current=0
        for j in range(i,len(num)):
            current+=num[j]
            max_sum=max(current,max_sum)
    return max_sum

print(brute_fr([-2, 1, -3, 4, -1, 1, -5, 4]))