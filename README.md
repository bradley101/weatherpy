

# wepy 
python script for weather updates

### Overview
wepy is a Python distribution that helps getting weather updates of a place.

### Functions
Weather updates includes
 - Location info
 - Wind conditions
 - Sun settings
 - Atmosphere conditions
 - Weather conditions
 - Weather forecast (max 10 days)

### Prerequisites
Python 2.7.x
 
### Installation
```
sudo pip install -U wepy --no-cache-dir
```
### Usage
 - ```wepy -l [location]```
   
   ```
   $ wepy -l Washington
   City - Washington
   Region -  DC
   Country - United States
   ```
 - ```wepy -l [location] -w (for wind)```
 
   ```
   $ wepy -l Washington
   City - Washington
   Region -  DC
   Country - United States


   Wind Temp - 73 F
   Direction - 70
   Speed - 7kmph
   ```
 - ```wepy -l [location] -s (for sun settings)```
 
   ```
   $ wepy -l Washington -s
   City - Washington
   Region -  DC
   Country - United States


   Sunrise - 6:2 am
   Sunset - 8:27 pm
   ```
 - ```wepy -l [location] -a (for atmospheric conditions)```
 
   ```
   $ wepy -l Washington -a
   City - Washington
   Region -  DC
   Country - United States


   Humidity - 93 percent
   Pressure - 1002.0 mb
   Visibility - 13.6m
   ```
   
 - ```wepy -l [location] -f [number of days of forecast] (max 10 days)```
 
   ```
   $ wepy -l Washington -f 4
   City - Washington
   Region -  DC
   Country - United States


   Weather Forecast

   Date - 24 Jul 2017 Mon
   High. Temp - 90
   Low. Temp - 73
   Weather - Thunderstorms


   Date - 25 Jul 2017 Tue
   High. Temp - 83
   Low. Temp - 73
   Weather - Partly Cloudy


   Date - 26 Jul 2017 Wed
   High. Temp - 82
   Low. Temp - 69
   Weather - Partly Cloudy


   Date - 27 Jul 2017 Thu
   High. Temp - 88
   Low. Temp - 72
   Weather - Mostly Cloudy
   ```
 - Usage of multiple parameters are also valid. Combination of ```wepy -l [location] -w -s -f 2 -a``` will result in display of all the contents
   ```
