from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.geo.trackview import GeoTrackViewMessageFactory as _
from collective.geo.mapwidget.browser.widget import MapWidget


class ITrackView(Interface):
    """
    Track view interface
    """


class TrackView(BrowserView):
    """
    Track browser view
    """
    implements(ITrackView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

        self.mapwidget = MapWidget(self, self.request, self.context)
        self.mapwidget._layers = ['track']
        self.mapwidget.mapid = 'default-cgmap'

        self.mapfields = [self.mapwidget]

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()
