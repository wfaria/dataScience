# Basic boxplot of a single column.
### Magic line to make plots appear on notebook
%matplotlib inline

def boxplot(df,col):
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(9, 6))
    ax = fig.gca()
    df.boxplot(column = col, ax = ax)
    ax.set_title('Box plot of ' + col)
    ax.set_ylabel(col)
    return col

boxplot(flightDataframe, "ArrDelay")
    
# Basic histogram of a single column.
def histplot(df,col):
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(9, 4))
    ax = fig.gca()
    df.hist(column = col, ax = ax, bins = 30)
    ax.set_title('Histogram of ' + col)
    return col
    
histplot(flightDataframe, "ArrDelay")

# Histogram by groups
def groupedhistplot (df, col, groupcol):
    import matplotlib.pyplot as plt
    #Use sharey to make it easier to compare different histograms side-by-side.
    df.hist(column = col, sharey = True, by = groupcol, bins = 30, figsize = [9,4])
    plt.suptitle('Histogram of ' + col + ' grouped by ' + groupcol)
    return

groupedhistplot(flightDataframe, 'DepDelay', 'ArrDel15')
groupedhistplot(flightDataframe, 'CRSArrTime', 'ArrDel15')
groupedhistplot(flightDataframe, 'CRSDepTime', 'ArrDel15')
groupedhistplot(flightDataframe, 'DayofMonth', 'ArrDel15')
groupedhistplot(flightDataframe, 'DayOfWeek', 'ArrDel15')
groupedhistplot(flightDataframe, 'Month', 'ArrDel15')

# Grouped pair plots by groups.
def grouppairplot(df, cols, groupcol):
    import seaborn as sns
    sns.pairplot(data=df, vars=cols, hue = groupcol, size = 2)

pairplotcols = ['DepDelay', 'CRSArrTime', 'CRSDepTime',
            'DayofMonth', 'DayOfWeek', 'Month']
grouppairplot(flightDataframe, pairplotcols, 'ArrDel15')

# Grouped scatter plot by group.
def scatterplot(df, xcol, ycol, groupcol):
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(8, 8))
    ax = fig.gca()
    tempDf0 = df.loc[df[groupcol] == 0]
    tempDf1 = df.loc[df[groupcol] == 1]
    if tempDf0.shape[0] > 0:                    
        tempDf0.plot(kind = 'scatter', x = xcol, y = ycol, 
                   ax = ax, color = 'DarkBlue')                          
    if tempDf1.shape[0] > 0:                    
        tempDf1.plot(kind = 'scatter', x = xcol, y = ycol,
                       ax = ax, color = 'Red')
    ax.set_title('Scatter plot of ' + xcol + ' vs. ' + ycol)
    return
    
scatterplot(flightDataframe, 'ArrDelay', 'Month', 'ArrDel15')
