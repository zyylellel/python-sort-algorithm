# .插入排序：插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，
# 从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序；首先将第一个作为已经排好序的，
# 然后每次从后的取出插入到前面并排序；
# 时间复杂度：O(n²)
# 空间复杂度：O(1)
# 稳定性：稳定
import random
# 步骤2：创建一个空列表，用于存放待排序随机数据集



data = [random.randint(0, 100) for i in range(10)]
print('待排序的随机数列: {0}'.format(data))
# 步骤3：获取列表数据集中随机数的个数
length = len(data)
# 步骤4：嵌套for循环实现插入排序
# 外层循环控制排序次数
for i in range(1, length):
    # 将当前的数字备份
    x = data[i]
    # 内层循环进行
    for j in range(i,-1,-1):
        # j为当前位置，试探j-1位置
        if x < data[j-1]:
            # 换值
            data[j] = data[j-1]
        else:
            break # 确定j位置
    data[j] = x
# 步骤5：输出排序后的结果
print('排序后的有序序列: {0}'.format(data))