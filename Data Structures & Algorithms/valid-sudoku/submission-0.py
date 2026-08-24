class Solution:
    def isValidSudoku(self, board):
        # 初始化三个数组，每个数组包含9个set集合
        # 用来记录每一行、每一列、每个3x3小格子出现过的数字
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 3x3小格子编号从0到8

        # 遍历数独的每一个格子
        for i in range(9):         # i是行索引，从0到8
            for j in range(9):     # j是列索引，从0到8
                num = board[i][j] # 当前格子的数字或'.'

                if num == '.':
                    # 空格不做任何判断，跳过
                    continue

                # 计算当前格子属于哪个3x3小格子
                # i // 3表示第几组行，j // 3表示第几组列
                box_index = (i // 3) * 3 + (j // 3)

                # 判断当前数字是否已经在对应的行、列、盒子里出现过
                if (num in rows[i] or
                    num in cols[j] or
                    num in boxes[box_index]):
                    # 如果出现重复，说明不符合数独规则，返回False
                    return False

                # 没有重复，则把数字添加到对应的行、列、盒子的集合中
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        # 遍历完所有格子后没有发现冲突，说明数独合法
        return True
