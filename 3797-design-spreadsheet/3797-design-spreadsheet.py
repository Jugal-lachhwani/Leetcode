class Spreadsheet(object):

    def __init__(self, rows):
        self.l = l = [[0] * 26 for _ in range(rows + 1)]

    def setCell(self, cell, value):
        col = ord(cell[0]) - 65
        row = int(cell[1:])
        self.l[row][col] = value
        

    def resetCell(self, cell):
        col = ord(cell[0]) - 65
        row = int(cell[1:])

        self.l[row][col] = 0

        

    def getValue(self, formula):
        s = formula[1:].split('+')
        sum = 0
        for i in s:
            if not i[0].isnumeric():
                col = ord(i[0]) - 65
                row = int(i[1:])
                sum += self.l[row][col]
            else:
                sum+=int(i)
        return sum
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)