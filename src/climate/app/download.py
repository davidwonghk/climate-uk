import logging
import requests

'download file by url via http protocal'         
class SingleHttpDownloader:
    
    'download by url and return the text data'
    def download(self, url):
        r = requests.get(url)
        return r.content
        
            
'''Download form the website(links provided by source) 
and save it into the model(after parsing by parser)'''
class BlukDownloader:
    
    def __init__(self, source, parser, singleDownloader=SingleHttpDownloader()):
        self.source = source
        self.singleDownloader = singleDownloader
        self.parser = parser
        
        
    def start(self):
        #download for each url from source, parse them and save into the model
        for uv in self.source.urls_with_vars():
            url = uv['url']
            logging.debug("download: {}".format(url))
            content = self.singleDownloader.download(url)
            
            for m in self.parser.parse(content, uv):
                logging.debug("saving: {}".format(m))
                m.save()
                yield m
                
