"""
选择排序 (Selection Sort)

原理：
选择排序通过反复选择未排序部分的最小元素，并将其放到已排序部分的末尾。
通俗讲就是从前往后，每个元素逐个与其后的元素进行比较，最后最小的值被放到排序队列后面（排序是从小到大排序）

时间复杂度：
最坏/平均/最好的时间复杂度：O（n**2）
空间复杂度：O(1)
"""
def selection_sort(arr):
    # 最小数值存储
    mix = None
    for i in range(len(arr)):
        mix = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[mix]:
                mix = j
        arr[i], arr[mix] = arr[mix],arr[i]
    return arr


if __name__ == '__main__':
    # 示例
    arr = [64, 25, 12, 22, 11]
    print("排序前:", arr)
    sorted_arr = selection_sort(arr)
    print("排序后:", sorted_arr)