from plone.app.layout.viewlets.common import ViewletBase
from plone.app.discussion.interfaces import IConversation
from Products.CMFPlone.utils import safe_hasattr

class CommentsViewlet(ViewletBase):

    def update(self):
        show = False
        num_comments = 0
        first_comment = self.context.absolute_url()
        if safe_hasattr(self.context, 'isDiscussable')\
            and self.context.isDiscussable()\
            and self.context.absolute_url() not in self.request.get('URL'):
            conversations = IConversation(self.context)
            num_comments = conversations.total_comments
            if num_comments > 0:
                try:
                    comment_id = conversations.getThreads().next()['id']
                    first_comment = '%s#%s' % (first_comment, comment_id)
                except StopIteration:
                    pass
                show = True
        self.show = show
        self.num_comments = num_comments
        self.first_comment = first_comment
