def azureml_main(flightdataframe):
    import pandas as pd
    
    ### Dropping any row which contains any NA value.
    return flightdataframe.dropna();
