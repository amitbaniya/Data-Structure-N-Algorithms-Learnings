'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
'''

def convert(s, numRows):
    s_metrix = []
    row = 0
    column = 0
    forward = True
    for _ in range(numRows):
        s_metrix.append([])
    for char in s:
        if row < numRows and forward:
            s_metrix[row].append(char)
            row += 1
            if row == numRows :
                forward = False
                row -= 1
        elif row <= numRows and not forward and row != 0:
            column +=1
            row -= 1
            s_metrix[row].append(char)
            if row == 1:
                forward = True
                row -= 1
            elif row == 0:
                forward= True
                row += 1
    output_string = ""
    print(s_metrix)
    for row in s_metrix:
        for char in row:
            output_string += char
    return(output_string)

if __name__ == '__main__':
    s = "ABCD"
    numRows = 2
    print(convert(s, numRows))
