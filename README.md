# Data is the ink

Provides datasets for data visualization, statistical analysis and modelling


List of datasets along with descriptions
---

**Dataset**: mrtsg.xlsx  
**Description**: Geolocations of train (MRT/LRT) stations in Singapore (as at Jun 2017)  
**Variables**: `OBJECTID` (id) , `STN_NAME` (station name), `STN_NO` (station number), `X` (X coord in SVY21 format), `Y` (Y coord in SVY21 format), `Latitude`, `Longitude`, `COLOR` (color of train line)    
**Mode of data collection**: Public dataset, Coordinate conversion web scraping  
**Source**: [LTA DataMall](https://www.mytransport.sg/content/mytransport/home/dataMall.html), [OneMap Singapore](https://docs.onemap.sg/#3414-svy21-to-3857)  

**Dataset**: passport.xlsx  
**Description**: Top 10 Passports (in the 2017 Global Passport Power Rank) and their visa requirements to other countries 
**Variables**: `Top 10 Country` (name of country with passport in Top 10), `Country` (visiting country), `Type of Visa` (visa required)  
**Mode of data collection**: Manual  
**Source**: [Passport Index 2017](https://www.passportindex.org/comparebyPassport.php)

**Dataset**: pokemon.xlsx  
**Description**: Pokemon and their attack and defense statistics  
**Variables**: `HP`, `Attack`, `Defense`, `Sp Atk`, `Sp Def`, `Speed`, `Total`, `	HP Percentile`, `Attack Percentile`,  `Defense Percentile`, `Sp Atk Percentile`, `Sp Def Percentile`, `Speed Percentile`, `Total Percentile`  
**Mode of data collection**: Manual, Excel function for percentile ranking  
**Source**: [Pokemon database](https://pokemondb.net/pokedex/all)  

**Dataset**: primaryschoolsg.xlsx  
**Description**: Locations of Primary schools in Singapore and their popularity  
**Variables**: `Name`, `Type`, `GenderMix`, `Area`, `Zone`, `PostalCode`, `Latitude`, `Longitude`, `PlacestakenuptillPhase2B`  
**Mode of data collection**: Public data, Web scraping, Tableau-generated latitude/longitude based on Postal code  
**Source**: [Wikipedia](https://en.wikipedia.org/wiki/Primary_schools_in_Singapore), [School Information Service - MOE](http://sis.moe.gov.sg/SchoolDirectory.aspx), [Salary.sg](http://www.salary.sg/2017/best-primary-schools-2017/)  

**Dataset**: tfresults02.xlsx  
**Description**: Results of 100m and 200m national track-and-field finals for "A" division boys and girls between 2002 and 2016    
**Variables**: `Year`, `Event`, `Division`, `Gender`, `School`, `Name`, `Position`, `Timing (in s)`  
**Mode of data collection**: Manual  
**Source**: [Singapore Athletics LIVE Results](https://tnf.sg/)  

