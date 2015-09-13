from zope.interface import Interface


class ITypeRecognition(Interface):
    """ Adapters implementing this, can check for GIS data """

    def isOfType():
        """ Returns True if self.file is of the asked type """

    def getIface():
        """ Returns Interface class """


class IGisFile(Interface):
    """ Marker interface for files containing GIS data.
    Should just be used in the browser page definition!!! """


class IGpxFile(IGisFile):
    """ Marker interface for files containing GPX data """
