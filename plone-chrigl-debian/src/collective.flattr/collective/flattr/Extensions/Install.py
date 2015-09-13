from Products.CMFCore.utils import getToolByName

def uninstall(portal, reinstall=False):
    if not reinstall:
        setup_tools = getToolByName(portal, 'portal_setup')
        setup_tools.runAllImportStepsFromProfile(
            'profile-collective.flattr:uninstall')
