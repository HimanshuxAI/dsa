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