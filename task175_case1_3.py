from distutils.command.build_scripts import first_line_re
import pandas as pd


cases = {1: [[30.,100.,1],[101.,140.,-1],[189.,193.,1],[232.,290.,-1]],
         2: [[30.,100.,1],[101.,140.,-1],[189.,193.,1]] ,
         3: []}

case_id = 1
df = pd.DataFrame(cases[case_id], columns=['start','end','is_insert'])
print(df, end='\n\n')

first_frame_pull = df[df['is_insert']==-1].index[0]
df = df.loc[first_frame_pull:]

df_push = df[df['is_insert']==1].reset_index()
df_pull = df[df['is_insert']==-1].reset_index()

print(df_push, end='\n\n')
print(df_pull, end='\n\n')

df_is_insert = pd.merge(df_pull, df_push, left_index=True, right_index=True, how='left', suffixes=['_push', '_pull'])
df_is_insert = df_is_insert[['start_push','end_push','start_pull','end_pull']]
print(df_is_insert)

df_is_insert.to_csv('task175_case{}.csv'.format(case_id))