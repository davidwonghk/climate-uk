import ConfigParser
import logging

from source import Source
from download import BlukDownloader
from parse import Filter, ClimateDataParser


class ClimateApp:
    def __init__(self, model):
        #read user config
        self.config = ConfigParser.ConfigParser()
        self.config.read('conf/app.conf')
        
        #initailize the objects and inject the dependencies
        source = Source(self.config, 'download')
        filter = Filter(self.config, 'filter')
        parser = ClimateDataParser(model, filter)
        self.downloader = BlukDownloader(source, parser)

    'pull data from the climate web site'
    def pull(self):
        return self.downloader.start()
        

    'start the web-data-downloader when server start'
    def pullAtStartup(self):
        
        #check if it is a startup run
        pullAtStartup = self.config.getboolean('download', 'startup')
        logging.info('download climate from web at startup={}'.format(pullAtStartup))
        if pullAtStartup:
            for c in self.downloader.start():
                pass
            