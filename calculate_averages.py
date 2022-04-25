import os,shutil,pandas as pd, xlsxwriter
# This script will calculate the averages of all the data in a specified sheet

# Get the user input for which movie FOLDER to calculate all averages for
user_input = input('Enter a directory containing compound Imaris output files for measured statistics\n')
print(f'Accessing {user_input}')
assert os.path.exists(user_input), "I did not find the directory at, "+str(user_input)
print("Hooray we found your directory!")
print(os.listdir(user_input))

# Make a new excel file in the same directory and call it Compiled
new_book = xlsxwriter.Workbook('Compiled.xlsx')

# Find the end of the values in each sheet and calculate the full averages
for file in os.listdir(user_input):
    count = 0
    # To open the workbook workbook object is created
    if file.endswith(".xls"):
        print(os.path.join(user_input, file))
        wb = pd.ExcelFile(os.path.join(user_input, file))
        sheetnames = wb.sheet_names
        for sheet in sheetnames:
            if sheet !='Overall':
                df = pd.read_excel(wb, header=1, sheetname=sheet)
                print(df)
                print(df.index[-1]) #this is the index number of the last row of the sheet
                col_names = list(df.columns)
                print(col_names)
                ave = df[col_names[0]].mean()
                print('AVERAGE')
                print(ave)
                if not col_names[0] in new_book.sheetnames: #if this is the first position for the given movie create the spreadsheet
                    worksheet = new_book.add_worksheet(col_names[0])

                ws_name = col_names[0]
                ws_name.write(count,0, ave)
    count+=1
new_book.close()