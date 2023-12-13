##STA308 Final ##
# Within the four census regions 
# computing percentage decrease of flu-pneumonia mortality
# the standard deviation
# and coefficient of variation
# from 2018-2021
##############################
library(tidyverse)
mortality_2018 = read_csv("https://tjfisher19.github.io/data/fluPneumonia_2018.csv")
mortality_2021 = read_csv("https://tjfisher19.github.io/data/fluPneumonia_2021.csv")
state_codes = read_csv("https://tjfisher19.github.io/data/state_abb_codes.csv")
census_regions = read_csv("https://tjfisher19.github.io/data/censusRegions.csv")

##mortality_2021 now has the state name code that matches 2018 and census regions set up##
mortality_2021 = merge(mortality_2021, state_codes)
mortality_2021 <- mortality_2021 %>% select('Rate','Code')
colnames(mortality_2021)[2] <- "State"

##drop Hawaii and Alaska##
mortality_2018 <- mortality_2018 %>% filter(State != "HI", State != "AK")
mortality_2021 <- mortality_2021 %>% filter(State != "HI", State != "AK")

mortality_compare <- merge(mortality_2018, mortality_2021, by = "State")
## Rate.x is 2018 Rate and Rate.y is 2021 Rate ##

mortality_compare <- merge(mortality_compare, census_regions, by = "State")

##calc percentage diff per state##
mortality_compare <- mortality_compare %>%
  mutate(Percentage = (Rate.x - Rate.y)/(Rate.x)*100)

##group_by Region ##
## find mean ## find sd ## calculate cv ##
mortality_all_data <- mortality_compare %>%
  group_by(Region)%>%
  summarize(mean_percent_diff = mean(Percentage),
            std = sd(Percentage))%>%
  mutate(cv = std/mean_percent_diff)

#print tibble #
mortality_all_data


