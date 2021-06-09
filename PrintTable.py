table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    count = 0
    while count < len(tableData):
        for item in tableData[count]:
            if len(item) > colWidths[count]:
                colWidths[count] = len(item)
        count += 1

    for word in range(len(tableData[0])):
        for item in range(len(tableData)):
            print(tableData[item][word].rjust(colWidths[item]), end=' ')
        print()



printTable(table_data)
