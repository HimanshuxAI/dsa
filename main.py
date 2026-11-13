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

def brute_fr(num):
    max_sum=float('-inf')
    for i in range(len(num)):
        current=0
        for j in range(i,len(num)):
            current+=num[j]
            max_sum=max(current,max_sum)
    return max_sum

print(brute_fr([-2, 1, -3, 4, -1, 1, -5, 4]))
'''


'''
#divide and conquer method


def maximum_crossing_subarray(nums,low,mid,high):
    left_sum=float('-inf')
    sum=0
    for i in range(mid,low-1,-1):
        sum+=nums[i]
        if sum>left_sum:
            left_sum=sum
            max_left=i
    right_sum=float('-inf')
    sum=0
    for i in range(mid+1,high+1):
        sum+=nums[i]
        if sum>right_sum:
            right_sum=sum
            max_right=i
    return (max_left,max_right,left_sum+right_sum)




def maximum_subarray(nums,low,high):
    if low==high:
        return (low,high,nums[low])
    else:
        mid = (low+high)//2
        left_low,left_high,left_sum=maximum_subarray(nums,low,mid)
        right_low,right_high,right_sum=maximum_subarray(nums,mid+1,high)
        cross_low,cross_high,cross_sum=maximum_crossing_subarray(nums,low,mid,high)
        if left_sum>right_sum and left_sum>cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>left_sum and right_sum>cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)

print(maximum_subarray([-2, -1, -3, -4, -1, -1, -5, -4],0,len([-2, -1, -3, -4, -1, -1, -5, -4])-1))

'''

'''
non recursive and linear time algo method:

def lin(num):
    max_sum=float('-inf')
    current=0
    for i in range(len(num)):
        current=max(num[i],current+num[i])
        max_sum=max(current,max_sum)
    return max_sum

print(lin([-2, -1, -3, -4, -1, -1, -5, -4]))
'''

'''
now same "non recursive and linear time algo method:" with tracking the low and high 

def lingo(nums):
    max_sum=float('-inf')
    current=0
    low=0
    high=0
    temp_start=0

    for i,num in enumerate(nums):
        if num>current+num:
            current=num;temp_start=i
        else: current=current+num
        if current>max_sum:
            max_sum=current
            low=temp_start
            high=i
    return (low,high,max_sum)
print(lingo([-2, 1, -3, 4, -1, 1, -5, 4]))
'''

'''
# matrix multipl o n 3
def mult(a,b):
    n=len(a)
    c=[[0.0 for col in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j]+=a[i][k]*b[k][j]

    return c
A = [[1, 2], [3, 4]]

B = [[5, 6],[7, 8]]

print(mult(A,B))
'''


'''
#square multiple matrix by recursive calling


def add_matrix(a,b):
    n=len(a)
    return [[a[i][j]+b[i][j] for i in range(n)]for j in range(n)]

def split_matrix(m):
    mid=len(m)//2
    a11=[row[:mid] for row in m[:mid]]
    a12=[row[:mid] for row in m[mid:]]
    a22=[row[mid:] for row in m[mid:]]
    a21=[row[mid:] for row in m[:mid]]
    return a11,a12,a21,a22

def square_multiply_matrix_recurisvely(a,b):
    n=len(a)
    if n==1:
        return [a[0][0]*b[0][0]]
    a11,a12,a21,a22=split_matrix(a)
    b11,b12,b21,b22=split_matrix(b)

    c11=add_matrix(square_multiply_matrix_recurisvely(a11,b11),square_multiply_matrix_recurisvely(a12,b21))
    c12=add_matrix(square_multiply_matrix_recurisvely(a11,b12),square_multiply_matrix_recurisvely(a12,b22))
    c21=add_matrix(square_multiply_matrix_recurisvely(a21,b11),square_multiply_matrix_recurisvely(a21,b21))
    c22=add_matrix(square_multiply_matrix_recurisvely(a21,b12),square_multiply_matrix_recurisvely(a21,b22))

    c=[]
    for i in range(len(c11)):
        c.append(c11[i] + c12[i])
    for i in range(len(c21)):
        c.append(c21[i]+ c22[i])
    return c

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(square_multiply_matrix_recurisvely(A, B))
    
'''


''' 
#strassen algorithm:  when n is an exact power of 2

def add(a, b):
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]

