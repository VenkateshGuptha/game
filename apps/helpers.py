import streamlit as st
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

def DisplayResults(container, report):
    formatter = '{:.1f}'
    new_title = '<p style="font-family:sans-serif; color:Brown; font-style: italic; font-weight: bold; font-size: 36px;">Scores:</p>'
    container.markdown(new_title, unsafe_allow_html=True)

    container.markdown(GetResultString('InFill Distance: ', formatter.format(report['fInfillDistance_m'] / 1000) + 'Km'), unsafe_allow_html=True)
    container.markdown(GetResultString('Transit Distance: ', formatter.format(report['fTransitDistance_m'] / 1000) + 'Km'), unsafe_allow_html=True)
    container.markdown(GetResultString('Total Distance: ', formatter.format(report['fTotalDistance_m'] / 1000) + 'Km'), unsafe_allow_html=True)

def GetResultString(key, value):
    return '<div style="font-family:sans-serif; color:Black; font-size: 24px;float:left;">' + key + '</div><div style="font-family:sans-serif; color:Green;font-style: italic; font-size: 24px;float:left;"> '+ value + '</div>'