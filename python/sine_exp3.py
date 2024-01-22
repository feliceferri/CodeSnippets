import math
from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd
import os

# Sales Projected
# number_of_entries = 24
# max = 15000
# zero_start_tail_size = 8
# zero_end_tail_size = 0
# starting_date = date(2022,1,1)

# Sales Actual
# number_of_entries = 24
# max = 12000
# zero_start_tail_size = 10
# zero_end_tail_size = 0
# starting_date = date(2022,1,1)

# Expenses Projected 
# number_of_entries = 24
# max = 5000
# zero_start_tail_size = 0
# zero_end_tail_size = 0
# starting_date = date(2022,1,1)

# Expenses Actual
number_of_entries = 24
max = 4000
zero_start_tail_size = 2
zero_end_tail_size = 0
starting_date = date(2022,1,1)

curve = []
dates = []
for i in range(0, number_of_entries + 1):
    x = (i -zero_start_tail_size)  / (number_of_entries - zero_start_tail_size - zero_end_tail_size)
    
    if((i <= zero_start_tail_size) or (number_of_entries - i <= zero_end_tail_size) ):
        y = 0
    else:
        y = round((math.sin(x * math.pi) ** 3) * max)
    
    curve.append(y)
    dates.append(starting_date +  relativedelta(months=i))

print(curve)
print('')

df = pd.DataFrame({'x': dates, 'y': curve})
df.to_csv(os.path.basename(__file__) + '.csv', index=False)
print(df)