from urlparse import urlparse
from urllib import urlopen
from hashlib import sha1

class URLMock(object):

    def __init__(self, url):
        '''Initialize a new URLMock object based on a given url'''
        
        self.responses = {}

        parsed_url = urlparse(url)
        url_components = dict( zip( ['scheme',
                                     'netloc',
                                     'path',
                                     'params',
                                     'query',
                                     'fragment'
                                     ], parsed_url ) )
        
        self.__dict__.update( url_components )
        self.params = params = dict(part.split('=') for part in parsed_url[4].split('&'))
        
        self.force(url)
        
    def force(self, url):
        '''Fetches a url and stores the answer'''
        key = sha1()
        
        content = urlopen(url).read()
        
        key.update(content)
        key = sha1().digest()
        
        self.responses[key] = content
        
    def __repr__(self):
        return repr(self.__dict__)



    
if __name__ == '__main__':
    from restmock import URLMock
    mock = URLMock('http://www.lanacion.com?param1=value1&param2=value2')
    mock.force('http://www.lanacion.com?param1=value1&param2=value2')
    print repr(mock)


