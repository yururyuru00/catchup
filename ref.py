import pandas as pd

list_df = pd.DataFrame( columns=['A','B'] )

for i in [0,1,2,3,4,5]:
    tmp_se = pd.Series( [ i, i*i ], index=list_df.columns )
    list_df = list_df.append( tmp_se, ignore_index=True )

print( list_df )