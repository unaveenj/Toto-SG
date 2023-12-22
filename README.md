# Toto-SG

## Overview
This project analyzes lottery data from various outlets to assign a "Luckiness" score to each. The analysis is based on the frequency of Group 1 and Group 2 wins. The project includes a data scraping component to gather data and a data processing component to calculate Luckiness scores. It also features a map visualizing the geographical distribution of outlets and their scores.

## Data Scraping
Data is scraped from "https://www.singaporepools.com.sg/en/product/Pages/toto_wo.aspx", providing information on Group 1 and Group 2 wins at different lottery outlets. This data is initially saved in a CSV file named `toto.csv`.

## Data Processing
The data processing involves calculating a percentile-based "Luckiness" score for each outlet based on its Group 1 and Group 2 win frequencies.

### Percentile-Based Scoring Method
Instead of normalizing based on the maximum wins, the Luckiness score is calculated based on percentile ranks. This approach ranks each outlet's win frequencies among all outlets and uses these ranks to assign scores.

#### Steps:
1. **Calculate Percentile Ranks:**
   - Determine the percentile rank for each outlet's Group 1 and Group 2 wins among all outlets.
   
2. **Average Percentile Ranks:**
   - Calculate the average of the percentile ranks for Group 1 and Group 2 wins for each outlet.

3. **Scale to 0-10 Range:**
   - Scale the average percentile rank to a 0-10 range for the Luckiness score.

The percentile-based scoring provides a more evenly distributed measure of luckiness across outlets compared to the max normalization technique.

## Output
The final output is a CSV file, `toto2.csv`, containing the original data along with the normalized win frequencies and calculated Luckiness scores for each outlet.

## Map Visualization
To view the geographical distribution of lottery outlets and their Luckiness scores, visit the interactive map at:
[![Toto Map](https://felt.com/map/Toto-Map-qZDghtiGQuO2JEZyKxkIND/embed)](https://felt.com/map/Toto-Map-qZDghtiGQuO2JEZyKxkIND?loc=1.34978,103.84148,12.25z&share=1)

This map visualizes each outlet's location along with its Luckiness score, offering a spatial perspective on the distribution of luck across outlets.
