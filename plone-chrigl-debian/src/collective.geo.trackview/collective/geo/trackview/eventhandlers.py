from zope.interface import alsoProvides
from zope.interface import noLongerProvides
from zope.component import getAdapters
from collective.geo.trackview.interfaces import ITypeRecognition
from Products.CMFPlone.utils import safe_hasattr


def mark_file(ob, event):
    if safe_hasattr(ob, 'getFile'):
        obfile = ob.getFile()
        reindex = False

        set_track_view = False
        for name, adapter in getAdapters((obfile,), ITypeRecognition):
            iface = adapter.getIface()
            if adapter.isOfType():
                if not iface.providedBy(ob):
                    alsoProvides(ob, iface)
                    reindex = True
                # if there is set an interface, I also want to switch the view
                set_track_view = True
                # ok, found the type. do not check any more.
                break
            else:
                if iface.providedBy(ob):
                    # remove the marker if the file type changed!
                    noLongerProvides(ob, iface)
                    reindex = True

        if set_track_view:
            # if at least one interface is set, switch the view.
            ob.setLayout('track_view')
        else:
            # reset the view
            ob.setLayout(ob.getDefaultLayout())
        # we need to reindex the object, because ObjectEditedEvent is fired
        # after reindexing
        if reindex:
            # TODO: just reindex object_provides?
            ob.reindexObject()