def sub(a, b):
    n = len(a)
    return [[a[i][j] - b[i][j] for j in range(n)] for i in range(n)]

def split_matrices(a, b):
    n = len(a)
    mid = n // 2
    a11 = [i[:mid] for i in a[:mid]]
    a12 = [i[mid:] for i in a[:mid]]
    a21 = [i[:mid] for i in a[mid:]]
    a22 = [i[mid:] for i in a[mid:]]

    b11 = [i[:mid] for i in b[:mid]]
    b12 = [i[mid:] for i in b[:mid]]
    b21 = [i[:mid] for i in b[mid:]]
    b22 = [i[mid:] for i in b[mid:]]

    return (a11, a12, a21, a22, b11, b12, b21, b22)


def strassen(a, b):
    if len(a) == 1:
        return [[a[0][0] * b[0][0]]]

    a11, a12, a21, a22, b11, b12, b21, b22 = split_matrices(a, b)

    c11 = add(sub(add(strassen(add(a11, a22), add(b11, b22)),strassen(a22, sub(b21, b11))),strassen(add(a11, a12), b22)),strassen(sub(a12, a22), add(b21, b22)))

    c12 = add(strassen(a11, sub(b12, b22)),strassen(add(a11, a12), b22))

    c21 = add(strassen(add(a21, a22), b11),strassen(a22, sub(b21, b11)))

    c22 = add(add( sub(strassen(add(a11, a22), add(b11, b22)), strassen(add(a21, a22), b11)),strassen(a11, sub(b12, b22))),strassen(sub(a21, a11), add(b11, b12)))

    top = [r1 + r2 for r1, r2 in zip(c11, c12)]
    bottom = [r1 + r2 for r1, r2 in zip(c21, c22)]
    return top + bottom


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(strassen(A, B)) 


'''

import numpy as np


def strassen(a, b, threshold=1):
  a = np.asarray(a)
  b = np.asarray(b)
  n = a.shape[0]

  if n <= threshold:
    return np.matmul(a, b)

  is_padded = False
  if n % 2 != 0:
    a = np.pad(a, ((0, 1), (0, 1)), mode="constant", constant_values=0)
    b = np.pad(b, ((0, 1), (0, 1)), mode="constant", constant_values=0)
    n += 1
    is_padded = True

  half = n // 2
  a11, a12 = a[:half, :half], a[:half, half:]
  a21, a22 = a[half:, :half], a[half:, half:]
  b11, b12 = b[:half, :half], b[:half, half:]
  b21, b22 = b[half:, :half], b[half:, half:]

  m1 = strassen(a11 + a22, b11 + b22, threshold)
  m2 = strassen(a21 + a22, b11, threshold)
  m3 = strassen(a11, b12 - b22, threshold)
  m4 = strassen(a22, b21 - b11, threshold)
  m5 = strassen(a11 + a12, b22, threshold)
  m6 = strassen(a21 - a11, b11 + b12, threshold)
  m7 = strassen(a12 - a22, b21 + b22, threshold)

  c11 = m1 + m4 - m5 + m7
  c12 = m3 + m5
  c21 = m2 + m4
  c22 = m1 - m2 + m3 + m6

  top = np.hstack((c11, c12))
  bottom = np.hstack((c21, c22))
  c = np.vstack((top, bottom))

  if is_padded:
    return c[:-1, :-1]
  return c


print(strassen([[1, 2], [3, 4]], [[5, 6], [7, 8]], threshold=1))
