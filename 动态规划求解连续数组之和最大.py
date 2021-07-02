
# # 用动态规划计算连续数组之和最大
# num = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Max = num[0]
# f_max = num[0]
#
# for i in range(1, len(num)-1):
#     if f_max >= 0:
#         f_max = f_max + num[i]
#
#     else:
#         f_max = num[i]
#     Max = max(f_max,Max)
#
# print(Max)

# 用分治算法计算
num = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def Max_list(start,final):
    if start == final:
        return num[start]
    middle = (final+start)//2  # ****这个地方是最需要注意的，可不能写成 "/"
# ***************判断左子树***************************
    left_max = Max_list(start, middle)
#  *******************判断右子树***********************
    right_max = Max_list(middle + 1, final)

    leftBorderSum = num[middle]
    leftSum = num[middle]
    for i in range(middle - 1, start, -1):
        leftSum += num[i]
        if leftSum > leftBorderSum:
            # 不断更新左区块的最大值
            leftBorderSum = leftSum

    rightBorderSum = num[middle + 1]
    rightSum = num[middle + 1]
    for i in range(middle + 2, final):
        rightSum += num[i]
        if rightSum > rightBorderSum:
            # 不断更新右区块的最大值
            rightBorderSum = rightSum
    # 左边界的和 + 右边那块的和
    BorderSum = leftBorderSum + rightBorderSum
    return max(left_max, right_max, BorderSum)

if __name__ == '__main__':
    Max = Max_list(0,len(num)-1)
    print(Max)

