import pandas as pd
import warnings
warnings.simplefilter('ignore')


cases = {4: [[30.,100.,1],[100.,133.,0],[133.,190.,-1],[190.,200.,0],[200.,220.,-1],[220.,239.,0],[239.,255.,1],[255.,265.,-1],[265.,292.,1]],
         5: [[30.,100.,1],[100.,133.,0],[133.,190.,-1],[190.,200.,0],[200.,220.,-1],[220.,239.,0],[239.,255.,1],[255.,265.,-1],[265.,292.,1],[292,296.,0],[296.,297.,-1]]}

case_id = 5
df = pd.DataFrame(cases[case_id], columns=['start','end','is_insert'])
print(df, end='\n\n')

first_frame_pull = df[df['is_insert']==-1].index[0]
df = df[df['is_insert']!=0]
df = df.loc[first_frame_pull:]

df_assign = pd.DataFrame(columns=['start','end','is_insert'])
for i, g in df.groupby([(df['is_insert'] != df['is_insert'].shift()).cumsum()]):
    start, end = g['start'].min(), g['end'].max()
    series_add = pd.Series([start, end, g['is_insert'].max()], index=df_assign.columns)
    df_assign = df_assign.append(series_add, ignore_index=True)

df_push = df_assign[df_assign['is_insert']==1].reset_index()
df_pull = df_assign[df_assign['is_insert']==-1].reset_index()

print(df_push, end='\n\n')
print(df_pull, end='\n\n')

df_is_insert = pd.merge(df_pull, df_push, left_index=True, right_index=True, how='left', suffixes=['_push', '_pull'])
df_is_insert = df_is_insert[['start_push','end_push','start_pull','end_pull']]
print(df_is_insert)

df_is_insert.to_csv('task175_case4.csv')