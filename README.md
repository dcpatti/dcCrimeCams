# dcCrimeCams

Group project analyzing the Washington, DC private security camera rebate/voucher programs.  Are the cameras being placed in the neighborhoods that have the highest crime rates? Do the cameras have any effect on the overall crime rates?

This project uses over 70,000 data records which were collected via geoJSON/API query and by CSV download. The data was cleaned and normalized using Python and Pandas and stored in a SQLite database.  The data was analyzed looking for relationships and trends.

Visualizations include:

* Interactive D3.js-based bar chart detailing 3 years of crime types and rates in each police district
* Interactive D3.js and Leaflet.js-based map comparing the crime rates to the proliferance of the private cameras
* Searchable, sortable data table of per-district camera spend and counts

 Full live site, hosted on Heroku:  https://dccrimecams.herokuapp.com/welcome


![image](https://github.com/dcpatti/dcCrimeCams/blob/master/DCThumbnail.JPG)
