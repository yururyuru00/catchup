import numpy as np
import pandas as pd

case_id = 2
df_frame = pd.read_csv('task175_case{}.csv'.format(case_id))

fs, fe = df_frame['start_push'].min(), max(df_frame['end_push'].max(), df_frame['end_pull'].max())
print(fs, fe)

frames = np.arange(fs, fe+1)
tawamis = np.random.choice(a=[False, True], size=len(frames))
df_is_tawami = pd.DataFrame({'frame':frames, 'is_tawami':tawamis})
print(df_is_tawami.columns)

df_assign = pd.merge(df_frame, df_is_tawami, how='left', left_on='end_push', right_on='frame')
df_frame_tawami = pd.merge(df_frame, df_assign, how='left', left_on='end_push', right_on='frame')
print(df_frame_tawami)