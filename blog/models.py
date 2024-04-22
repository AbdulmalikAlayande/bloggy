from django.db import models
from django.db.models import CASCADE
from django.utils.translation import gettext_lazy as _

from auths.models import Blogger
from commons.models import AbstractCommonModel


# Create your models here

class Post(AbstractCommonModel):

    class Status(models.TextChoices):
        DRAFT = "draft", _("Draft")
        PUBLISHED = "published", _("Published")
        REMOVED = "removed", _("Removed")

    title = models.CharField(verbose_name=_("Title"), max_length=255)
    body = models.TextField(verbose_name=_("Body"))
    blogger = models.ForeignKey(verbose_name=_('Blogger'), to=Blogger, on_delete=CASCADE)
    status = models.CharField(verbose_name=_("Status"), choices=Status.choices, default=Status.DRAFT)

    def __str__(self) -> str:
        return f"{self.title} - {self.blogger.first_name} {self.blogger.last_name}"
class Media(AbstractCommonModel):
    cloud_url = models.URLField()
    post = models.OneToOneField(verbose_name=_('Post'), to=Post, on_delete=CASCADE)

    def __str__(self) -> str:
        return f"{self.post.title} - {self.post.blogger.first_name} {self.post.blogger.last_name}"


class Comment(AbstractCommonModel):
    author = models.ForeignKey(verbose_name=_("Author"), to=Blogger, on_delete=CASCADE)
    post = models.ForeignKey(verbose_name=_("Post"), to=Post, on_delete=CASCADE)
    body = models.TextField(verbose_name=_('Body'))
    is_deleted = models.BooleanField(verbose_name=_('Deleted'), default=False)

    def __str__(self) -> str:
        return f"{self.author.username}'s comment on {self.post.blogger.username}'s post - {self.post.title}"

class Like(AbstractCommonModel):
    post = models.ForeignKey(verbose_name=_("Post"), to=Post, on_delete=CASCADE)
    amount = models.IntegerField(_("Number Of Likes"))

    def __str__(self) -> str:
        return f"{self.post.title} - {self.amount}"

class Tag(AbstractCommonModel):
    pass
