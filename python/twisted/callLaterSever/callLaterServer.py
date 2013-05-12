import os, sys, time
from twisted.internet import protocol, reactor, task
import itertools
import redis
import time

#def sendScenario(self):
    #def sendelayed(d):
        #self.sendata(d)
        #self.factory.out_dump.write(d)
        #try:
            #timeout, data = next(sc)
            #reactor.callLater(timeout, sendelayed, data)
        #except StopIteration:
            #print "Scenario completed!"
            #self.transport.loseConnection()

#scenario = [(1, "Message after 1 sec!"), (4, "This after 4 secs"), (2, "End final after 2 secs")]

#sc = iter(self.scenario)
#timeout, data = next(self.sc)

#reactor.callLater(timeout, sendelayed, data)
#reactor.run()

dbconf = {'host':'192.168.1.199','port':6379,'db':0}
client  = redis.StrictRedis(**dbconf)
list_name = 'test_pop'


def f(s):
    print "done %s"% s

def g():
    print "do"

def printlist(list_name):
    while(client.llen(list_name)>0):
        item = client.lpop(list_name)
        print "processing item %s"% item
    else:
        print "nothing done"

def called(result = "called"):
    print result

task = task.deferLater(reactor, 3.5, f , "task")
task.addCallback(called)
task.addCallback(g)
#task = task.LoopingCall(printlist, (list_name))
#task.start(1)

reactor.run()

