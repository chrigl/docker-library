import logging
from zope.interface import implements, Interface

from Products.ATContentTypes.interfaces import IATTopic, IATFolder
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_hasattr

from collective.geo.mapwidget.browser.widget import MapWidget
from collective.geo.trackview.interfaces import IGisFile
from collective.geo.trackview import GeoTrackViewMessageFactory as _


logger = logging.getLogger('collective.geo.trackview.browser.RouteView')


class IRouteView(Interface):
    """
    Route view interface
    """


class RouteView(BrowserView):
    """
    Route browser view
    """
    implements(IRouteView)

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

    def getRoute(self):
        """ Returns a list of IGisFile files """
        query = {'object_provides': IGisFile.__identifier__}
        if IATTopic.providedBy(self.context):
            return self.context.queryCatalog(**query)
        elif IATFolder.providedBy(self.context)\
            or IPloneSiteRoot.providedBy(self.context):
            return self.context.getFolderContents(query)
        else:
            logger.info('Unsupported container type')
        return []
