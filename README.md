# surfs_up

# 1. Overview of the statistical analysis:
  - The purpose of this analysis was to help identify weather trends (Precipitation and Temperature) on the island of Oahu in Hawaii. This analysis is going to help us determine if the surf and ice cream shop will be able to survive throughout the entire year. To conduct the analysis, I used my knowledge of SQLAlchemy, Python, Pandas, and Numpy to write the code needed to find the data I was looking for. 

## 2. Results:
  - three key differences in the data betwee June and December:
    - the average temperature was 3 degrees higher in June (74.94 degrees) vs. December (71.04 degrees)
    - The maximum temperature in each month did not vary too much. June has a high of 85 degrees and December has a high of 83 degrees. 
    - However, the minimum temperature varies pretty drastically. June saw a low temp of 64 degrees whereas December saw a low temp of 56 degrees.

    ### June Temperature Statistics
    
    ![image](https://user-images.githubusercontent.com/84791455/129425102-1033af67-6913-4b1a-8e61-4e6ae3189ad9.png)


    ### December Temperature Statistics
    
    ![image](https://user-images.githubusercontent.com/84791455/129425130-db0f7e11-995a-4e44-b37c-dd0df3138f69.png)


## 3. Summary:
  - High Level Summary:
    - Overall, our temperature analysis shows it is likely a viable option to run the surf and ice cream shop year round. Although it can reach low temperatures in December, the average temperature is still above 70 degrees, which is perfectly fine temperatures for surfing and eating ice cream. However, it will be likely sales will be higher in June because there is more consistent warmer weather. 
  - Two other additional queries that can be performed to gather more weather data
    - We could also query the precipitation data to identify if June or Decmber has more days of the year where it is raining. There may be warm temperatures year round but if the precipiation is too much in the winter months, it can be harmful towards the total sale #'s
    - Another way to look at the data would be the location of the stations. We can get more granular temperature and precipitation data if we were to look individually at each station. This can better help us pinpoint the exact location to open up the surf and ice cream shop. 
