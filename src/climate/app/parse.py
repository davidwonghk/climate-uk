import csv
import re
from ConfigParser import NoOptionError

'''
provider filtering functionility to the parser below
filter years and columns
'''
class Filter:
    def __init__(self, config, name):
        self.columns = Filter._getList(config, name, 'columns')
        self.years = Filter._getList(config, name, 'years')
            
    @staticmethod
    def _getList(config, name, listName):
        try:
            listStr = config.get(name, listName)
        except NoOptionError:
            return None
        return listStr.split(', ')
        
        
    def filterColumns(self, row):
        if self.columns is None:
            return row
        return {k: row[k] for k in row if k in self.columns}
        
    def filterYears(self, year):
        if self.years is None:
            return True
        return year in self.years
        


'''parse the climate txt data file download from http://www.metoffice.gov.uk/climate/uk
to the Model use in this project'''
class ClimateDataParser:
    MONTH_MAP = {
        'JAN': 1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12
    }
    def __init__(self, model, filter=None):
        self.filter = filter
        self.model = model
    
    def parse(self, txtData, srcData):
        #skip the first few lines until blank line
        data = self._skipTillBlank(txtData)
        
        #replace multiple spaces to single space
        data = re.sub( ' +', ' ', data).strip()
        
        #read the text as csv
        reader = csv.DictReader(data.splitlines(), delimiter=' ')
        for row in reader:
            year = row.pop('Year', None)
            
            if self.filter is not None:
                if not self.filter.filterYears(year):
                    continue
                
                row = self.filter.filterColumns(row)
            
            for month in row:
                c = self.model()
                c.year = year
                c.month = self.MONTH_MAP[month] if month in self.MONTH_MAP else month
                c.data = row[month]
                c.region = srcData['region']
                c.type = srcData['type']
                yield c
            
            
    def _skipTillBlank(self, data):
        s = data.find('\n\n')
        return data[s+1:]
            