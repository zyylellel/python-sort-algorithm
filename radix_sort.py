# 基数排序：透过键值的部份资讯，将要排序的元素分配至某些“桶”中，藉以达到排序的作用
# 时间复杂度：O(d(r+n))
# 空间复杂度：O(rd+n)
# 稳定性：稳定

def radix_sort(array):
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(array):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(array)):
            num = (array[i] // 10 ** digit) % 10
            bucket[num].append(array[i])
        array.clear()
        for i in range(len(bucket)):
            array += bucket[i]
        digit += 1
    return array

a = radix_sort([1,23,3,12,2,234,210])
print(a)