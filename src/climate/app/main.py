import ConfigParser

from source import Source
from download import BlukDownloader
from parse import Filter, ClimateDataParser


'pull data from the climate web site'
def pull(model, checkStartup=False):
    #read user config
    config = ConfigParser.ConfigParser()
    config.read('conf/app.conf')
    
    #check if it is a startup run
    if checkStartup:
        if not config.getboolean('download', 'startup'):
            return 0
            
    #initailize the objects and inject the dependencies
    source = Source(config, 'download')
    filter = Filter(config, 'filter')
    parser = ClimateDataParser(model, filter)
    downloader = BlukDownloader(source, parser)
    
    #start the web-data-downloader when server start
    return downloader.start()
