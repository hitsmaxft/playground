from twisted.internet import reactor
from twisted.internet.protocol import Factory

import TwistedQuota.quoteproto
import TwistedQuota.quoters
import os
filequote = TwistedQuota.quoters.FortuneQuoter(map(lambda x: os.path.join('/tmp/test', x),os.listdir('/tmp/test')))
quoter = TwistedQuota.quoters.StaticQuoter(filequote)
factory =  TwistedQuota.quoteproto.QOTDFactory(quoter)
reactor.listenTCP(1234, factory)
reactor.run()

# 8007 is the port you want to run under. Choose something >1024
#endpoint = TCP4ServerEndpoint(reactor, 8007)
#endpoint.listen(factory)
#reactor.run()
