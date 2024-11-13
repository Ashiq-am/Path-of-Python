import http.client
from ftplib import FTP


class SimpleFactory(object):

    @staticmethod
    def build_connection(protocol):
        if protocol == 'https':
            return http.client.HTTPSConnection('www.python.org')
        elif protocol == 'ftp':
            return FTP('ftp1.at.proftpd.org')
        else:
            raise RuntimeError('Unknown protocol')


if __name__ == '__main__':

    input_protocol = input('Which protocol to use? (https or ftp):')
    protocol = SimpleFactory.build_connection(input_protocol)

    if input_protocol == 'https':
        protocol.request("GET", "/")
        resp = protocol.getresponse()
        print(resp.status, resp.reason)

    elif input_protocol == 'ftp':
        resp = protocol.login()
        print(resp)
