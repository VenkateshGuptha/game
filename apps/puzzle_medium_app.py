import streamlit as st
from hydralit import HydraHeadApp
from PIL import Image
import requests
import base64
import io
import json
from pymongo import MongoClient

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
              361.0,
              0.0
            ],
            [
              252.7,
              361.0
            ],
            [
              108.3,
              361.0
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
    "Obstacle-000": {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              140.79,
              108.3
            ],
            [
              220.21,
              108.3
            ],
            [
              180.5,
              240.666667
            ],
            [
              140.79,
              108.3
            ]
          ]
        ]
      },
      "properties": {
        "sID": "Obstacle-000",
        "sType": "Boundary",
        "sCategory": "Input",
        "nVersion": 1,
        "fClearance_m": 0.25
      }
    }
  },
	"debugParameters":	{
		"bDumpCvsFiles": False,
		"bUseObstacles": True,
		"bSingleTurnSolutions": True,
    "bAutoMergeAdjacentBlocks": False
	},
	"advancedParameters":	{
    "infill": {
			"bFilterOutShortTracks": True,
			"fShortTrackFilterThreshold": 36.0
		},
		"EORT": {
			"bUseBoundary": True
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
      "sStartingDirection_experimental": "AB",
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
        "1:2",
        "1:1",
        "1:3"
      ],
			"directionOverrides_experimental" : {
				"1:1" : {
					"sSweepDirection_experimental": "ToTheLeft",
					"sStartingDirection_experimental": "BA"
				}	
			}
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
st.session_state['row_direction'] = 90

def LoadPuzzleDefaultImage() -> str:
    client = MongoClient(st.secrets["url"])
    db = client.Game
    my_collections = db.PuzzleDetails
    return(list(my_collections.find({"number": 2}))[0]['puzzle_default_image'])

buf = LoadPuzzleDefaultImage()
st.session_state['puzzle_image'] = Image.open(io.BytesIO(base64.b64decode(buf)))

class PuzzleMediumApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

     def run(self):
         column_left, column_right = st.columns(2)
         self.image_placeholder = column_left.empty()

         '''row_direction = column_left.slider("Row direction", 0, 360, st.session_state['row_direction'], key='RowDirection')
         if(row_direction != st.session_state.row_direction):
             st.session_state.row_direction = row_direction
             self.onRowDirectionChange()'''

         #self.image_placeholder.image(st.session_state['puzzle_image'], use_column_width=True)
         image = Image.open('resources\\medium.png')
         self.image_placeholder.image(image)

         column_right.title('Block details')
         self.addBlocksInUI(column_right, 1, 1, 3, 1, 1, 1)
         self.addBlocksInUI(column_right, 2, 1, 3, 2, 1, 1)
         self.addBlocksInUI(column_right, 3, 1, 3, 3, 1, 1)

         if column_right.button('Submit'):
             Block1Order = st.session_state.Block1Order
             Block1SweepDirection = st.session_state.Block1SweepDirection
             Block1StartDirection = st.session_state.Block1StartDirection
             Block2Order = st.session_state.Block2Order
             Block2SweepDirection = st.session_state.Block2SweepDirection
             Block2StartDirection = st.session_state.Block2StartDirection
             Block3Order = st.session_state.Block3Order
             Block3SweepDirection = st.session_state.Block3SweepDirection
             Block3StartDirection = st.session_state.Block3StartDirection

             if(6 != Block1Order + Block2Order + Block3Order):
                st.error('Block number should be unique')
                return
             
             directions = []
             for i in range(1, 4):
                 if(Block1Order == i):
                    directions.append('1:' + str(1))
                
                 if(Block2Order == i):
                    directions.append('1:' + str(2))
                    
                 if(Block3Order == i):
                    directions.append('1:' + str(3))
             
             Block1Directions = {'sSweepDirection_experimental' : self.GetSweepDirection(Block1SweepDirection), 'sStartingDirection_experimental': self.GetStartingDirection(Block1StartDirection)}
             Block2Directions = {'sSweepDirection_experimental' : self.GetSweepDirection(Block2SweepDirection), 'sStartingDirection_experimental': self.GetStartingDirection(Block2StartDirection)}
             Block3Directions = {'sSweepDirection_experimental' : self.GetSweepDirection(Block3SweepDirection), 'sStartingDirection_experimental': self.GetStartingDirection(Block3StartDirection)}

             payload['inputsStage2']['blocks']['manualOrder'] = directions
             payload['inputsStage2']['blocks']['directionOverrides_experimental'] = {'1:1':Block1Directions, '1:2':Block2Directions, '1:3':Block3Directions}

             #st.text(directions)
             #st.json(payload)
             resp = requests.post(st.secrets["stage2"], data=json.dumps(payload), headers=headers)
             output = json.loads(resp.text)
             self.displayPuzzleImage(output['outputs']['Stage2']['base64Image'])
             st.title('Scores')
             results = output['outputs']['Stage2']['report']
             self.SaveResults(results)
             self.displayResults(results)

     def GetStartingDirection(self, startingDirection) -> str:
         if 'A - North' == startingDirection:
            return 'AB'
         return 'BA'

     def GetSweepDirection(self, sweepDirection) -> str:
         if 'To the left' == sweepDirection:
            return 'ToTheLeft'
         return 'ToTheRight'

     def addBlocksInUI(self, column, blockNo, minValue, maxValue, orderNo, sweepDirection, startingDirection):
         blocknumber = 'Block' + str(blockNo)
         blockorder = blocknumber + 'Order'
         blocksweep = blocknumber + 'SweepDirection'
         blockstarting = blocknumber + 'StartDirection'

         column.caption(blocknumber + ' :')
         column.number_input('Order', key=blockorder, min_value=minValue, max_value=maxValue, step=1, value=orderNo)
         column.radio('Start Direction', ('A - North', 'B - South'), key=blockstarting, index=startingDirection)
         column.radio('Sweep Direction', ('To the left', 'To the right'), key=blocksweep, index=sweepDirection)

     def onRowDirectionChange(self):
        payload['inputsStage1']['infill']['fDirection_deg'] = st.session_state.RowDirection
        resp = requests.post(st.secrets["stage2"], data=json.dumps(payload), headers=headers)
        output = json.loads(resp.text)
        self.displayPuzzleImage(output['outputs']['Stage2']['base64Image'])

     def displayPuzzleImage(self, base64string):
         buf = io.BytesIO(base64.b64decode(base64string))
         image = Image.open(buf)
         self.image_placeholder.image(image, use_column_width=True)
         st.session_state['puzzle_image'] = image;

     def displayResults(self, report):
         st.text('Estimated InFill Distance - ' + '{:.2f}'.format(report['fEstimatedInfillDistance_m'] / 1000) + 'Km')
         st.text('Estimated Total Distance - ' + '{:.2f}'.format(report['fEstimatedTotalDistance_m'] / 1000) + 'Km')

     def SaveResults(self, report):
         block1 = {'blockno':1, 'orderno':st.session_state.Block1Order, 'startdirection':self.ConvertToDBStartDirection(st.session_state.Block1StartDirection), 'sweepdirection':self.ConvertToDBSweepDirection(st.session_state.Block1SweepDirection)}
         block2 = {'blockno':2, 'orderno':st.session_state.Block2Order, 'startdirection':self.ConvertToDBStartDirection(st.session_state.Block2StartDirection), 'sweepdirection':self.ConvertToDBSweepDirection(st.session_state.Block2SweepDirection)}
         block3 = {'blockno':3, 'orderno':st.session_state.Block3Order, 'startdirection':self.ConvertToDBStartDirection(st.session_state.Block3StartDirection), 'sweepdirection':self.ConvertToDBSweepDirection(st.session_state.Block3SweepDirection)}

         results = {'userid': self.session_state.UserID, 'blocks':[block1, block2, block3], 'puzzlenumber':2, 'infilldistance':report['fEstimatedInfillDistance_m'], 'totaldistance':report['fEstimatedTotalDistance_m']}
         client = MongoClient(st.secrets["url"])
         db = client.Game
         my_collections = db.PuzzleResults
         x = my_collections.insert_one(results)

     def ConvertToDBStartDirection(self, startingDirection) -> int:
         if 'A - North' == startingDirection:
            return 0
         return 1

     def ConvertToUIStartDirection(self, startingDirection) -> str:
         if 0 == startingDirection:
            return 'A - North'
         return 'B - Sourth'

     def ConvertToDBSweepDirection(self, sweepDirection) -> int:
         if 'To the left' == sweepDirection:
            return 0
         return 1

     def ConvertToUISweepDirection(self, sweepDirection) -> str:
         if 0 == sweepDirection:
            return 'To the left'
         return 'To the right'