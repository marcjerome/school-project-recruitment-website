from .models import Membership, Notification
from django.db.models.signals import post_save

def add_notification(sender, **kwargs):
    if not kwargs['created']:
        member = kwargs['instance']
       
        if member.is_approve:
            project = member.project

            notification = Notification.objects.filter(project=project).first()
            if notification is not None:
                member.user.notifications.add(notification)
            else:
                notification = Notification.objects.create(project=project, message="You were approved as member of this project: " + project.name)
                member.user.notifications.add(notification)
                
post_save.connect(add_notification, sender=Membership)


