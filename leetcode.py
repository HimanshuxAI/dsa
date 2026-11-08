'''


two sum #1


def two_sum1(arr,x):
    seen={}
    for i in range(len(arr)):
        seen[arr[i]]=i
    for j in range(len(arr)):
        complement=x-arr[j]
        if complement in seen and seen[complement]!=i:
            return [j,arr[complement]]
'''


'''
counting duplicate #217 

def containsduplicate(arr):
    return len(set(arr)) < len(arr)

print(containsduplicate([1,2,1]))
print(containsduplicate([1,2]))
'''



'''merge sorted array #88


def merge(nums1,m,nums2,n):
    merged=[]

    i=j=0
    while i<m and j<n:
        if nums1[i]<=nums2[j]:
            merged.append(nums1[i])
        else:
            merged.append(nums2[j])
            j+=1
    merged.extend(nums1[i:m])
    merged.extend(nums2[j:n])
    return merged
    
print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))




# merging back to nums1




def merge(nums1,m,nums2,n):
    i=m-1
    j=n-1
    k=m+n-1
    while j>=0:
        if i>=0 and nums1[i]>nums2[j]:
            nums1[k]=nums1[i]
            i-=1
        else:
            nums1[k]=nums2[j]
            j-=1
        k-=1
    return nums1

print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))

'''

'''
#maximum subarray #53

def find_max_crossing_subarray(nums,low,mid,high):
    left_sum=float('-inf')
    sum=0
    for i in range(mid,low-1,-1):
        sum+=nums[i]
        if sum>left_sum:
            left_sum=sum
            max_left=i

    right_sum=float('-inf')
    sum=0
    for j in range(mid+1,high+1):
        sum+=nums[j]
        if sum>right_sum:
            right_sum=sum
            max_right=j

    return (max_left,max_right,left_sum+right_sum)

def find_max_subarray(nums,low,high):
    if low==high:
        return (low, high, nums[low])
    else:
        mid=(low+high)//2
        left_low,left_high,left_sum=find_max_subarray(nums,low,mid)
        right_low,right_high,right_sum=find_max_subarray(nums,mid+1,high)
        cross_low,cross_high,cross_sum=find_max_crossing_subarray(nums,low,mid,high)
        if left_sum>=right_sum and left_sum>=cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>=left_sum and right_sum>=cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)
print(find_max_subarray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7],0,15))



'''


'''
#53 same with Kadane's algorithm

def maxSubArray(nums):
    best=curr=nums[0]
    for i in nums[1:]:
        curr=max(i,curr+i)
        best=max(best,curr)
    return best


print(maxSubArray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]))
'''
