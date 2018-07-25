def azureml_main(flightDataframe):
    import pandas as pd
    
    ### Replace all values on the following columns by 0.
    flightDataframe.DepDelay.fillna(value=0, inplace=True)
    flightDataframe.ArrDelay.fillna(value=0, inplace=True)
    
    return flightDataframe
