class Solution:
    def isValidSudoku(self,b):
        blocks = [[[], [], []], [[], [], []], [[], [], []]]
        # print(blocks)
        for i in range(len(b)):
            for j in range(len(b)):
                # print(i//3,j//3)
                if b[i][j] == ".":
                    continue
                if b[i][j] in blocks[i // 3][j // 3]:
                    return False
                blocks[i // 3][j // 3].append(b[i][j])
        # print(blocks)
        for i in range(len(b)):
            s = set()
            s1 = set()
            for j in range(len(b)):
                # print(b[i][j], b[i + 1 :][j])
                # if b[i][j] != "." and b[i][j] in b[i][j + 1 :]:
                #     return False
                if b[j][i] != "." and b[j][i] in s:
                    return False
                if b[i][j] != "." and b[i][j] in s1:
                    return False
                s1.add(b[i][j])
                s.add(b[j][i])
                print(s)

        return True