import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

inputReader = data.splitlines()
inputReader = [item.split(', ') for item in inputReader]
cols = inputReader[0]
rows = inputReader[1::]
df = pd.DataFrame(rows, columns=cols)
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#Calculate mean consumption
print('Mean consumption of Alcohol and Tobacco are: %s, %s' %(df['Alcohol'].mean(), df['Tobacco'].mean()))

#Calculate median
print('Median consumption of Alcohol and Tobacco are: %s, %s' %(df['Alcohol'].median(), df['Tobacco'].median()))

#Standard Deviation
print('Standard deviation of Alcohol and Tobacco consumption are: %s, %s' %(df['Alcohol'].std(), df['Tobacco'].std()))