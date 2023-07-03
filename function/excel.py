import pandas as pd
import json
import os
import io
from PIL import Image
from generalFunction import getPath
ap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def readExcel(name, sheetname):
    df = pd.read_excel(name, sheet_name=sheetname, dtype=object, header=None)
    return df

def getCell(data, row, col):
    return data.values[row][col]

def getRow(data, index):
    return data.values[index]

def getCol(data, index):
    return data[index].tolist()

def get_resized_image_data(file_path, bound_width_height):
    # get the image and resize it
    im = Image.open(file_path)
    im.thumbnail(bound_width_height, Image.ANTIALIAS)  # ANTIALIAS is important if shrinking

    # stuff the image data into a bytestream that excel can read
    im_bytes = io.BytesIO()
    im.save(im_bytes, format='PNG')
    return im_bytes

def writeScreeshot(worksheet, screenshotImage):
    col = 2; row = 1
    for item in screenshotImage:
        col = 2
        for img in item:
            worksheet.insert_image(f"{ap[col]}{row}", img, {'x_scale': 0.5, 'y_scale': 0.5})
            col = col + 11
        row = row + 20

def writeExcel(data, fileName):
    path = getPath(f"testCase/testResult/{fileName}")
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    screenshotImage = [];row = 0
    for item in data:
        screenshotImage.append(item["screenshot"])
        del item["screenshot"]
    
        df = pd.DataFrame([item])
        df.to_excel(writer, sheet_name='Sheet1', index=False, startcol=0,startrow=row)
        row = row + 20

    # Get the xlsxwriter workbook and worksheet objects.
    worksheet = writer.sheets['Sheet1']
    # Insert image.
    writeScreeshot(worksheet, screenshotImage)

    writer.close()


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
