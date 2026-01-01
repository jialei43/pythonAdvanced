"""
快速排序是一种分治法，选择一个基准元素（pivot），将数组分成两部分，一部分所有元素比基准元素小，另一部分所有元素比基准元素大，然后递归排序这两部分。
时间复杂度：
最坏时间复杂度：O(n**2)(当选取的基准值是最小或最大元素时)
最好/平均时间复杂度：O(nlogn)
空间复杂度：O(logn)
"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 选择基准元素
    left = [x for x in arr if x < pivot]  # 小于基准的元素
    middle = [x for x in arr if x == pivot]  # 等于基准的元素
    right = [x for x in arr if x > pivot]  # 大于基准的元素
    return quick_sort(left) + middle + quick_sort(right)

# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
print("排序前:", arr)
sorted_arr = quick_sort(arr)
print("排序后:", sorted_arr)
