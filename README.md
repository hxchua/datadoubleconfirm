# Data is nutrients for the soul

Provides simple datasets for data visualization, statistical analysis and modelling  
Suitable for those starting out in data science and of course all who find the datasets useful  
Data visualizations can be found [here](https://public.tableau.com/profile/hx.chua#!/)  
Tutorials/ exercises can be found [here](https://projectosyo.wix.com/datadoubleconfirm)  
If you find my repo useful, [buy me a coffee](https://www.buymeacoffee.com/MnhwNsXTE)!

List of datasets along with descriptions
---
**Dataset**: akcdogs.csv  
**Description**: Cleaned data on dog breeds scraped from akc.org (as at 17 Jan 2018)  
**Variables**: `Breed` , `Trait1`, `Trait2`, `Trait3`, `Energy level`, `Size`, `Rank`, `Good with Children`, `Good with other Dogs`, `Shedding`, `Grooming`, `Trainability`, `Height`, `Weight`, `Life expectancy`, `Barking level`, `Group`             
**Mode of data collection**: Web scraping    
**Source**: [American Kennel Club](http://www.akc.org/content/news/articles/most-popular-dog-breeds-full-ranking-list/?button)  

**Dataset**: arrivals2018.csv  
**Description**: Top 20 cities based on 2017 arrivals and 2018 estimates  
**Variables**: `rank` , `city`, `country`, `arrivals_2017` (actual arrival count for 2017), `arrivals_2018` (estimated arrival count for 2018)             
**Mode of data collection**: Web scraping    
**Source**: [Most visited: World's top cities for tourism](http://edition.cnn.com/travel/article/most-visited-cities-euromonitor-2018/index.html)  

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

**Dataset**: Class1.csv  
**Description**: Hypothetical dataset consisting score results of 100 students for three tests      
**Variables**: `id`, `gender`, `test1`, `test2`, `test3`          
**Mode of data collection**: N.A.    
**Source**: N.A.    

**Dataset**: Class2.csv  
**Description**: Hypothetical dataset consisting score results of 100 students for four tests      
**Variables**: `id`, `gender`, `test1`, `test2`, `test3`, `test4`            
**Mode of data collection**: N.A.    
**Source**: N.A.  

**Dataset**: DisneySongs25.csv  
**Description**: Top 25 Disney Songs (as at 4 Apr 2016)  
**Variables**: `Rank` , `Song Title`, `Movie`, `Year`, `Lyrics`        
**Mode of data collection**: Manual    
**Source**: [Top 25 Disney Songs - IGN](https://www.ign.com/articles/2013/08/09/top-25-disney-songs-2), [Metrolyrics](www.metrolyrics.com), [Disneyclips.com](https://www.disneyclips.com/)  

**Dataset**: emojis.csv  
**Description**: names and descriptions of emojis   
**Variables**: `id` (number to identify unique emoji in dataset), `index` (running number in dataset), `name` (name of emoji), `desc` (description/ alternative names)          
**Mode of data collection**: Web scraping   
**Source**: [Emoji Cheat Sheet](https://www.webfx.com/tools/emoji-cheat-sheet/)    

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

**Dataset**: gov-sg-terms-translations.tsv  
**Descriptions**: Official English-Mandarin translations of Singapore Government Terms.  
**Variables**: `english`, `mandarin`  
**Mode of data collection**: Webscraping  
**Source**: [Government Terms Translated](https://www.gov.sg/resources/translation) 


**Dataset**: mrtfaretime.csv  
**Description**: Travel time and fare information between train (MRT/LRT) stations in Singapore (as at Oct 2018)  
**Variables**: `Station_start` (Boarding station), `Station_end` (Alighting station), `Time` (Travel time in mins), `Adult` (Adult fare), `Senior` (Fare for Seniors and Persons with Disabilities), `Standard` (Fare for Standard Ticket), `Student` (Student fare), `WTCS` (Fare under Workfare Transport Concession Scheme), `REF_STNSTART`, `Latitude_Start`, `Longitude_Start`, `REF_STNEND`, `Latitude_End`, `Longitude_End`      
**Mode of data collection**: Web scraping  
**Source**: [TransitLink Electronic Guide](https://www.transitlink.com.sg/eservice/eguide/rail_idx.php)  

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

**Dataset**: secsch_cleaned.csv  
**Description**: Locations of Secondary schools in Singapore and their 2017 PSLE cut-off scores   
**Variables**: `row` (row number), `SCHNAME` (name of school in upper case), `zipcode`, `area`, `zone`, `type`, `latitude`, `longitude`, `School` (name of school for PSLE cut-off scores as matching key), `Rank2017`, `IB`, `IP`, `SAP`, `Girls`, `Boys`, `Co-ed`, `O-level track` (PSLE cut-off score for O-level track), `PSLE2017 Cut Off`, `Gender Mix`  
**Mode of data collection**: Web scraping, Tableau-generated latitude/longitude based on zipcode, Manual    
**Source**: [School Information Service - MOE](http://sis.moe.gov.sg/SchoolDirectory.aspx), [Salary.sg](https://www.salary.sg/2017/secondary-school-ranking-based-on-cut-off-for-2017-intake/)  

**Dataset**: tfresults02.csv  
**Description**: Results of 100m and 200m national track-and-field finals for "A" division boys and girls between 2002 and 2016    
**Variables**: `Year`, `Event`, `Division`, `Gender`, `School`, `Name`, `Position`, `Timing (in s)`  
**Mode of data collection**: Manual  
**Source**: [Singapore Athletics LIVE Results](https://tnf.sg/)  

**Dataset**: usunirankings.csv  
**Description**: Average U.S. News Rankings for 123 Universities: 2013-2020      
**Variables**: `school`, `rank_2013`, `rank_2014`, `rank_2015`, `rank_2016`, `rank_2017`, `rank_2018`, `rank_2019`, `rank_2020`,  `avg_rank`, `chg` (change between 2013 and 2020)    
**Mode of data collection**: Webscraping  
**Source**: [Public University Honors](https://publicuniversityhonors.com/2016/09/18/average-u-s-news-rankings-for-126-universities-2010-1017/)  

**Dataset**: wastestats.csv  
**Description**: 15 years of data from 2003 to 2017 on waste management and recycling statistics (Waste type is inconsistently named across years. eg. C&D should refer to construction debris, and some categories are capitalized in some years but not others)      
**Variables**: `waste_type`, `waste_disposed_of_tonne`, `total_waste_recycled_tonne`, `total_waste_general_tonne`, `recycling_rate`, `year`    
**Mode of data collection**: Manual (Consolidated data in CSV format from PDF and website)     
**Source**: [National Environment Agency](https://www.nea.gov.sg/our-services/waste-management/waste-statistics-and-overall-recycling)   


List of notebooks along with descriptions
---

**Notebook**: AKCDogs.ipynb  
**Description**: Python code for scraping akc.org dog information  

**Notebook**: bookdepository.ipynb  
**Description**: Python code for scraping bookdepository.com bestsellers information  

**Notebook**: emojis.ipynb  
**Description**: Python code for scraping [Emoji Cheat Sheet](https://www.webfx.com/tools/emoji-cheat-sheet/) information   

**Notebook**: imdb.ipynb  
**Description**: Python code for scraping imdb.com most popular movies information  

**Notebook**: Creating Datasets in Python.ipynb  
**Description**: Python code for importing practice datasets from R to Python and creating hypothetical datasets  

**Notebook**: Creating Datasets in R.ipynb  
**Description**: R code for creating hypothetical datasets  

**Notebook**: Data Cleaning in Python.ipynb  
**Description**: Python code for performing various data cleaning tasks  

**Notebook**: Data Cleaning in R.ipynb  
**Description**: R code for performing various data cleaning tasks    

**Notebook**: seleniummrt.ipynb  
**Description**: Python code for scraping time and fare information between train stations in Singapore from [TransitLink Electronic Guide](https://www.transitlink.com.sg/eservice/eguide/rail_idx.php)    

**Notebook**: Statistical tests.ipynb  
**Description**: R code for performing various types of two-sample tests and correlation checks  

**Notebook**: StatutoryBoardSG.ipynb  
**Description**: Python code for scraping addresses/ contact information of statutory boards in Singapore from [Singapore Government Directory](https://www.gov.sg/sgdi/statutory-boards) and automating download of organisation logo images  

**Notebook**: Text Frequency Analysis.ipynb  
**Description**: R code for getting frequency distribution of words in a chunk of text  

**Notebook**: WiDS.ipynb  
**Description**: R code for predicting gender of survey respondents as part of the WiDS 2018 Datathlon  

**Notebook**: youtube_data_analysis-need_key.ipynb  
**Description**: Python code for getting YouTube data for analysis based on a list of search terms using YouTube Data API v3    
