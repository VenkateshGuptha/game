import streamlit as st
from hydralit import HydraHeadApp
from PIL import Image
import requests
import base64
import io
import json

class PuzzleMediumApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

     def run(self):
         column_left, column_right = st.columns(2)
         column_left.slider("Direction", 0, 360, 10)

         column_right.title('Block details')
         ''' column_right.caption('Block 1 :')
         block1_order = column_right.number_input('Order', key='Block1Order', min_value=1, max_value=3, step=1, value=1)
         block1_direction = column_right.radio('Start point', ('A', 'B', 'C', 'D'), key='Block1Direction')
         
         column_right.caption('Block 2 :')
         block2_order = column_right.number_input('Order', key='Block2Order', min_value=1, max_value=3, step=1, value=2)
         block2_direction = column_right.radio('Start point', ('A', 'B', 'C', 'D'), key='Block2Direction')
         
         column_right.caption('Block 3 :')
         block3_order = column_right.number_input('Order', key='Block3Order', min_value=1, max_value=3, step=1, value=3)
         block3_direction = column_right.radio('Start point', ('A', 'B', 'C', 'D'), key='Block3Direction') '''

         self.addBlocksInUI(column_right, 1, 1, 3, 1, 1)
         self.addBlocksInUI(column_right, 2, 1, 3, 2, 2)
         self.addBlocksInUI(column_right, 3, 1, 3, 3, 2)

         if column_right.button('Submit'):
             st.text(str(st.session_state.Block1Order) + st.session_state.Block1Direction)
             st.text(str(st.session_state.Block2Order) + st.session_state.Block2Direction)
             st.text(str(st.session_state.Block3Order) + st.session_state.Block3Direction)

             #resp = requests.get("https://loopr-linux-pylattice-dev.azurewebsites.net/")
             #st.text(resp.text)

             headers = {'Content-type':'application/json'}
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
             resp = requests.post(st.secrets["stage2"], data=json.dumps(payload), headers=headers)
             output = json.loads(resp.text)
             buf = io.BytesIO(base64.b64decode(output['outputs']['Stage2']['base64Image']))
             image = Image.open(buf)
             column_left.image(image, use_column_width=True)


     def addBlocksInUI(self, column, blockNo, minValue, maxValue, orderNo, direction):
         blocknumber = 'Block' + str(blockNo)
         blockorder = 'Block' + str(blockNo) + 'Order'
         blockdirection = 'Block' + str(blockNo) + 'Direction'

         column.caption(blocknumber + ' :')
         column.number_input('Order', key=blockorder, min_value=minValue, max_value=maxValue, step=1, value=orderNo)
         column.radio('Start point', ('A', 'B', 'C', 'D'), key=blockdirection, index=direction)