class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        u1 = n1
        l1 = 0
        u2 = n2
        l2 = 0

        i = (u1 + l1) // 2
        j = (u2 + l2) // 2
        count = 0

        while nums1[i] != nums2[j] and count < n1+n2:
            i = (u1 + l1) // 2
            j = (u2 + l2) // 2
            if nums1[i] < nums2[j]:
                l1 = i
                u2 = j
            elif nums1[i] > nums2[j]:
                u1 = i
                l2 = j
            count += 1


        if (n1 + n2) % 2 == 0:
            return (nums1[i] + nums2[j]) / 2
        else:
            return nums1[i]