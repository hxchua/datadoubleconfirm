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

**Dataset**: covid19_sg.csv  
**Description**: Covid-19 case time series data in Singapore (more details [here](https://data.world/hxchua/covid-19-singapore))// Data is contributed to https://github.com/neherlab/covid19_scenarios          
**Variables**: `Date`,	`Daily_Confirmed_`, `False_Positives_Found`, `Cumulative_Confirmed`, `Daily_Discharged`, `Passed_but_not_due_to_COVID`,	`Cumulative_Discharged`, `Discharged_to_Isolation`, `Still_Hospitalised`, `Daily_Deaths`, `Cumulative_Deaths`, `Tested_positive_demise`, `Daily_Imported`,	`Daily_Local_transmission`, `Local_cases_residing_in_dorms_MOH_report`,	`Local_cases_not_residing_in_doms_MOH_report`,	`Intensive_Care_Unit_(ICU)`, `General_Wards_MOH_report`, `In_Isolation_MOH_report`,	`Total_Completed_Isolation_MOH_report`, `Total_Hospital_Discharged_MOH_report`, `Linked_community_cases`, `Unlinked_community_cases`, `Phase`, `Cumulative_Vaccine_Doses`, `Cumulative_Individuals_Vaccinated`, `Cumulative_Individuals_Vaccination_Completed`  
**Mode of data collection**: Manual/ Web scraping   
**Source**: [Ministry of Health](https://www.moh.gov.sg/covid-19)  

**Dataset**: datagovscraped_stacked.csv  
**Description**: List of datasets available on data.gov.sg as at 2 Sep 2022          
**Variables**: `title`,	`link`, `org`, `description`, `last_updated`, `created`,	`format`, `coverage`, `licence`    
**Mode of data collection**: Web scraping   
**Source**: [Data.gov.sg](https://data.gov.sg/)  

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

**Dataset**: hawker_stacked.csv  
**Descriptions**: Nutritional contents of Singapore hawker foods  
**Variables**: `kcal`,	`protein(g)`, `fat(g)`,	`saturatedfat(g)`,	`dietaryfibre(g)`,	`carbs(g)`,	`cholesterol(mg)`,	`sodium(mg)`,	`food`,	`comments`,	`image_link`,	`type`  
**Mode of data collection**: Webscraping  
**Source**: [Best and Worst Singapore Hawker Chinese Food: Dim Sum, Char Kway Teow and More](https://www.healthxchange.sg/food-nutrition/food-tips/best-worst-singapore-hawker-chinese-food-dim-sum-char-kway-teow),[Best and Worst Singapore Hawker Malay Breakfast Foods: Nasi Lemak, Mee Siam, Soto and More](https://www.healthxchange.sg/food-nutrition/food-tips/best-worst-singapore-hawker-malay-breakfast-foods-nasi-lemak-mee-siam-soto), [Best and Worst Singapore Hawker Indian Breads: Prata, Mutton Murtabak and More](https://www.healthxchange.sg/food-nutrition/food-tips/best-worst-singapore-hawker-indian-breads-prata-mutton-murtabak) 

**Dataset**: mrtfaretime.csv  
**Description**: Travel time and fare information between train (MRT/LRT) stations in Singapore (as at Oct 2018)  
**Variables**: `Station_start` (Boarding station), `Station_end` (Alighting station), `Time` (Travel time in mins), `Adult` (Adult fare), `Senior` (Fare for Seniors and Persons with Disabilities), `Standard` (Fare for Standard Ticket), `Student` (Student fare), `WTCS` (Fare under Workfare Transport Concession Scheme), `REF_STNSTART`, `Latitude_Start`, `Longitude_Start`, `REF_STNEND`, `Latitude_End`, `Longitude_End`      
**Mode of data collection**: Web scraping  
**Source**: [TransitLink Electronic Guide](https://www.transitlink.com.sg/eservice/eguide/rail_idx.php)  

**Dataset**: mrtsg.csv  
**Description**: Latitude and longitude of train (MRT/LRT) stations in Singapore (as at Dec 2020)  
**Variables**: `OBJECTID` (id) , `STN_NAME` (station name), `STN_NO` (station number), `X` (X coord in SVY21 format), `Y` (Y coord in SVY21 format), `Latitude`, `Longitude`, `COLOR` (color of train line)  
**Mode of data collection**: Public dataset, Coordinate conversion web scraping  
**Source**: [LTA DataMall](https://www.mytransport.sg/content/mytransport/home/dataMall.html), [OneMap Singapore](https://docs.onemap.sg/#3414-svy21-to-3857)  

**Dataset**: mydramalistactors_tocsv.csv  
**Description**: Top rated actors from MyDramaList (as at Dec 2022)  
**Variables**: `person`, `ranking`, `likes_num`, `nationality`, `gender`, `dob`, `title`, `title_info`, `title_ratings`        
**Mode of data collection**: Web scraping (slightly over 2000 records scraped)        
**Source**: [MyDramaList](https://mydramalist.com/people/top?page=1)  

**Dataset**: mydramalisttop.csv  
**Description**: Top rated movies from MyDramaList (as at Dec 2022)  
**Variables**: `title`, `ranking`, `movie_url`, `movie_country`, `ratings`, `num_watchers`, `synopsis`, `duration`, `tags`, `genres`, `cast_list`   
**Mode of data collection**: Web scraping (all 5000 records scraped) (Note: Data requires cleaning)  
**Source**: [MyDramaList](https://mydramalist.com/movies/top?page=1)  

**Dataset**: passport.csv  
**Description**: Top 10 Passports (in the 2017 Global Passport Power Rank) and their visa requirements to other countries   
**Variables**: `Top 10 Country` (name of country with passport in Top 10), `Country` (visiting country), `Type of Visa` (visa required)  
**Mode of data collection**: Manual  
**Source**: [Passport Index 2017](https://www.passportindex.org/comparebyPassport.php)

**Dataset**: pokemon.csv  
**Description**: Pokemon and their attack and defense statistics  
**Variables**: `HP`, `Attack`, `Defense`, `Sp Atk`, `Sp Def`, `Speed`, `Total`, `HP Percentile`, `Attack Percentile`,  `Defense Percentile`, `Sp Atk Percentile`, `Sp Def Percentile`, `Speed Percentile`, `Total Percentile`  
**Mode of data collection**: Manual, Excel function for percentile ranking  
**Source**: [Pokemon database](https://pokemondb.net/pokedex/all)  

**Dataset**: populationsg.csv  
**Description**: Count of Residents By Age Group & Type Of Dwelling, Annual from 2000 to 2019    
**Variables**: `agegroup`, `dwelling`, `value`, `year`    
**Mode of data collection**: API   
**Source**: [Singapore Department of Statistics](https://www.tablebuilder.singstat.gov.sg/publicfacing/createDataTable.action?refId=14910)  

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

**Dataset**: seedly_sal.csv  
**Description**: Annual base salaries ($'000) for different roles in various industries in Singapore (as at Jan 2020)    
**Variables**: `Industry`, `Role`, `Minimum`, `Median`, `Maximum`  
**Mode of data collection**: Web scraping     
**Source**: ["The Ultimate Salary Guide For Singaporeans" on Seedly](https://blog.seedly.sg/salary-guide-singapore/)  

**Dataset**: tfresults02.csv  
**Description**: Results of 100m and 200m national track-and-field finals for "A" division boys and girls between 2002 and 2016    
**Variables**: `Year`, `Event`, `Division`, `Gender`, `School`, `Name`, `Position`, `Timing (in s)`  
**Mode of data collection**: Manual  
**Source**: [Singapore Athletics LIVE Results](https://tnf.sg/)  

**Dataset**: unesco_sites.csv  
**Description**: UNESCO World Heritage List (as at 30 Oct 2019)       
**Variables**: `country`, `site`, `type` (category of site)    
**Mode of data collection**: Webscraping  
**Source**: [UNESCO World Heritage Centre - World Heritage List](https://whc.unesco.org/en/list/), more data can be downloaded [here](https://whc.unesco.org/en/syndication).    

**Dataset**: usunirankings.csv  
**Description**: Average U.S. News Rankings for 123 Universities: 2013-2020      
**Variables**: `school`, `rank_2013`, `rank_2014`, `rank_2015`, `rank_2016`, `rank_2017`, `rank_2018`, `rank_2019`, `rank_2020`,  `avg_rank`, `chg` (change between 2013 and 2020)    
**Mode of data collection**: Webscraping  
**Source**: [Public University Honors](https://publicuniversityhonors.com/2016/09/18/average-u-s-news-rankings-for-126-universities-2010-1017/)  

**Dataset**: vaccinations_sg_minmed.csv  
**Description**: Price and description of vaccinations offered by Minmed in Singapore. Price is applicable for one dose only and includes consultation charge.       
**Variables**: `vaccinations`, `public_rate`, `chas_green`, `merdeka_generation_chas_blue_orange`, `pioneer_generation`, `description`    
**Mode of data collection**: Webscraping       
**Source**: [Minmed](https://minmed.sg/vaccinations/)   

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

**Notebook**: chopesg.ipynb  
**Description**: Python code for scraping 100 best restaurants in Singapore published by [chope.co](https://www.chope.co/singapore-restaurants/pages/100-best-restaurants-singapore?lang=en_US)    

**Notebook**: covid_public_places_2021.ipynb  
**Description**: Python code for webscraping, cleaning, processing and updating of the [Public Places Visited by Singapore Covid-19 Cases dataset](https://data.world/hxchua/public-places-visited-in-singapore-by-covid-19-cases) using BeautifulSoup, pdfplumber and Google Sheets API. It updates the dataset by comparing the previous day's PDF with the current day's published by [Ministry of Health Singapore](https://www.moh.gov.sg/covid-19), and adding the newly added places to the existing dataset.  

**Notebook**: covid_sg_stats.ipynb  
**Description**: Python code for webscraping, cleaning, processing and updating of the [COVID-19 Singapore dataset](https://data.world/hxchua/covid-19-singapore) using BeautifulSoup, pdfplumber and Google Sheets API based on data published by [Ministry of Health Singapore](https://www.moh.gov.sg/covid-19).    

**Notebook**: covid_spread.ipynb  
**Description**: Python code for understanding the pace of increase in number of COVID-19 cases for each country using [data](https://github.com/CSSEGISandData/COVID-19) provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)     

**Notebook**: Creating Datasets in Python.ipynb  
**Description**: Python code for importing practice datasets from R to Python and creating hypothetical datasets  

**Notebook**: Creating Datasets in R.ipynb  
**Description**: R code for creating hypothetical datasets  

**Notebook**: Data Cleaning in Python.ipynb  
**Description**: Python code for performing various data cleaning tasks  

**Notebook**: Data Cleaning in R.ipynb  
**Description**: R code for performing various data cleaning tasks    

**Notebook**: engineeringjobs.ipynb  
**Description**: Python code for scraping information relating to engineering job openings in Singapore on a government portal as at 31 Jul 2020 using selenium and BeautifulSoup 

**Notebook**: emojis.ipynb  
**Description**: Python code for scraping [Emoji Cheat Sheet](https://www.webfx.com/tools/emoji-cheat-sheet/) information   

**Notebook**: Gov.sg Translations.ipynb  
**Description**: Python code for scraping Official English-Mandarin translations of Singapore Government Terms from [Government Terms Translated](https://www.gov.sg/resources/translation)      

**Notebook**: imdb.ipynb  
**Description**: Python code for scraping imdb.com most popular movies information  

**Notebook**: Json.ipynb  
**Description**: Python code for working with Json    

**Notebook**: linecharts.ipynb  
**Description**: Python code for plotting line charts using matplotlib and seaborn involving major/ minor ticks, markers and data labels for the last point  

**Notebook**: lta_tweets.ipynb  
**Description**: Python code for working with text and datetime data from [LTATrafficNews](https://twitter.com/ltatrafficnews?lang=en) tweets (between 12-Dec-2019 and 29-Dec-2019)       

**Notebook**: mas-api.ipynb  
**Description**: Python code for calling data from Monetary Authority of Singapore's [API](https://secure.mas.gov.sg/api/APIDescPage.aspx?resource_id=5f2b18a8-0883-4769-a635-879c63d3caac)    

**Notebook**: mohcovid.ipynb    
**Description**: Python code for scraping updates on COVID-19 local situation (Singapore) on Ministry of Health's [website](https://www.moh.gov.sg/covid-19/past-updates) since January and an [interactive visualization](https://nbviewer.jupyter.org/github/hxchua/datadoubleconfirm/blob/master/notebooks/mohcovid.html) created using Plotly (download/run the notebook locally to view it) with some static charts created using Seaborn  

**Notebook**: Monte_Carlo_COVID.ipynb    
**Description**: Python code for Monte Carlo simulations on number of COVID-19 cases in Singapore using 20 days of [historical data](https://github.com/hxchua/datadoubleconfirm/blob/master/datasets/covid19_sg.csv)         

**Notebook**: OneMapSG_XY_LatLon.ipynb    
**Description**: Python code for converting from OneMap Singapore's [X Y coordinates](https://www.onemap.gov.sg/docs/#3414-svy21-to-3857) in 3414(SVY21) format to latitude and longitude in 4326(WGS84) format      

**Notebook**: pytesseract_onlineimage.ipynb      
**Description**: Python code for extracting text data from an image hosted online          

**Notebook**: QOTD.ipynb  
**Description**: Python code for scraping quotes off "Inhale, Exhale and Repeat After Me! 150 Best Quotes About Life" by [Parade.com](https://parade.com/937586/parade/life-quotes/)   

**Notebook**: seleniummrt.ipynb  
**Description**: Python code for scraping time and fare information between train stations in Singapore from [TransitLink Electronic Guide](https://www.transitlink.com.sg/eservice/eguide/rail_idx.php)    

**Notebook**: singapore_latlon.ipynb  
**Description**: Python code for getting data on latitude and longitude based on road name in Singapore using [OneMap API](https://www.onemap.gov.sg/apidocs/)    

**Notebook**: SingStat API.ipynb  
**Description**: Python code for calling data from SingStat Table Builder/ Singapore Department of Statistics using the [API function](https://www.tablebuilder.singstat.gov.sg/publicfacing/initApiList.action)      

**Notebook**: ssg-api.ipynb  
**Description**: Python code for calling data from SkillsFuture Singapore using their [API](https://developer.ssg-wsg.gov.sg/webapp/api-discovery)    

**Notebook**: Statistical tests.ipynb  
**Description**: R code for performing various types of two-sample tests and correlation checks  

**Notebook**: StatutoryBoardSG.ipynb  
**Description**: Python code for scraping addresses/ contact information of statutory boards in Singapore from [Singapore Government Directory](https://www.gov.sg/sgdi/statutory-boards) and automating download of organisation logo images  

**Notebook**: table.ipynb  
**Description**: Python code for scraping table data from a website. Here we scrape price and description information of vaccinations offered by Minmed in Singapore from [Minmed](https://minmed.sg/vaccinations/)  

**Notebook**: traffic_updates.ipynb  
**Description**: Python code for scraping Traffic Updates data from [LTA One Monitoring](https://onemotoring.lta.gov.sg/content/onemotoring/home/driving/traffic_information/traffic_updates_and_road_closures.html?type=tc)   

**Notebook**: Text Frequency Analysis.ipynb  
**Description**: R code for getting frequency distribution of words in a chunk of text  

**Notebook**: textgen-covid_resilience.ipynb  
**Description**: Python code for text-generating neural network trained using text from [Singapore's Budget 2020 - Resilience Budget/ Supplementary Budget Statement](https://www.singaporebudget.gov.sg/budget_2020/resilience-budget/supplementary-budget-statement) with textgenrnn  

**Notebook**: unesco.ipynb  
**Description**: Python code for scraping UNESCO World Heritage countries and sites from [UNESCO World Heritage Centre - World Heritage List](https://whc.unesco.org/en/list/)      

**Notebook**: weathersg.ipynb  
**Description**: Python code for scraping rainfall and temperatures data from [Meteorological Service Singapore’s website](http://www.weather.gov.sg/climate-historical-daily/) for five randomly selected locations in different parts of Singapore, namely Ang Mo Kio, Changi, Clementi, Jurong West, and Newton    

**Notebook**: WiDS.ipynb  
**Description**: R code for predicting gender of survey respondents as part of the WiDS 2018 Datathlon  

**Notebook**: youtube_data_analysis-need_key.ipynb  
**Description**: Python code for getting YouTube data for analysis based on a list of search terms using YouTube Data API v3    
