from fastapi import APIRouter
from fastapi.responses import HTMLResponse, StreamingResponse

from src.excel.service import convert_file_to
router = APIRouter()


@router.get('')
def get_converted_data():
    try:
        print('Converted Data')
        return {'data': 'Sample is working'}
    except: 
        pass

@router.post('/convert-to/{type}')
def convert_excel(type, data = None):
    try:
        print(data, type)
        res = convert_file_to(data=data, type=type)
        opts = {
            "media_type":'text/html',
            "headers":{"Content-Disposition": f"attachment; filename=data.html"}
        }

        if type == 'json':
            return res
        elif type == 'csv':
            opts = {
                "media_type":'text/csv',
                "headers":{"Content-Disposition": f"attachment; filename=data.csv"}
            }
        return StreamingResponse(
            iter([res]),
            **opts
        )
    except Exception as e:
        print('Error while :>> executing convert_file_to from convert_excel api')
        print(e)
        pass
