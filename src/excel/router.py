from fastapi import APIRouter
from service import convert_file_to

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
        convert_file_to(data=data['val'])
        print(data)
    except:
        pass

