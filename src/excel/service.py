import pandas as pd
import base64
import io
import os
import json


def base64_to_excel(data:str):
    return pd.read_excel(data)

def read_excel_from_base64(base64_data):
    decoded_bites = base64.b64decode(base64_data)
    decoded_buffer = io.BytesIO(decoded_bites)
    return base64_to_excel(data=decoded_buffer)

def convert_file_to(type:str, data):
    # try:   
    current_dir = os.path.dirname(__file__)
    test_file_path = os.path.join(current_dir, 'text.txt')
    file = open(test_file_path, 'r') 
    data = file.read()
    excel_data = read_excel_from_base64(base64_data=data) 
    return excel_data.to_dict(orient='records')
    # except:
    #     pass
    # return None
    # return df.to_json();