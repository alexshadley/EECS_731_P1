import pandas as pd

inc = pd.read_csv('incident_reports.csv')
ped = pd.read_csv('pedestrian_volume.csv')

# remove unhelpful IDs
del inc['Row ID']
del inc['Incident ID']
del inc['Incident Number']
del inc['CAD Number']

# produce a new column in ped that matches intersection format of inc
ped = ped.assign(
    Intersection=ped.apply(lambda x: x.ST_NAME1 + ' ' + x.ST_TYPE1 + ' \\ ' + x.ST_NAME2 + ' ' + x.ST_TYPE2, axis=1)
)

# merge both datasets across intersection
comb = pd.merge(inc, ped, on='Intersection')
