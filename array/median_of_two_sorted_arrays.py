"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    sorted_array = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            sorted_array.append(nums1[i])
            i += 1
        else:
            sorted_array.append(nums2[j])
            j += 1

    sorted_array.extend(nums1[i:])
    sorted_array.extend(nums2[j:])

    item_count = len(sorted_array)

    if item_count % 2 == 0:  # even
        position = (item_count // 2 ) - 1
        return (sorted_array[position] + sorted_array[position + 1]) / 2
    else:
        position = (item_count) // 2
        return sorted_array[position]


median = findMedianSortedArrays(nums1=[1, 3], nums2=[2])
print(median)
median = findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4])
print(median)
