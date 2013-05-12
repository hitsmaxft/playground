from random import choice

from zope.interface import implements

from TwistedQuotes import quoteproto

#from zope.interface import Interface

from twisted.internet.protocol import Factory, Protocol


class StaticQuoter:
    """
    Return a static quote.
    """

    implements(quoteproto.IQuoter)

    def __init__(self, quote):
        self.quote = quote


    def getQuote(self):
        return self.quote



class FortuneQuoter:
    """
    Load quotes from a fortune-format file.
    """
    implements(quoteproto.IQuoter)

    def __init__(self, filenames):
        self.filenames = filenames


    def getQuote(self):
        quoteFile = file(choice(self.filenames))
        quotes = quoteFile.read().split('\n%\n')
        quoteFile.close()
        return choice(quotes)





class IQuoter(Interface):
    """
    An object that returns quotes.
    """
    def getQuote():
        """
        Return a quote.
        """



class QOTD(Protocol):
    def connectionMade(self):
        self.transport.write(self.factory.quoter.getQuote()+'\r\n')
        self.transport.loseConnection()



class QOTDFactory(Factory):
    """
    A factory for the Quote of the Day protocol.

    @type quoter: L{IQuoter} provider
    @ivar quoter: An object which provides L{IQuoter} which will be used by
        the L{QOTD} protocol to get quotes to emit.
    """
    protocol = QOTD

    def __init__(self, quoter):
        self.quoter = quoter
