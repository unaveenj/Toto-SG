# Toto Singapore
<a href="https://ibb.co/DQ2Kgv3"><img src="https://i.ibb.co/RcwH4sL/Screenshot-2023-12-26-102747.png" alt="Screenshot-2023-12-26-102747" border="0"></a>
## Overview
This project analyzes lottery data from various outlets to assign a "Luckiness" index to each. The analysis is based on the frequency of Group 1 and Group 2 wins. The project includes a data scraping component to gather data and a data processing component to calculate Luckiness scores using the Z-score methodology. It also features a map visualizing the geographical distribution of outlets and their scores.

## Data Scraping
Data is scraped from "https://www.singaporepools.com.sg/en/product/Pages/toto_wo.aspx", providing information on Group 1 and Group 2 wins at different lottery outlets. This data is initially saved in a CSV file named `toto.csv`.

## Data Processing
The data processing involves calculating a Z-score based "Luckiness" index for each outlet based on its Group 1 and Group 2 win frequencies.

### Z-Score Based Luck Index
The Z-score standardizes the number of wins by converting them into a score that represents the number of standard deviations away from the mean wins. This approach provides a more refined measure of each outlet's performance relative to the average.

#### Steps:
1. **Calculate Mean and Standard Deviation:**
   - Determine the mean and standard deviation for Group 1 and Group 2 wins among all outlets.
   
2. **Calculate Z-Scores:**
   - For each outlet, calculate the Z-score for its Group 1 and Group 2 wins.

3. **Combine Z-Scores for Luckiness Index:**
   - Calculate an overall Luckiness Index for each outlet by averaging its Group 1 and Group 2 Z-scores.

### Interpreting Z-Scores
- A Z-score indicates how many standard deviations an element is from the mean.
- A Z-score of 0 means the value is exactly the average.
- A positive Z-score indicates the value is above the average, while a negative Z-score indicates it is below the average.
- The magnitude of the Z-score shows the degree of variation from the mean; larger absolute values signify more "unusual" or "extreme" results.

### Output
The final output is a CSV file, `toto3.csv`, containing the original data along with the Z-scores and calculated Luckiness Index for each outlet.

## Map Visualization
To view the geographical distribution of lottery outlets and their Luckiness indices, visit the interactive map at:
[![Toto Map](https://felt.com/map/Toto-Map-qZDghtiGQuO2JEZyKxkIND/embed)](https://felt.com/map/Toto-Map-qZDghtiGQuO2JEZyKxkIND?loc=1.34978,103.84148,12.25z&share=1)

This map visualizes each outlet's location along with its Luckiness index, offering a spatial perspective on the distribution of luck across outlets.

## Alternate Map
![Map](https://www.google.com/maps/d/edit?mid=1o3MQ8v-M1seCQn6H4SxzJzCBZSEQOM4&usp=sharing)
