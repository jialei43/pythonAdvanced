num_list = range(100)

target = int(input('请输入目标值'))
pre_current = 0
current = 0

length = len(num_list)

total = 100

while True:
    total = total if total % 2 == 0 else total+1
    pre_current = current
    current = total // 2
    if target < current:
        print(f'猜大了,猜的值为{current}')
        total = pre_current + current
    if target > current:
        total = current + length
        print(f'猜小了,猜的值为{current}')
    if target == current:
        print(f'猜对了，目标值是{current}')
        break
