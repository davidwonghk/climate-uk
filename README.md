URL: http://www.metoffice.gov.uk/climate/uk/summaries/datasets#Yearorder

1. Data parsing and modelling - Server side - use Python + Django 

1.1 Use above URL and write code to programatically download the data for Max temp, Min temp, Mean temp, Sunshine, and Rainfall for UK, England, Wales, and Scotland regions. 
1.2 Create appropriate data model using Django ORM to store the above data (Hint: Please make sure that the model is generic so user can store data across more regions and parameters in future if necessary without changing the model).
1.3 Write code to store all of the downloaded data from 1.1 in the data model built in 1.2 (please use SQLite to store the data). The file download and data storing process has to be fully automated and user should be able to run it multiple times without any duplication of data etc. 

2. Simple mobile app - Ionic Framework
Please build a simple mobile app to display the data from 1. 
