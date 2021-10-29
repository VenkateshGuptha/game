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
                -0.009382,
                -0.018078
              ],
              [
                -8.815636,
                -0.796736
              ],
              [
                -17.408833,
                -0.129287
              ],
              [
                -24.368607,
                1.42807
              ],
              [
                -31.54142,
                4.431528
              ],
              [
                -38.217083,
                9.659749
              ],
              [
                -42.975258,
                13.886823
              ],
              [
                -51.00021,
                22.229729
              ],
              [
                -61.013576,
                35.244659
              ],
              [
                -69.89064,
                46.257313
              ],
              [
                -82.034424,
                60.162212
              ],
              [
                -91.550575,
                70.285011
              ],
              [
                -99.646378,
                78.739235
              ],
              [
                -112.07412,
                90.530693
              ],
              [
                -120.596008,
                96.982674
              ],
              [
                -128.620773,
                102.878464
              ],
              [
                -144.244156,
                114.002655
              ],
              [
                -166.47197,
                126.461945
              ],
              [
                -198.996841,
                144.261124
              ],
              [
                -212.702698,
                151.047165
              ],
              [
                -226.834579,
                158.500687
              ],
              [
                -249.985275,
                169.736755
              ],
              [
                -265.750488,
                176.189316
              ],
              [
                -275.266327,
                181.084274
              ],
              [
                -279.101044,
                183.531708
              ],
              [
                -281.586456,
                186.090302
              ],
              [
                -283.219666,
                189.093811
              ],
              [
                -284.568756,
                192.987213
              ],
              [
                -286.911743,
                202.553802
              ],
              [
                -288.899628,
                212.565308
              ],
              [
                -290.248535,
                219.462128
              ],
              [
                -291.242432,
                225.357788
              ],
              [
                -292.023285,
                231.253433
              ],
              [
                -293.300995,
                241.042435
              ],
              [
                -294.933319,
                259.39679
              ],
              [
                -300.256592,
                308.897919
              ],
              [
                -301.888946,
                325.694916
              ],
              [
                -301.959717,
                330.033203
              ],
              [
                -301.178497,
                331.479248
              ],
              [
                -299.687103,
                333.258972
              ],
              [
                -296.633453,
                334.593658
              ],
              [
                -282.714691,
                335.705261
              ],
              [
                -286.405762,
                366.184662
              ],
              [
                -296.98169,
                455.842957
              ],
              [
                -298.11731,
                465.965668
              ],
              [
                -298.259186,
                468.412903
              ],
              [
                -297.761993,
                470.526398
              ],
              [
                -295.844543,
                472.862305
              ],
              [
                -292.293884,
                474.085724
              ],
              [
                -286.967957,
                474.975311
              ],
              [
                -275.890045,
                476.087097
              ],
              [
                -262.255707,
                477.866211
              ],
              [
                -232.85672,
                480.979492
              ],
              [
                -233.921234,
                495.885437
              ],
              [
                -237.186188,
                530.81427
              ],
              [
                -240.947998,
                569.636475
              ],
              [
                -241.30275,
                576.088257
              ],
              [
                -241.018585,
                578.757996
              ],
              [
                -239.456284,
                580.648926
              ],
              [
                -236.828827,
                582.09491
              ],
              [
                -234.272446,
                582.317261
              ],
              [
                -230.437882,
                582.428345
              ],
              [
                -224.046951,
                582.650574
              ],
              [
                -213.96344,
                583.540039
              ],
              [
                -203.24086,
                584.429504
              ],
              [
                -194.222473,
                586.320252
              ],
              [
                -185.133057,
                589.10083
              ],
              [
                -178.315994,
                591.659058
              ],
              [
                -173.3452,
                594.328613
              ],
              [
                -167.948334,
                597.109375
              ],
              [
                -161.699326,
                600.780029
              ],
              [
                -158.787857,
                602.671021
              ],
              [
                -155.379349,
                603.560791
              ],
              [
                -152.894043,
                602.003418
              ],
              [
                -151.615936,
                599.556152
              ],
              [
                -150.692902,
                596.107727
              ],
              [
                -147.852905,
                581.201782
              ],
              [
                -146.716873,
                576.529785
              ],
              [
                -145.935867,
                572.858887
              ],
              [
                -143.663605,
                569.966614
              ],
              [
                -140.255112,
                569.521606
              ],
              [
                -132.017868,
                570.411316
              ],
              [
                -115.046326,
                572.301941
              ],
              [
                -110.50164,
                573.191711
              ],
              [
                -107.093109,
                574.52655
              ],
              [
                -104.394684,
                576.083801
              ],
              [
                -101.128166,
                578.085998
              ],
              [
                -87.777985,
                592.101746
              ],
              [
                -84.085403,
                594.993897
              ],
              [
                -79.895775,
                596.884888
              ],
              [
                -72.297676,
                598.330872
              ],
              [
                -65.764755,
                597.552063
              ],
              [
                -59.30286,
                595.216003
              ],
              [
                -53.196018,
                591.878845
              ],
              [
                -46.308067,
                587.651733
              ],
              [
                -32.81617,
                579.308777
              ],
              [
                -19.253218,
                571.96698
              ],
              [
                -9.950854,
                567.962402
              ],
              [
                -2.068687,
                565.292664
              ],
              [
                3.967211,
                563.735352
              ],
              [
                11.281303,
                562.622986
              ],
              [
                19.447525,
                561.51062
              ],
              [
                28.110821,
                561.065735
              ],
              [
                38.904438,
                560.509582
              ],
              [
                43.662155,
                559.730957
              ],
              [
                46.573605,
                558.284912
              ],
              [
                48.348904,
                554.725281
              ],
              [
                49.41412,
                548.607239
              ],
              [
                45.295902,
                501.108612
              ],
              [
                42.100735,
                457.837067
              ],
              [
                41.603691,
                452.83136
              ],
              [
                44.089592,
                395.432617
              ],
              [
                83.998901,
                389.537506
              ],
              [
                108.356544,
                379.52652
              ],
              [
                171.133453,
                337.146576
              ],
              [
                184.908722,
                376.302765
              ],
              [
                185.689499,
                386.981628
              ],
              [
                121.847755,
                434.478333
              ],
              [
                119.078095,
                442.37616
              ],
              [
                111.47937,
                462.176331
              ],
              [
                100.400886,
                494.546356
              ],
              [
                96.281998,
                507.004913
              ],
              [
                92.660248,
                516.793762
              ],
              [
                83.641457,
                539.597412
              ],
              [
                80.800903,
                547.606506
              ],
              [
                81.013931,
                547.606506
              ],
              [
                79.948723,
                551.054871
              ],
              [
                79.593628,
                553.390808
              ],
              [
                79.451576,
                555.393127
              ],
              [
                80.232666,
                557.506653
              ],
              [
                81.652855,
                559.175232
              ],
              [
                83.499107,
                560.510132
              ],
              [
                86.339516,
                561.511291
              ],
              [
                89.03791,
                562.067566
              ],
              [
                91.80732,
                562.290039
              ],
              [
                96.351997,
                562.067688
              ],
              [
                100.541626,
                562.067749
              ],
              [
                104.731255,
                561.734131
              ],
              [
                127.099632,
                560.177307
              ],
              [
                187.245743,
                556.953186
              ],
              [
                266.635956,
                551.172241
              ],
              [
                350.357971,
                546.171387
              ],
              [
                367.897736,
                544.837769
              ],
              [
                369.247681,
                534.270264
              ],
              [
                369.745331,
                526.149902
              ],
              [
                371.949707,
                482.87851
              ],
              [
                372.589447,
                474.201996
              ],
              [
                373.157745,
                471.198639
              ],
              [
                389.916107,
                476.984222
              ],
              [
                408.236542,
                484.661011
              ],
              [
                424.994659,
                492.560211
              ],
              [
                455.528259,
                508.136078
              ],
              [
                467.031738,
                512.364136
              ],
              [
                478.251312,
                514.478638
              ],
              [
                493.163574,
                515.703613
              ],
              [
                505.51947,
                516.14978
              ],
              [
                519.011536,
                516.596008
              ],
              [
                530.586365,
                516.819641
              ],
              [
                548.907227,
                517.377685
              ],
              [
                560.907959,
                518.491333
              ],
              [
                587.679077,
                519.717896
              ],
              [
                600.886963,
                520.942993
              ],
              [
                608.130127,
                520.832581
              ],
              [
                618.426697,
                521.167481
              ],
              [
                626.948059,
                521.168518
              ],
              [
                633.055054,
                520.83551
              ],
              [
                637.528992,
                518.945007
              ],
              [
                638.665527,
                515.941711
              ],
              [
                638.310852,
                513.0495
              ],
              [
                633.482544,
                509.155579
              ],
              [
                626.239929,
                504.7052
              ],
              [
                616.015259,
                495.916199
              ],
              [
                604.086731,
                483.67865
              ],
              [
                592.655273,
                471.329956
              ],
              [
                583.779968,
                460.872589
              ],
              [
                517.320252,
                384.222778
              ],
              [
                506.669403,
                372.875488
              ],
              [
                499.071655,
                365.86676
              ],
              [
                491.331787,
                359.859192
              ],
              [
                467.117462,
                346.063507
              ],
              [
                451.779236,
                338.05304
              ],
              [
                440.843628,
                332.045258
              ],
              [
                420.818573,
                321.92099
              ],
              [
                412.29718,
                318.694428
              ],
              [
                406.048035,
                317.581543
              ],
              [
                401.716156,
                318.026184
              ],
              [
                397.668274,
                319.360718
              ],
              [
                391.631928,
                321.696258
              ],
              [
                386.731781,
                323.920654
              ],
              [
                382.04483,
                324.810211
              ],
              [
                378.494171,
                324.253784
              ],
              [
                374.87262,
                322.028748
              ],
              [
                371.961395,
                317.022858
              ],
              [
                370.186462,
                311.460846
              ],
              [
                368.056427,
                305.898804
              ],
              [
                365.07431,
                299.113068
              ],
              [
                360.742798,
                293.884613
              ],
              [
                355.417114,
                288.211121
              ],
              [
                348.671112,
                282.76001
              ],
              [
                340.788849,
                277.753784
              ],
              [
                311.957947,
                261.622498
              ],
              [
                276.30957,
                242.821335
              ],
              [
                263.81134,
                234.811569
              ],
              [
                251.45517,
                226.023178
              ],
              [
                239.454025,
                216.678635
              ],
              [
                227.452896,
                206.332977
              ],
              [
                217.014023,
                197.099808
              ],
              [
                116.387176,
                100.31971
              ],
              [
                76.47628,
                62.053173
              ],
              [
                38.340244,
                25.233044
              ],
              [
                31.806644,
                18.336256
              ],
              [
                24.633861,
                12.774327
              ],
              [
                18.88142,
                8.102315
              ],
              [
                12.276751,
                4.097735
              ],
              [
                6.879377,
                1.650493
              ],
              [
                -0.009382,
                -0.018078
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
            247.0,
            548.0
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
            47.0,
            30.0
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
        "fDirection_deg": 93.9091567993164,
        "fShift_m": 24.2939453125,
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
          "1:1",
          "1:2",
          "1:3"
        ],
              "directionOverrides_experimental" : {
                  "1:1" : {
                      "sSweepDirection_experimental": "ToTheLeft",
                      "sStartingDirection_experimental": "AB"
                  },	
                  "1:2" : {
                      "sSweepDirection_experimental": "ToTheLeft",
                      "sStartingDirection_experimental": "AB"
                  },	
                  "1:3" : {
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

st.session_state['hard_puzzle_image'] = Image.open('resources/puzzle-medium.png')
headers = {'Content-type':'application/json'}
st.session_state['row_direction'] = 90

class PuzzleHardApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

     def run(self):
         column_left, column_right = st.columns(2)
         self.image_placeholder = column_left.empty()
         self.image_placeholder.image(st.session_state['hard_puzzle_image'], use_column_width=True)

         btnRedraw = column_right.button('Redraw')
         # Default values
         column_right.title('Block details')
         self.addBlocksInUI(column_right, 1, 1, 3, 1, 0, 0)
         self.addBlocksInUI(column_right, 2, 1, 3, 2, 0, 0)
         self.addBlocksInUI(column_right, 3, 1, 3, 3, 0, 0)

         if column_right.button('Submit'):
             payload = self.GetPayload()
             if payload is None:
                 return

             resp = requests.post(st.secrets["stage4"], data=json.dumps(payload), headers=headers)
             output = json.loads(resp.text)
             image = ConvertToImage(output['outputs']['Stage4']['base64Image'])
             st.session_state['hard_puzzle_image'] = image;
             self.image_placeholder.image(image, use_column_width=True)

             results = output['outputs']['Stage4']['report']
             self.SaveResults(results)
             DisplayResults(column_left, results)

         if btnRedraw:
             payload = self.GetPayload()
             if payload is None:
                 return

             resp = requests.post(st.secrets["stage2"], data=json.dumps(payload), headers=headers)
             output = json.loads(resp.text)

             image = ConvertToImage(output['outputs']['Stage2']['base64Image'])
             st.session_state['hard_puzzle_image'] = image;
             self.image_placeholder.image(image, use_column_width=True)

     def GetPayload(self):
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
            return None
             
         directions = []
         for i in range(1, 4):
            if(Block1Order == i):
                directions.append('1:' + str(1))
                
            if(Block2Order == i):
                directions.append('1:' + str(2))
                    
            if(Block3Order == i):
                directions.append('1:' + str(3))
             
         Block1Directions = {'sSweepDirection_experimental' : GetSweepDirection(Block1SweepDirection), 'sStartingDirection_experimental': GetStartingDirection(Block1StartDirection)}
         Block2Directions = {'sSweepDirection_experimental' : GetSweepDirection(Block2SweepDirection), 'sStartingDirection_experimental': GetStartingDirection(Block2StartDirection)}
         Block3Directions = {'sSweepDirection_experimental' : GetSweepDirection(Block3SweepDirection), 'sStartingDirection_experimental': GetStartingDirection(Block3StartDirection)}

         payload['inputsStage2']['blocks']['manualOrder'] = directions
         payload['inputsStage2']['blocks']['directionOverrides_experimental'] = {'1:1':Block1Directions, '1:2':Block2Directions, '1:3':Block3Directions}
         return payload

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
         block2 = {'blockno':2, 'orderno':st.session_state.Block2Order, 'startdirection':ConvertToDBStartDirection(st.session_state.Block2StartDirection), 'sweepdirection':ConvertToDBSweepDirection(st.session_state.Block2SweepDirection)}
         block3 = {'blockno':3, 'orderno':st.session_state.Block3Order, 'startdirection':ConvertToDBStartDirection(st.session_state.Block3StartDirection), 'sweepdirection':ConvertToDBSweepDirection(st.session_state.Block3SweepDirection)}

         results = {'userid': self.session_state.UserID, 'blocks':[block1, block2, block3], 'puzzlenumber':3, 'infilldistance':report['fInfillDistance_m'], 'totaldistance':report['fTotalDistance_m'], 'transitdistance':report['fTransitDistance_m']}
         client = MongoClient(st.secrets["url"])
         db = client.Game
         my_collections = db.PuzzleResults
         x = my_collections.insert_one(results)