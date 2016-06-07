from gevent import monkey; monkey.patch_all()
import urllib2
import threading
import random
import time
import gevent
import jsonpickle


def randomInteger(Range):
    rand = random.Random()
    return int(rand.random() * Range)


class ProxyServer:
    def __init__(self, host, port, type="http"):
        self.delay = None
        self.host = host
        self.port = port
        self.Type = type
        self.valid = True

    def __unicode__(self):
        return "< %s : %s | %s >" % (self.host, self.port, self.Type)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def validate(self):
        gevent.spawn(self._validate_internal).start()

    def _validate_internal(self):
        try:
            start = time.time()
            proxy_handler = urllib2.ProxyHandler({self.Type: "%s:%s" % (self.host, self.port)})
            opener = urllib2.build_opener(proxy_handler)
            resp = opener.open("http://www.baidu.com", timeout=5)
            self.delay = time.time() - start
            print str(self) + "delay is : " + str(self.delay)
            print str(resp)
            self.valid = True
        except Exception,e:
            print str(e)
            self.valid = False


class ProxyManager:
    def __init__(self):
        self.servers = []
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def get_proxy(self):
        return self.servers[randomInteger(len(self.servers))]

    def run(self):
        while (True):
            time.sleep(10)
            for server in self.servers:
                server.validate()
            self.servers = filter(lambda x: x.valid, self.servers)

    def load_server(self, server):
        if isinstance(server, ProxyServer):
            self.servers.append(server)
        else:
            raise Exception("Wrong Class Type!")

    def size(self):
        return self.__len__()

    def __len__(self):
        return len(self.servers)

    def load_servers(self):
        resp = urllib2.urlopen("http://qsrdk.daili666api.com/ip/?tid=558571735483018&num=100&delay=3&category=2&protocol=http&foreign=only&format=json")
        servers = jsonpickle.loads(resp.read())
        for sver in servers:
            server  = ProxyServer(sver['host'],sver['port'])
            print("load " + str(server) + " into manager")
            self.load_server(server)


if __name__ == '__main__':
    pm = ProxyManager()
    pm.load_servers()
    time.sleep(40)
    #print server.valid
