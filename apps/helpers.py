from PIL import Image
import base64
import io

def ConvertToDBStartDirection(startingDirection) -> int:
    if 'A - North' == startingDirection:
        return 0
    return 1

def ConvertToUIStartDirection(startingDirection) -> str:
    if 0 == startingDirection:
        return 'A - North'
    return 'B - Sourth'

def ConvertToDBSweepDirection(sweepDirection) -> int:
    if 'To the left' == sweepDirection:
        return 0
    return 1

def ConvertToUISweepDirection(sweepDirection) -> str:
    if 0 == sweepDirection:
        return 'To the left'
    return 'To the right'

def GetStartingDirection(startingDirection) -> str:
    if 'A - North' == startingDirection:
        return 'AB'
    return 'BA'

def GetSweepDirection(sweepDirection) -> str:
    if 'To the left' == sweepDirection:
        return 'ToTheLeft'
    return 'ToTheRight'

def ConvertToImage(base64string):
    buf = io.BytesIO(base64.b64decode(base64string))
    return Image.open(buf)
