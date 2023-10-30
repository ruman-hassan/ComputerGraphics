import pandas as pd
# First DataFrame
df1 = pd.DataFrame({
      'Student Admission No.': ['192098', '156789'],
       'Student Name': [ 'John Doe Hurt', 'Susan Muhia Wanja' ],
       'Date of Birth': ['2003', '2004']})
 
# Second DataFrame
df2 = pd.DataFrame({
      'Student Admission No.': ['192099', '156745'],
       'Student Name': [ 'Clara Ravis', 'Tom Denton James' ],
       'Date of Birth': ['2007', '2006']})
 
 
frames = [df1, df2]
 
result = pd.concat(frames)
result.to_excel("trial3.xlsx")