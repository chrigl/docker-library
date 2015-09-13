from elementtree.ElementTree import XML
from zope.interface import implements
from zope.interface import Interface
from zope.component import adapts
from collective.geo.trackview.interfaces import ITypeRecognition
from collective.geo.trackview.interfaces import IGpxFile


class GpxRecognition(object):
    implements(ITypeRecognition)
    adapts(Interface)

    def __init__(self, file):
        self.file = file

    def isOfType(self):
        """ Returns True if self.data is a GPX file """
        if self.file.getContentType() != 'text/xml':
            return False
        tree = XML(self.file.data)
        if u'http://www.topografix.com/GPX' in tree.tag:
            return True
        return False

    def getIface(self):
        """ This is a IGpxFile!!! """
        return IGpxFile
