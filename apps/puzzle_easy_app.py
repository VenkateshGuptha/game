import streamlit as st
from hydralit import HydraHeadApp
from PIL import Image
import requests
import base64
import io
import json
from pymongo import MongoClient
from apps.helpers import *

payload = {
    "sVersion": "005",
    "features": {
      "InputBoundary": {
        "type": "Feature",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                0.0,
                0.0
              ],
              [
                400.0,
                0.0
              ],
              [
                400.0,
                400.0
              ],
              [
                0.0,
                400.0
              ],
              [
                0.0,
                0.0
              ]
            ]
          ]
        },
        "properties": {
          "sID": "InputBoundary",
          "sType": "Boundary",
          "sCategory": "Input",
          "nVersion": 1,
          "fClearance_m": 0.25
        }
      },
      "Origin": {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [
            0.0,
            0.0
          ]
        },
        "properties": {
          "sID": "Origin",
          "sType": "OriginPoint",
          "sCategory": "Input",
          "nVersion": 1
        }
      },
      "EntryGate": {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [
            70.0,
            0.0
          ]
        },
        "properties": {
          "sID": "EntryGate",
          "sType": "GatePoint",
          "sCategory": "Input",
          "nVersion": 1
        }
          },
      "ExitGate": {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [
            200.0,
            0.0
          ]
        },
        "properties": {
          "sID": "ExitGate",
          "sType": "GatePoint",
          "sCategory": "Input",
          "nVersion": 1
        }
      }
    },
      "debugParameters":	{
          "bDumpCvsFiles": False,
          "bUseObstacles": True,
          "bSingleTurnSolutions": False,
      "bAutoMergeAdjacentBlocks": False
      },
      "advancedParameters":	{
      "infill": {
              "bFilterOutShortTracks": True,
              "fShortTrackFilterThreshold": 36.0
          },
          "EORT": {
              "bUseBoundary": False
          },
          "planner": {
              "fPlannerSpacing_m": 3.0
          }
      },
      "inputsStage1": {
      "infill": {
        "sType": "AB",
        "aTypeChoices": [
          "AB",
          "ABLine"
        ],
        "sReferenceID": None,
        "fDirection_deg": 90,
        "fShift_m": 0,
        "fSwathWidth_m": 36
      },
      "headland": {
        "nCount": 1,
        "sGenerationMode": "Generate",
        "aGenerationModeChoices": [
          "AsInput",
          "Generate"
        ],
        "sReferenceID": "InputBoundary"
      },
      "fieldboundary": {
        "sGenerationMode": "AsInput",
        "aGenerationModeChoices": [
          "AsInput",
          "Generate"
        ],
        "sReferenceID": "InputBoundary"
      },
      "obstacles": {
              "fDefaultClearance_m": 0.25,
        "aReferenceIDs": [
          "Obstacle-000"
        ]
      }
    },
    "inputsStage2": {
      "infill": {
        "sHarrowPattern_experimental": "SimpleCoverage",
        "aHarrowPatternChoices_experimental": [
          "BlockRaceTrackPattern(3)",
          "HarrowPattern(4)",
          "SimpleCoverage",
          "DoublePassesSimpleCoverage",
          "2-3AlternatePassesSimpleCoverage"
        ],
        "sSweepDirection_experimental": "ToTheRight",
        "aSweepDirectionChoices_experimental": [
          "ToTheRight",
          "ToTheLeft"
        ],
        "sStartingDirection_experimental": "BA",
        "aStartingDirectionChoices_experimental": [
          "AB",
          "BA"
        ]
          },
      "headland": {
        "sOrdering": "OnEntry",
        "aOrderingChoices": [
          "OnEntry",
          "OnExit",
          "Skip"
        ],
        "sLapDirection": "CCW",
        "aLapDirectionChoices": [
          "CW",
          "CCW"
        ],
        "sSweepDirection": "Inward",
        "aSweepDirectionChoices": [
          "Inward",
          "Outward"
        ]
        },
      "blocks": {
              "bOptimizeBlockSequence": False,
        "manualOrder": [
          "1:1"
        ],
              "directionOverrides_experimental" : {
                  "1:1" : {
                      "sSweepDirection_experimental": "ToTheLeft",
                      "sStartingDirection_experimental": "AB"
                  }
              }
      },
          "gates":
          {
              "sEntryGateReferenceID": "EntryGate",
              "sExitGateReferenceID": "ExitGate"
          }
      },
    "inputsStage3": {
      "vehicle": {
        "sVehicleClass": "4WS",
        "aVehicleClassChoices": [
          "FWS",
          "4WS",
          "Articulated"
        ],
        "parameters": {
          "fWheelBase_m": 3.9,
          "fMaxSteeringAngle_deg": 15,
          "fSlewRate_degps": 7,
          "fWorkSpeed_mps": 5.36,
          "fTurnSpeed_mps": 1.3,
          "fNominalAcc_mps2": 0.2,
          "fLength_m": 9.5,
          "fWidth_m": 35.5,
          "fRearAxelToHitch_m": 2.59
        }
      },
      "implement": {
        "sImplementClass": "ThreePoint",
        "aImplementClassChoices": [
          "ThreePoint",
          "Drawbar(Not Implemented)"
        ],
        "parameters": {
          "fImplementLength_m": 1.26,
          "fImplementWidth_m": 35.5,
          "fDrawBarLength_m": 0.63,
          "fDrawBarWidth_m": 0.75
        }
      }
      },
    "inputsStage4": {
          "EORT": {
              "sTurnStyle": "ForwardOnly",
              "aTurnStyleChoices": [
                  "ForwardOnly",
                  "TwoPoint",
                  "ThreePoint",
                  "ForwardOrReverse"
              ],
              "sTurnType": "HeadlandFollowing",
              "aTurnTypeChoices": [
                  "Free",
                  "HeadlandFollowing"
              ],
              "internalParameters": {
                  "sTurnStartBias": "Neutral",
                  "aTurnStartBiasChoices": [
                      "Neutral",
                      "Early",
                      "Late"
                  ],
                  "sTurnGoalBias": "Neutral",
                  "aTurnGoalBiasChoices": [
                      "Neutral",
                      "Early",
                      "Late"
                  ],
                  "settings":
                  {
                      "fBiasMultiplier": 0.9,
                      "fDesignSpeed_mps": 1.0,						
                      "bByDistance": False,
                      "fMaxStartDistance_m": 6.0,
                      "fMaxGoalDistance_m": 6.0,
                      "fMaxStartDistance_Factor": 3.0,
                      "fMaxGoalDistance_Factor": 3.0
                  }			
              },
              "custom":
              {
                  "x1:1-3": {
                      "sTurnStyle": "ForwardOnly",
                      "aTurnStyleChoices": [
                          "ForwardOnly",
                          "TwoPoint",
                          "ThreePoint",
                          "ForwardOrReverse"
                      ],
                      "sTurnType": "Free",
                      "aTurnTypeChoices": [
                          "Free",
                          "HeadlandFollowing"
                      ],
                      "internalParameters": {
                          "sTurnStartBias": "Late",
                          "aTurnStartBiasChoices": [
                              "Neutral",
                              "Early",
                              "Late"
                          ],
                          "sTurnGoalBias": "Early",
                          "aTurnGoalBiasChoices": [
                              "Neutral",
                              "Early",
                              "Late"
                          ],
                          "settings":
                          {
                              "fBiasMultiplier": 0.9,
                              "fDesignSpeed_mps": 1.0,						
                              "bByDistance": False,
                              "fMaxStartDistance_m": 6.0,
                              "fMaxGoalDistance_m": 6.0,
                              "fMaxStartDistance_Factor": 3.0,
                              "fMaxGoalDistance_Factor": 3.0
                          }					
                      }
                  }
              }
      }
      },
    "outputs": {}
  }

