from Products.CMFPlone.utils import safe_hasattr
from collective.geo.mapwidget.maplayers import MapLayer
from collective.geo.trackview import GeoTrackViewMessageFactory as _


js_tpl = u"""function() {
                return new OpenLayers.Layer.Vector("%s", {
                    protocol: new OpenLayers.Protocol.HTTP({
                      url: "%s",
                      format: %s
                      }),
                    strategies: [new OpenLayers.Strategy.Fixed()],
                    projection: new OpenLayers.Projection("EPSG:4326")
                  });
                }"""


class TrackMapLayer(MapLayer):

    name = u'track'
    Title = _(u'Track')

    @property
    def jsfactory(self):
        file_format = 'new OpenLayers.Format.GPX({extractWaypoints: true, extractRoutes: true, extractAttributes: true})'
        if not safe_hasattr(self.view, 'getRoute'):
            title = self.context.title_or_id() + ' (' + self.Title + ') '
            return js_tpl % (title, self.context.absolute_url(), file_format)
        else:
            tracks = []
            brains = self.view.getRoute()
            for brain in brains:
                tracks.append(js_tpl % (brain.Title,
                    brain.getURL(), file_format))
            return ',\n'.join(tracks)
