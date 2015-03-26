class Carta(object):
    insure = False

    def __init__(self, numero, nipe):
        self.numero = numero
        self.nipe = nipe
        self.maior, self.menor = self._points()

    def __eq__(self, other):
        return (self.nipe == other.nipe and
                self.numero == other.numero and
                self.maior == other.maior and
                self.menor == other.menor)

    def __repr__(self):
        return "{__class__.__name__}(nipe={nipe!r}, numero={numero!r})".format(__class__=self.__class__, **self.__dict__)

    def __str__(self):
        return "{numero}{nipe}".format(**self.__dict__)
