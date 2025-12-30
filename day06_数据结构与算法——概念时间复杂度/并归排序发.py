"""
5. 归并排序 (Merge Sort)

原理：
归并排序是另一种分治法，通过将数组分成两部分，递归排序后合并成有序数组。

时间复杂度：

最坏/平均/最好时间复杂度：O(nlogn)
空间复杂度：O(n)
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # 左部分排序
    right = merge_sort(arr[mid:])  # 右部分排序
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 示例
arr = [38, 27, 43, 3, 9, 82, 10]
print("排序前:", arr)
sorted_arr = merge_sort(arr)
print("排序后:", sorted_arr)

