# Data is nutrients for the soul

Provides simple datasets for data visualization, statistical analysis and modelling  
Suitable for those starting out in data science and of course all who find the datasets useful  
Data visualizations can be found [here](https://public.tableau.com/profile/hx.chua#!/)  
Tutorials/ exercises can be found [here](https://projectosyo.wix.com/datadoubleconfirm)  

List of datasets along with descriptions
---
**Dataset**: akcdogs.csv  
**Description**: Cleaned data on dog breeds scraped from akc.org (as at 17 Jan 2018)  
**Variables**: `Breed` , `Trait1`, `Trait2`, `Trait3`, `Energy level`, `Size`, `Rank`, `Good with Children`, `Good with other Dogs`, `Shedding`, `Grooming`, `Trainability`, `Height`, `Weight`, `Life expectancy`, `Barking level`, `Group`             
**Mode of data collection**: Web scraping    
**Source**: [American Kennel Club](http://www.akc.org/content/news/articles/most-popular-dog-breeds-full-ranking-list/?button)  

**Dataset**: bookdepo.csv  
**Description**: Raw data on bestsellers scraped from bookdepository.com (as at 11 Jan 2018)  
**Variables**: `(blank)` (row index number) , `name` (book title), `material` (book material), `author` (author), `rank` (bestsellers rank), `maincat` (main category), `subcat` (sub category), `rating` (rating by readers), `ratingcount` (number of readers who gave ratings), `saleprice` (discounted price in S$), `listprice` (original price in S$), `numofpages` (number of pages), `datepub` (date published), `isbn13` (ISBN13 number)          
**Mode of data collection**: Web scraping    
**Source**: [Book Depository](https://www.bookdepository.com/bestsellers)  

**Dataset**: bookdepobest.csv  
**Description**: Cleaned data on bestsellers scraped from bookdepository.com (as at 11 Jan 2018)  
**Variables**: `SN`, `name`, `rank`, `maincat`, `subcat`, `rating`, `saleprice`, `listprice`, `datepub`, `isbn13`, `GoodreadsRateCount`, `BookMaterial`, `Author(s)`, `PageCount`        
**Mode of data collection**: Web scraping    
**Source**: [Book Depository](https://www.bookdepository.com/bestsellers)  

**Dataset**: Book1.csv  
**Description**: Hypothetical dataset consisting score results of 50 students for three exams      
**Variables**: `id`, `gender`, `exam1`, `exam2`, `exam3`          
**Mode of data collection**: N.A.    
**Source**: N.A.    

**Dataset**: FreqWordsObama.csv  
**Description**: Frequently mentioned words in Barack Obama's tweets between 2007 and 2017 (as at 12 Dec 2017)  
**Variables**: `Year` (year of tweet), `Word` (frequently mentioned word), `Count` (number of tweets containing word), `Year Volume` (volume of tweet in the year), `Percentage` (percentage of tweets containing word)      
**Mode of data collection**: Twitter web scraping and text mining  
**Source**: [Barack Obama's Twitter account](https://twitter.com/barackobama)    

**Dataset**: GovSG.csv  
**Description**: Addresses with GIS location and contact information of Ministries and Statutory Boards in Singapore  
**Variables**: `Organisation`, `Type` (Ministry/ Statutory Board), `Zipcode`, `Latitude`, `Longitude`, `Website`, `Tel`, `Fax`, `Email`, `Enquiry/ Feedback Form` (url), `Parent Ministry` (Statutory Boards under respective Ministries)       
**Mode of data collection**: Web scraping, Manual, Tableau-generated latitude/longitude based on Zipcode  
**Source**: [Singapore Government Directory](https://www.gov.sg/sgdi/statutory-boards), [The Public Service | Careers@Gov](https://www.careers.gov.sg/build-your-career/career-toolkit/public-agencies)    

**Dataset**: mrtsg.csv  
**Description**: Latitude and longitude of train (MRT/LRT) stations in Singapore (as at Jun 2017)  
**Variables**: `OBJECTID` (id) , `STN_NAME` (station name), `STN_NO` (station number), `X` (X coord in SVY21 format), `Y` (Y coord in SVY21 format), `Latitude`, `Longitude`, `COLOR` (color of train line)    
**Mode of data collection**: Public dataset, Coordinate conversion web scraping  
**Source**: [LTA DataMall](https://www.mytransport.sg/content/mytransport/home/dataMall.html), [OneMap Singapore](https://docs.onemap.sg/#3414-svy21-to-3857)  

**Dataset**: passport.csv  
**Description**: Top 10 Passports (in the 2017 Global Passport Power Rank) and their visa requirements to other countries 
**Variables**: `Top 10 Country` (name of country with passport in Top 10), `Country` (visiting country), `Type of Visa` (visa required)  
**Mode of data collection**: Manual  
**Source**: [Passport Index 2017](https://www.passportindex.org/comparebyPassport.php)

**Dataset**: pokemon.csv  
**Description**: Pokemon and their attack and defense statistics  
**Variables**: `HP`, `Attack`, `Defense`, `Sp Atk`, `Sp Def`, `Speed`, `Total`, `	HP Percentile`, `Attack Percentile`,  `Defense Percentile`, `Sp Atk Percentile`, `Sp Def Percentile`, `Speed Percentile`, `Total Percentile`  
**Mode of data collection**: Manual, Excel function for percentile ranking  
**Source**: [Pokemon database](https://pokemondb.net/pokedex/all)  

**Dataset**: primaryschoolsg.csv  
**Description**: Locations of Primary schools in Singapore and their popularity  
**Variables**: `Name`, `Type`, `GenderMix`, `Area`, `Zone`, `PostalCode`, `Latitude`, `Longitude`, `PlacestakenuptillPhase2B`  
**Mode of data collection**: Public data, Web scraping, Tableau-generated latitude/longitude based on Postal code  
**Source**: [Wikipedia](https://en.wikipedia.org/wiki/Primary_schools_in_Singapore), [School Information Service - MOE](http://sis.moe.gov.sg/SchoolDirectory.aspx), [Salary.sg](http://www.salary.sg/2017/best-primary-schools-2017/)  

**Dataset**: tfresults02.csv  
**Description**: Results of 100m and 200m national track-and-field finals for "A" division boys and girls between 2002 and 2016    
**Variables**: `Year`, `Event`, `Division`, `Gender`, `School`, `Name`, `Position`, `Timing (in s)`  
**Mode of data collection**: Manual  
**Source**: [Singapore Athletics LIVE Results](https://tnf.sg/)  


List of notebooks along with descriptions
---

**Notebook**: AKCDogs.ipynb  
**Description**: Python code for scraping akc.org dog information  

**Notebook**: bookdepository.ipynb  
**Description**: Python code for scraping bookdepository.com bestsellers information  

**Notebook**: imdb.ipynb  
**Description**: Python code for scraping imdb.com most popular movies information  

**Notebook**: Statistical tests.ipynb  
**Description**: R code for performing various types of two-sample tests and correlation checks  

**Notebook**: StatutoryBoardSG.ipynb  
**Description**: Python code for scraping addresses/ contact information of statutory boards in Singapore from [Singapore Government Directory](https://www.gov.sg/sgdi/statutory-boards) and automating download of organisation logo images  

**Notebook**: WiDS.ipynb  
**Description**: R code for predicting gender of survey respondents as part of the WiDS 2018 Datathlon


  
