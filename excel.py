import pandas as pd

def run():
    excel = readExcel('Demo.xlsx', 'Sheet1')
    print("get cell [0,1]", getCell(excel, 0, 1))
    print("get row [2]", getRow(excel, 2))
    print("get col [1]", getCol(excel, 1))

def readExcel(name, sheetname):
    df = pd.read_excel(name, sheet_name=sheetname, dtype=object, header=None)
    return df

def getCell(data, row, col):
    return data.values[row][col]

def getRow(data, index):
    return data.values[index]

def getCol(data, index):
    return data[index].tolist()
run()