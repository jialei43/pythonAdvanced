"""
堆排序 (Heap Sort)

原理：
堆排序基于堆这一数据结构，首先将数组构建成最大堆（或最小堆），然后反复将堆顶元素移除，并重新调整堆。

时间复杂度：

最坏/平均/最好时间复杂度：O(nlogn)

空间复杂度：O(1)

"""

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):  # 建立最大堆
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 将堆顶元素与最后一个元素交换
        heapify(arr, i, 0)
    return arr

# 示例
arr = [12, 11, 13, 5, 6, 7]
print("排序前:", arr)
sorted_arr = heap_sort(arr)
print("排序后:", sorted_arr)
