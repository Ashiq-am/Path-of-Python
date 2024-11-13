import abc
import urllib
import urllib.error
import urllib.request
from bs4 import BeautifulSoup


class Connector(metaclass=abc.ABCMeta):
    def __init__(self, is_secure):
        self.is_secure = is_secure
        self.port = self.factory_port()
        self.protocol = self.factory_protocol()

    @abc.abstractmethod
    def crawl(self):
        pass

    def scan(self, con_domain, con_path):
        url = self.protocol + '://' + con_domain \
              + ':' + str(self.port) + con_path
        print(url)
        return urllib.request.urlopen(url, timeout=10).read()

    @abc.abstractmethod
    def factory_protocol(self):
        pass

    @abc.abstractmethod
    def factory_port(self):
        pass


class HTTPConnector(Connector):
    """ Creates an HTTP Connector """

    def factory_protocol(self):
        if self.is_secure:
            return 'https'
        return 'http'

    def factory_port(self):
        if self.is_secure:
            return '443'
        return '80'

    def crawl(self, data):
        """ crawls web content """
        filenames = []
        soup = BeautifulSoup(data, "html.parser")
        links = soup.table.findAll('a')

        for link in links:
            filenames.append(link['href'])
        return '\n'.join(filenames)


class FTPConnector(Connector):
    def factory_protocol(self):
        return 'ftp'

    def factory_port(self):
        return '21'

    def crawl(self, data):
        # converting byte to string
        data = str(data, 'utf-8')
        lines = data.split('\n')
        filenames = []
        for line in lines:
            extract_line = line.split(None, 8)
            if len(extract_line) == 9:
                filenames.append(extract_line[-1])

        return '\n'.join(filenames)


if __name__ == "__main__":
    con_domain = 'ftp.freebsd.org'
    con_path = '/pub/FreeBSD/'

    con_protocol = input('Choose the protocol \
					(0-http, 1-ftp): ')

    if con_protocol == '0':
        is_secure = input('Use secure connection? (1-yes, 0-no):')
        if is_secure == '1':
            is_secure = True
        else:
            is_secure = False
        connector = HTTPConnector(is_secure)
    else:
        is_secure = False
        connector = FTPConnector(is_secure)

    try:
        data = connector.scan(con_domain, con_path)
    except urllib.error.URLError as e:
        print('Cannot access resource with this method', e)
    else:
        print(connector.crawl(data))

