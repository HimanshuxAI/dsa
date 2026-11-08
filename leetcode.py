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

print(len([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]))