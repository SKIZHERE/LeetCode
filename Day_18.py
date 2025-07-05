# 118. Pascal's Triangle

class Solution(object):
    def generate(self, numRows):
        x = [[1]]
        if numRows == 1:
            return x
        x.append([1,1])
        for i in range (1,numRows-1):
            z = [1, 1]
            for j in range(len(x[i])-1):
                n = x[i][j] + x[i][j+1]
                z.insert(j+1, n)
            x.append(z)
        return x

