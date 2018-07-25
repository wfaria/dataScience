def azureml_main(flightDataframe):
    import pandas as pd
    
    uniqueIdColumns = ['Year', 'Month',
        'DayofMonth', 'Carrier', 'OriginAirportID',
        'DestAirportID', 'CRSDepTime', 'CRSArrTime']
    return flightDataframe.drop_duplicates(subset=uniqueIdColumns)