headers = {'Content-type':'application/json'}

class PuzzleEasyApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        
     def run(self):
         column_left, column_right = st.columns(2)
         self.image_placeholder = column_left.empty()

         image = Image.open('resources/puzzle-easy.png')
         self.image_placeholder.image(image)

         # Default values
         column_right.title('Block details')
         self.addBlocksInUI(column_right, 1, 1, 1, 1, 0, 0)

         if column_right.button('Submit'):
             Block1Order = st.session_state.Block1Order
             Block1SweepDirection = st.session_state.Block1SweepDirection
             Block1StartDirection = st.session_state.Block1StartDirection
             
             directions = ['1:1']
             
             Block1Directions = {'sSweepDirection_experimental' : GetSweepDirection(Block1SweepDirection), 'sStartingDirection_experimental': GetStartingDirection(Block1StartDirection)}

             payload['inputsStage2']['blocks']['manualOrder'] = directions
             payload['inputsStage2']['blocks']['directionOverrides_experimental'] = {'1:1':Block1Directions}

             resp = requests.post(st.secrets["stage4"], data=json.dumps(payload), headers=headers)
             output = json.loads(resp.text)
             image = ConvertToImage(output['outputs']['Stage4']['base64Image'])
             self.image_placeholder.image(image, use_column_width=True)
             st.title('Scores')
             results = output['outputs']['Stage4']['report']
             self.SaveResults(results)
             self.displayResults(results)

     def addBlocksInUI(self, column, blockNo, minValue, maxValue, orderNo, sweepDirection, startingDirection):
         blocknumber = 'Block' + str(blockNo)
         blockorder = blocknumber + 'Order'
         blocksweep = blocknumber + 'SweepDirection'
         blockstarting = blocknumber + 'StartDirection'

         column.caption(blocknumber + ' :')
         column.number_input('Order', key=blockorder, min_value=minValue, max_value=maxValue, step=1, value=orderNo)
         column.radio('Start Direction', ('A - North', 'B - South'), key=blockstarting, index=startingDirection)
         column.radio('Sweep Direction', ('To the left', 'To the right'), key=blocksweep, index=sweepDirection)

     def displayResults(self, report):
         st.text('InFill Distance - ' + '{:.5f}'.format(report['fInfillDistance_m']) + 'Meters')
         st.text('Transit Distance - ' + '{:.5f}'.format(report['fTransitDistance_m']) + 'Meters')
         st.text('Total Distance - ' + '{:.5f}'.format(report['fTotalDistance_m']) + 'Meters')

     def SaveResults(self, report):
         block1 = {'blockno':1, 'orderno':st.session_state.Block1Order, 'startdirection':ConvertToDBStartDirection(st.session_state.Block1StartDirection), 'sweepdirection':ConvertToDBSweepDirection(st.session_state.Block1SweepDirection)}

         results = {'userid': self.session_state.UserID, 'blocks':[block1], 'puzzlenumber':1, 'infilldistance':report['fInfillDistance_m'], 'totaldistance':report['fTotalDistance_m'], 'transitdistance':report['fTransitDistance_m']}
         client = MongoClient(st.secrets["url"])
         db = client.Game
         my_collections = db.PuzzleResults
         x = my_collections.insert_one(results)