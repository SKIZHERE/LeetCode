# print(chr(64+1))
# colNum = 100
# x = 703//26
# y = 703%26
# print(x,y)
# print(chr(64+y))
# print(chr(64+x))
columnNumber = 703
op = ""
while columnNumber > 0:
    columnNumber-=1
    charr = columnNumber % 26
    op = chr(65 + charr) + op
    columnNumber = columnNumber // 26
print(op)