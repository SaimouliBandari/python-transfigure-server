from fastapi import APIRouter

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
        print(data)
    except:
        pass

