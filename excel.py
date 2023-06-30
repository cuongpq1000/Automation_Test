import pandas


def readExcel():
    excel_data_df = pandas.read_excel('Demo.xlsx', sheet_name='Sheet1')
    # print whole sheet data
    print(excel_data_df)

readExcel()