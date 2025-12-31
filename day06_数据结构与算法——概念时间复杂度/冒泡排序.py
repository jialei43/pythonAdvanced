"""
1. 冒泡排序 (Bubble Sort)

原理：
冒泡排序通过重复地比较相邻元素，并将较大的元素交换到后面，从而“冒泡”出最大元素。重复此过程，直到所有元素有序。

时间复杂度：

最坏/平均时间复杂度：𝑂(𝑛2)
最好时间复杂度：𝑂(𝑛)（当输入数据已排序时）
空间复杂度：O(1)
"""
def bubble_sort(arr):
    for i in range(len(arr)):
        # 这个-1主要是因为倒数第二个元素和最后一个像素比较后，就确定了最大的是那个了，
        # 所以最后一个就不用去和后面的比较，且后面已经都是拍好的顺序都是每次循环的最大值
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                # temp = arr[j+1]
                # arr[j+1] = arr[j]
                # arr[j] = temp
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True
        # 如果第一轮循环没有一个进行交换，说明程序本来就是有序的，不需要进行排序了
        if not swapped:
            break
    return arr
if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", arr)
    sorted_arr = bubble_sort(arr)
    print("排序后:", sorted_arr)
