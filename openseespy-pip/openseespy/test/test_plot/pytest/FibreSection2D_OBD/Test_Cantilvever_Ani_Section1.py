import openseespy.opensees as op
import openseespy.postprocessing.Get_Rendering as opp
import numpy as np
import matplotlib.pyplot as plt

import ModelFunctions as mf
import AnalysisFunctions as af
import MainAnalysis as main

def test_animate_fiberResponse2D_Section1(monkeypatch):
    # repress the show plot attribute
    monkeypatch.setattr(plt, 'show', lambda: None)
    
    main.RunAnalysis()    
       
    op.wipe()
    
    Model = 'test'
    LoadCase = 'Pushover'
    element1 = 1
    section1 = 1
    
    ani1 = opp.animate_fiberResponse2D(Model, LoadCase, element1, section1, InputType = 'stress', rFactor = 4)
    plt.close()
    assert True == True