DAY 2

    import pandas as pd
    ipl=pd.read_csv("C:/Users/Dell/Downloads/IPL Matches 2008-2020.csv")
    ipl.head(10)
    ipl.tail(10)
    ipl.result_margin.mean()
    ipl.result_margin.median()
    ipl.result_margin.mode()
    ipl.result_margin.std()
    ipl.result_margin.var()
    import pandas as pd
    ipl=pd.read_csv("C:/Users/Dell/Downloads/IPL Matches 2008-2020.csv")
    ipl.head(10)
    ipl.tail(10)
    ipl.result_margin.median()
    ipl.result_margin.skew()
    ipl.result_margin.kurt()
    ipl.result_margin.hist()
    ipl.winner.value_counts()
    ipl.eliminator.value_counts()
    ipl.toss_winner.value_counts()
    ipl.venue.value_counts()    
    ipl.size
    ipl.columns
    ipl.shape
    ipl.team1.value_counts()
    ipl.team2.mode()
    ipl.drop('neutral_venue',axis=1)
    ipl1=ipl.drop('neutral_venue',axis=1)
    ipl1.columns
    ipl.drop('method',axis=1,inplace=True)
    ipl.columns
    ipl.winner.unique()
    ipl.winner.nunique()
    G_list=["pop corn","top raman","pedigree","perfume","tip pencil"]
    G_list[1]
    ipl.iloc[10,:]
    ipl.loc[:,'city']
    ipl.loc[2:,'city']
    wickets=ipl[ipl.result=='wickets']
    runs=ipl[ipl.result=='runs']
    ipl.result.unique()
    runs.result_margin.max()
    runs[runs.result_margin==146]
    runs.winner[runs.result_margin==runs.result_margin.max()]
    wickets.result_margin.max()
    runs[runs.result_margin.max==10]
    wickets.winner=[wickets.result_margin==wickets]
    runs[runs.result_margin.max==10]


