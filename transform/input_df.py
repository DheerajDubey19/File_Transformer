import pandas as pd
import numpy as np
import os
from django.shortcuts import get_object_or_404
from .models import Category, Insurer, Month

def myFunc(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input File not found: {file_path}")

    # Converting the excel sheet into Dataframe
    sheet = pd.read_excel(file_path, sheet_name=None)
    sheet1_df = sheet['Segmentwise Report']
    sheet2_df = sheet['Miscellaneous portfolio']
    sheet3_df = sheet['Health Portfolio']
    
    #Extracting the month and year from the dataframe
    date_lst = sheet1_df.columns[0].split('UPTO')[1].split()
    Month = date_lst[0][:3]
    Year = int(date_lst[1])


    print("***********first******************")

    # Renaming the column name into desired form and adding year and month column
    sheet1_df.columns = sheet1_df.iloc[0]
    sheet1_df = sheet1_df[1:].reset_index(drop=True)
    sheet1_df = sheet1_df.rename(columns={np.nan: 'insurer'})
    sheet1_df['Year'] = Year
    sheet1_df['Month'] = Month
    sheet1_df.loc[sheet1_df['insurer'] == 'Previous Year', 'Year'] -= 1

    sheet2_df.columns = sheet2_df.iloc[0]
    sheet2_df = sheet2_df[1:].reset_index(drop=True)
    sheet2_df = sheet2_df.rename(columns={np.nan: 'insurer'})
    sheet2_df['Year'] = Year
    sheet2_df['Month'] = Month
    sheet2_df.loc[sheet2_df['insurer'] == 'Previous Year', 'Year'] -= 1

    sheet3_df.columns = sheet3_df.iloc[1]
    sheet3_df = sheet3_df[2:].reset_index(drop=True)
    sheet3_df = sheet3_df.rename(columns={np.nan: 'insurer'})
    sheet3_df['Year'] = Year
    sheet3_df['Month'] = Month
    sheet3_df.loc[sheet3_df['insurer'] == 'Previous Year', 'Year'] -= 1

    sheet1_df['clubbed_name'] = np.nan
    sheet1_df['category'] = np.nan

    def get_clubbed_name_and_category(insurer_name):
        insurer = get_object_or_404(Insurer, insurer=insurer_name)
        category = insurer.clubbed_name
        result = {
            'clubbed_name': category.clubbed_name,
            'category': category.category
        }
        # print(insurer)
        return result

    dct_insurer = {}
    
    print("***********mid*****************")

    # Adding the clubbed_name and category from the database to the dataframe using a dictionary to avoid multiple database calls
    for index, row in sheet1_df.iterrows():
        insurer_name = row['insurer']
        try:
            if insurer_name not in dct_insurer:
                result = get_clubbed_name_and_category(insurer_name)
                dct_insurer[insurer_name] = result
            sheet1_df.at[index, 'clubbed_name'] = dct_insurer[insurer_name]['clubbed_name']
            sheet1_df.at[index, 'category'] = dct_insurer[insurer_name]['category']
            sheet1_df.at[index + 1, 'clubbed_name'] = dct_insurer[insurer_name]['clubbed_name']
            sheet1_df.at[index + 1, 'category'] = dct_insurer[insurer_name]['category']
        except:
            continue

    # print(sheet1_df)

    for index, row in sheet2_df.iterrows():
        insurer_name = row['insurer']
        try:
            if insurer_name not in dct_insurer:
                result = get_clubbed_name_and_category(insurer_name)
                dct_insurer[insurer_name] = result
            sheet2_df.at[index, 'clubbed_name'] = dct_insurer[insurer_name]['clubbed_name']
            sheet2_df.at[index, 'category'] = dct_insurer[insurer_name]['category']
            sheet2_df.at[index + 1, 'clubbed_name'] = dct_insurer[insurer_name]['clubbed_name']
            sheet2_df.at[index + 1, 'category'] = dct_insurer[insurer_name]['category']
        except:
            continue

    for index, row in sheet3_df.iterrows():
        insurer_name = row['insurer']
        try:
            if insurer_name not in dct_insurer:
                result = get_clubbed_name_and_category(insurer_name)
                dct_insurer[insurer_name] = result
            sheet3_df.at[index, 'clubbed_name'] = dct_insurer[insurer_name]['clubbed_name']
            sheet3_df.at[index, 'category'] = dct_insurer[insurer_name]['category']
            sheet3_df.at[index + 1, 'clubbed_name'] = dct_insurer[insurer_name]['clubbed_name']
            sheet3_df.at[index + 1, 'category'] = dct_insurer[insurer_name]['category']
        except:
            continue

    products = ["All Other miscellaneous","Aviation","Credit Guarantee","Crop Insurance","Engineering","Fire","Health-Government schemes","Health-Group","Health-Retail","Liability","Marine Cargo","Marine Hull","Motor OD","Motor TP","Overseas Medical","P.A."]

    #Creating the output dataframe in the desired form  
    output = pd.DataFrame(columns=['Year','Month','category','clubbed_name','Product','Value'])
    print("***********last******************")
    for index,row in sheet1_df.iterrows():
        # print(row)
        if row['insurer']=='Previous Year':
            for product in products:
                if product in sheet1_df.columns:
                    new_row = pd.DataFrame({
                    'Year': [row['Year']],
                    'Month': [row['Month']],
                    'category': [row['category']],
                    'clubbed_name': [row['clubbed_name']],
                    'Product': [product],
                    'Value': [row[product]]
                    })
                    output = pd.concat([output, new_row], ignore_index=True)

    for index,row in sheet2_df.iterrows():
        if row['insurer']=='Previous Year':
            for product in products:
                if product in sheet2_df.columns:
                    new_row = pd.DataFrame({
                    'Year': [row['Year']],
                    'Month': [row['Month']],
                    'category': [row['category']],
                    'clubbed_name': [row['clubbed_name']],
                    'Product': [product],
                    'Value': [row[product]]
                    })
                    output = pd.concat([output, new_row], ignore_index=True)

    for index,row in sheet3_df.iterrows():
        if row['insurer']=='Previous Year':
            for product in products:
                if product in sheet3_df.columns:
                    new_row = pd.DataFrame({
                    'Year': [row['Year']],
                    'Month': [row['Month']],
                    'category': [row['category']],
                    'clubbed_name': [row['clubbed_name']],
                    'Product': [product],
                    'Value': [row[product]]
                    })
                    output = pd.concat([output, new_row], ignore_index=True)

    #sorting the output dataframe on the clubbed_name
    print("**********mic check******************")

    output = output.sort_values(by='clubbed_name')

    # print("**********mic check******************")

    output_dir = 'media/outputs/'
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, 'output.xlsx')
    output.to_excel(output_file_path, index=False)

    print("*****************last output*******************")

    return output_file_path
