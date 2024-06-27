
# pip install pandas
# pip install pandas-profiling

import pandas as pd
from ydata_profiling import ProfileReport



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('InputCSVFile-housing.csv')

# Print the DataFrame to verify it has been loaded correctly
print(df)

# Generate the ProfileReport
profile = ProfileReport(df)
profile.to_file(output_file='OutputAnalysisFileHTML-housing')
