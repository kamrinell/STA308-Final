# STA308-Final
Rstudio and Python code for sta308 final project
Flu and Pneumonia mortality rates from 2018 and 2021

#Table of R and Python Values Found
| Region    | R.mean diff | R.std     | R.cv      | Py.mean diff |            Py.std |               Py.cv |  
|-----------|-------------|-----------|-----------|--------------|-------------------|---------------------|
| Midwest   |    35.72255 |  8.918304 | 0.2496548 |    35.722550 |         0.2871966 | 0.24965475137565343 | 
| Northeast |    38.52745 | 12.432945 | 0.3227036 |    38.527446 | 8.918304293133854 | 0.3227035959622255  |
| South     |    24.86342 |  7.140688 | 0.2871966 |    24.863418 | 12.43294539873221 | 0.2871965704985935  | 
| West      |    34.87706 | 12.928896 | 0.3706991 |    34.877063 | 7.140688471824783 | 0.3706991103474302  | 

##Compare and Contrast Percent Difference and Variation between Regions
The Coefficient of Variation(CV) is the ratio of the standard deviation/mean. It determines the variability across
the mean meaning a lower CV is better data as the data is less dispersed.

The CV for each Region is fairly high meaning its spread is fairly large and likely dip into each other. However, 
while the Midwest and West have similar average means in differation they varuiation is very different as the Midwest
has a much lower CV of ~.25 while the West has ~.37. The South also has a very different mean compared to the other
regions as it has the smallest one at ~25 while its cv is in the middle of the other regions. The Northeast has the 
most similar average and cv to all the other regions. Slightly higher than the other averages and right in the middle
of the West and South cv at ~.32.

#Table of Functionality Between R and Python
| Functionality                               | In R               | In Python                   |
|---------------------------------------------|--------------------|-----------------------------|
| Calculating New Columns in Dataframe        | mutate()           | assign()                    |
| Sums up all grouped data                    | summarize()        | agg()                       |
| Merges by selected same column names        | by =               | on =                        |

#My Favorite Topic
My favorite topic was using Python to create interlooping functions. I enjoyed the methodology of how to get from
logic to logic and how within the loops you would need other conditions with a conditioned loop. Specifically
with Python because it was easier for me to think using its language.
