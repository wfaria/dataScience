def azureml_main(flightDataframe, airportDataframe):
    import pandas as pd
    
    retDataFrame = pd.merge(
        flightDataframe,
        airportDataframe,
        how='inner',
        left_on=['OriginAirportID'],
        right_on=['airport_id'])
        
    ### The last parameter add different suffixes for overlapping columns.
    retDataFrame = pd.merge(
        retDataFrame,
        airportDataframe,
        how='inner',
        left_on=['DestAirportID'],
        right_on=['airport_id'],
        suffixes=['Origin', 'Dest'])
        
    return retDataFrame