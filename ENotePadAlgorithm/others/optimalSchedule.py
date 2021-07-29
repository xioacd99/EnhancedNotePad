import math

# 多维指标最短路径

# 无  : 0
# 编码: 1
# 加密: 2
# 压缩: 3
# 移动: 4
# 编译: 5
# 替换: 6
# 重命名: 7
# 语法检查: 8

INF = float('inf') / 4


class OptimialSchedule(object):
    def __init__(self):
        # 默认权重矩阵
        self.weight = [
            [[0, 0], [800, 300], [700, 500], [500, 500], [100, 400], [100, 100], [300, 500], [10, 0], [20, 0]],
            [[INF, INF], [0, 0], [1000, 300], [500, 200], [INF, INF], [INF, INF], [INF, INF], [INF, INF], [INF, INF]],
            [[INF, INF], [INF, INF], [0, 0], [700, 100], [INF, INF], [INF, INF], [INF, INF], [INF, INF], [INF, INF]],
            [[INF, INF], [INF, INF], [INF, INF], [0, 0], [INF, INF], [INF, INF], [INF, INF], [INF, INF], [INF, INF]],
            [[INF, INF], [INF, INF], [INF, INF], [INF, INF], [0, 0], [INF, INF], [200, 100], [INF, INF], [INF, INF]],
            [[INF, INF], [INF, INF], [INF, INF], [INF, INF], [INF, INF], [0, 0], [INF, INF], [INF, INF], [INF, INF]],
            [[INF, INF], [INF, INF], [INF, INF], [INF, INF], [INF, INF], [INF, INF], [0, 0], [50, 30], [10, 10]],
            [[INF, INF], [INF, INF], [INF, INF], [INF, INF], [INF, INF], [INF, INF], [INF, INF], [0, 0], [30, 0]],
            [[INF, INF], [INF, INF], [INF, INF], [INF, INF], [INF, INF], [50, 50], [INF, INF], [INF, INF], [0, 0]]
        ]

    def setWeight(self, weight):
        self.weight = weight

    # 回溯法求全排列
    def permute(self, nums):
        def backtrack(first=0):
            if first == n:
                results.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        results = []
        backtrack()
        return results

    # 输入一个选择的操作列表，输出路径
    def getPath(self, chioces):
        chioces.append(0)
        assign = self.permute(chioces)
        minPath = []
        minCost = INF
        for i in range(len(assign)):
            tmpCost = 0
            for j in range(len(assign[i]) - 1):
                row= assign[i][j]
                col=assign[i][j+1]
                tmpCost += math.sqrt((self.weight[row][col][0])**2 + (self.weight[row][col][1])**2)
            if tmpCost < minCost:
                minCost = tmpCost
                minPath = assign[i]
        return minPath


if __name__ == '__main__':
    test = OptimialSchedule()
    result = test.getPath([1, 3])
    print(result)
