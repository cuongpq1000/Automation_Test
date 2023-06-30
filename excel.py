import pandas as pd
import json
import os

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

def convertExceltoJSON(excelFile, jsonFile):
    # Get current folder
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Create folder excel path
    excelPath = os.path.join(current_dir, "testCase", "excel")

    # Create file excel path
    excelFilePath = f"{excelPath}\{excelFile}"

    # Read file excel
    Excel = pd.read_excel(excelFilePath)

    # Convert Excel to JSON
    Json = Excel.to_json(orient='records')

    # Create folder json path
    jsonPath = os.path.join(current_dir, "testCase", "json")

    # Create file json path
    jsonFilePath = f"{jsonPath}\{jsonFile}.json"

    # Create json file
    out_file = open(jsonFilePath, "w")
    json.dump(json.loads(Json), out_file, indent = 6)
