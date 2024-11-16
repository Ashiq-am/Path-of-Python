import pandas as pd


dataFrame1 = pd.DataFrame([['PQR', 'B1'], ['QRS', 'B2'], ['RDE', 'B3']],
						columns=['work_name', 'tag_name'])

dataFrame2 = pd.DataFrame([['RR', 'T1'], ['QR', 'T2'], ['HG', 'T3'],
						['PQ', 'T4']],
						columns=['sub_work_name', 'extra_tag_value'])

dataFrame1['join'] = 1
dataFrame2['join'] = 1

dataFrameFull = dataFrame1.merge(
dataFrame2, on='join').drop('join', axis=1)

dataFrame2.drop('join', axis=1, inplace=True)

dataFrameFull['match'] = dataFrameFull.apply(
	lambda x: x.work_name.find(x.sub_work_name), axis=1).ge(0)

print(dataFrameFull[dataFrameFull['match']])
