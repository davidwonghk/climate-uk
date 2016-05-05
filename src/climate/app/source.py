import itertools
from string import Formatter

'read the configuration file and give out the urls for download'
class Source:
    def __init__(self, conf, name):
        self.name = name
        self.conf = conf
        
    def urls_with_vars(self):
        urlTemplate = self.conf.get(self.name, 'urlTemplate')
        
        #get the string keys
        keysMap = {} 
        for keys in Formatter().parse(urlTemplate):
            key = keys[1]
            if key == None:
                break
            keysMap[key] = self.conf.get(self.name, key).split(', ')
            
        #product all the keys to dictionary combination
        for d in Source._productDict(keysMap):
            url = urlTemplate.format(**d)
            d.update({'url': url})
            yield d
        
        
    @staticmethod
    def _productDict(d):
        varNames = sorted(d)
        combinations = [dict(zip(varNames, prod)) for prod in itertools.product(*(d[varName] for varName in varNames))]
        return combinations