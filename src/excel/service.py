import pandas as pd
import base64
import io
import os

def read_excel_from_base64(base64_data):
    decoded_bites = base64.b64decode(base64_data)
    return io.BytesIO(decoded_bites)

def convert_file_to(type:str, data):
    # try:   
    current_dir = os.path.dirname(__file__)
    test_file_path = os.path.join(current_dir, 'text.txt')
    file = open(test_file_path, 'r') 
    data = file.read()
    excel_file = read_excel_from_base64(base64_data=data) 
    excel_data = pd.read_excel(excel_file)

    return excel_data.to_json()
    # except:
    #     pass
    # return None
    # return df.to_json();