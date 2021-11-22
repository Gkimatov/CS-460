# CS-460

# Project Title

### Group Members
- Greg Kimatov
- Zeal Patel
- Mehedi Shohag

### Repository Structure
List each file and what it's purpose it. Make sure you indicate where your data cleaning code and data dictionary are! 

For example:
- `data`
  - `raw_twitter.csv`: Raw data from the Twitter API
  - `raw_census.csv`: Raw data from the Census API
  - `cleaned.csv`: The cleaned and combined dataset for modeling. 
  - `data_dictionary.csv`: The data dictionary for cleaned. 
- `code`
  - `etl_twitter.py`: Cleans `raw_twitter.csv`
  - `etl_census`: Cleans `raw_census.csv`
  - `exploratory_data_analysis.ipynb`: Includes descriptive statistics and charts. 
  - `build_model.py`: Builds Logistic Regression model. 


### Exploratory Analysis
Describe what work you have done so far and include the code. 

**Visualization #1 (Bar Chart):** We looked at the arrest count by year in NYC. The peak arrest count occurred in 2011, while the lowest point was in 2019, the last year in the dataset. Overall, we found that the number of arrests trended downwards in the last 10 years. 

**Visualization #2 (Grouped Bar Chart):** Here, we looked at the arrest count per year by borough. In every year from 2006 to 2019, we see that the arrest count is highest in Brooklyn, followed by Manhattan, Bronx, Queens, and Staten Island. 

**Visualization #3 (Grouped Bar Chart):** Here, we looked at the arrest count by borough and offense level. The most common offense level is misdemeanor, followed by felony, violation, and infraction. 

**Visualization #4 (Grouped Bar Chart):** Here, we looked at the arrest count per year by the sex of the perpetrator. Consistently, throughout the 14-year time period, males committed significantly more crimes than females.

**Visualization #5 (Grouped Bar Chart):** Here, we looked at the arrest count per year by the age range of the perpetrator. Throughout the 14-year time period, 25-44 is the most common age group the age of perpetrators fell in, followed by 18-24, 45-64, <18, and 65+.
**Pie Chart Visualizations:** The pie chart visualizations show the top 10 crimes committed in all of NYC as well as specific boroughs like Queens, Manhattan, Brooklyn, Bronx, and Staten Island. In all the boroughs, “dangerous drugs” and “assault 3 & related offenses” consistently made it into the top 3 offenses. The exact proportion of the overall crime that was, for example, “dangerous drugs” in a specific borough can be viewed in the nested pie chart. The issues we have been having with the nested pie chart are described in the notebook as well as the “Challenges” section of this analysis.


### Challenges
Describe any challenges you've encountered so far. Let me know if there's anything you need help with!

The biggest challenge for us is to find a way to visualize the data such that it is detailed enough but not too detailed that it becomes hard to follow. For example, we wanted to build a nested pie chart that would show the top 10 crimes in each borough. The issue is there are many possible top 10 offenses, so we don’t think a legend would be too helpful. The same color in 1 borough could present a different offense for another borough because the colors are determined by the offense's rank in the list of the top 10 offenses in the borough. 

Another challenge for us has been to show the arrest count per 100,000 people in a given borough in our data visualizations. We realized that showing the arrest count isn’t as useful as showing it relative to the population of an area, so we want to display the arrest count/100k people in a borough in our visualizations. We used the 2010 Census data to calculate this for 2011-2019. The following is the 2010 Census data for each borough. Manhattan: 1,585,873. Queens: 2,230,722. Brooklyn: 2,504,700. Bronx: 1,385,108. Staten Island: 468,730. NYC Total Population: 8,175,133. The formula for the arrest count per 100,000 people will look this: (# of arrests/borough population)*100,000. This is how the crime rate in an area is typically computed. We just need to figure out how to show the result of our computation in our visualizations instead of the arrest count.


### Future Work
Describe what work you are planning to complete for the final analysis.

For the final analysis, we are planning on doing more exploratory analysis by visualizing the offense levels and frequently-occurring offenses in a map view based on the borough. That will allow us to visualize what types of offenses are happening in which part of the city and will create clusters.  We will also calculate the crime rate based on each precinct, so we can get an idea about which area tends to be more violent. Finally, we plan to use the crime data over a recent 14-year time period to build a linear regression model that will allow us to predict the crime rate in NYC over the next decade.


### Contributions
Describe the contributions that each group member made.

