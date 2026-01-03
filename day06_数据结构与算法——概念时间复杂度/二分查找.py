def binary_search_recursive(arr, target, low, high):
    # 如果范围有效
    if low <= high:
        mid = (low + high) // 2  # 找中间元素

        # 判断中间元素是否为目标
        if arr[mid] == target:
            return mid  # 返回元素索引
        elif arr[mid] > target:
            return binary_search_recursive(arr, target, low, mid - 1)  # 递归查找左半部分
        else:
            return binary_search_recursive(arr, target, mid + 1, high)  # 递归查找右半部分
    else:
        return -1  # 如果没有找到目标，返回 -1


# 测试递归版
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Element found at index: {result}")



def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # 找中间元素

        # 判断中间元素是否为目标
        if arr[mid] == target:
            return mid  # 返回元素索引
        elif arr[mid] > target:
            high = mid - 1  # 如果目标在左半部分
        else:
            low = mid + 1  # 如果目标在右半部分

    return -1  # 如果没有找到目标，返回 -1


# 测试迭代版
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search_iterative(arr, target)
print(f"Element found at index: {result}")

