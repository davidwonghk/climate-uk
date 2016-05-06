# Django Climate Web Server

## PURPOSE
A demostration to show how I learn pyhon+DJango in a given short amount of peroid.

This web server would download the climate data from:
http://www.metoffice.gov.uk/climate/uk/summaries/datasets

and provide RESTFUL Webservice to frontend.

## PREREQUEST
- Python 2.7.6
- Django 1.9.5
- django-cors-headers (https://github.com/ottoyiu/django-cors-headers/)

## INSTALL, CONFIGURATION AND START
1. downlaod all the source code and run the following command in the "server" folder
```
python src/manage.py makemigrations
python src/manage.py migrate
```
after this step, a database db.sqlite3 should be created

2. edit the conf/app.conf (follow the instruction of the comments):
```
[download]
#if startup flag is set and set to True, the server would download the climate data from the web when startup
startup=True

#the url pattern of the txt climate data web
urlTemplate=http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{type}/date/{region}.txt

#the following parameters are following the above pattern
type=Tmax, Tmin, Tmean, Sunshine, Rainfall
region=UK, England, Wales, Scotland


[filter]
#if 'columns' is set, only the following columns would be saved to the database
columns = JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC

#if 'years' is set, only the following years would be downloaded to the database
#years = 2007, 2008
```

3. edit the conf/logging.conf for logging

4. To start the Django server:
```
python src/manage.py runserver
```

## WEBSERVICE
### To get the climate data
```
http://{host}/climate
```
possible GET parameters:
- [region] - The region set in the conf/app.conf
- [type] - The type set in the conf/app.conf
- [year] - a number between 1910 - 2016, to query the data of specify year
- [month] - a number between 1 - 12, to query the data of specify month

example:
```
http://{host}/climate/?region=England&type=Tmax&year=2012
```
```
[  
   {   'region':u'England', 'month':u'1', 'type':u'Tmax', 'year':2012 },
   {   'region':u'England', 'month':u'10', 'type':u'Tmax', 'year':2012 },
   {   'region':u'England', 'month':u'11', 'type':u'Tmax', 'year':2012 },
   {   'region':u'England', 'month':u'12', 'type':u'Tmax', 'year':2012 },
   {   'region':u'England', 'month':u'2', 'type':u'Tmax', 'year':2012 },
   {   'region':u'England', 'month':u'3', 'type':u'Tmax', 'year':2012 },
   {   'region':u'England', 'month':u'4', 'type':u'Tmax', 'year':2012 },
   {   'region':u'England', 'month':u'5', 'type':u'Tmax', 'year':2012 },
   {   'region':u'England', 'month':u'6', 'type':u'Tmax', 'year':2012 },
   {   'region':u'England', 'month':u'7', 'type':u'Tmax', 'year':2012 },
   {   'region':u'England', 'month':u'8', 'type':u'Tmax', 'year':2012 },
   {   'region':u'England', 'month':u'9', 'type':u'Tmax', 'year':2012 },

]
```

### List the options
(the GET parameters above)
```
http://{host}/climate/options
```
example:
```
{
  "region": [ "England", "Scotland", "UK", "Wales" ],
  "month": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ],
  "type": [ "Rainfall", "Sunshine", "Tmax", "Tmean", "Tmin" ],
  "year": [ 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016 ] 
}
```

### To force the server update the climate data 
(by downloading from the origin climate web site)
```
http://{host}/climate/pull
```

