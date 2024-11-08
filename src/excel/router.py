from fastapi import APIRouter
from src.excel.service import convert_file_to
router = APIRouter()


@router.get('')
def get_converted_data():
    try:
        print('Converted Data')
        return {'data': 'Sample is working'}
    except: 
        pass

@router.post('/convert')
def convert_excel(data):
    try:
        return convert_file_to(data='', type='')
        # print(data)
    except Exception as e:
        print('Error while :>> executing convert_file_to from convert_excel api')
        print(e)
        # pass

