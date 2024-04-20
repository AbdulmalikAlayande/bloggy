from django.db import models
from django.db.models import CASCADE, PROTECT
from auths.models import User
from commons.models import AbstractCommonModel
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Blogger(User):

    first_name = models.CharField(verbose_name=_('First Name'), unique=True, max_length=120, null=False, blank=False)
    last_name = models.CharField(verbose_name=_('First Name'), unique=True, max_length=120, null=False, blank=False)
    profile_image_url = models.URLField(_('Profile Image Url'), max_length=1000)

    class Meta:
        verbose_name = _('Blogger')
        verbose_name_plural = _('Bloggers')

class Post(AbstractCommonModel):

    class Status(models.TextChoices):
        DRAFT = "draft", _("Draft")
        PUBLISHED = "published", _("Published")
        REMOVED = "removed", _("Removed")

    title = models.CharField(verbose_name=_("Title"), max_length=255)
    body = models.TextField(verbose_name=_("Body"))
    blogger = models.ForeignKey(verbose_name=_('Blogger'), to=Blogger, on_delete=CASCADE)
    status = models.CharField(verbose_name=_("Status"), choices=Status.choices, default=Status.DRAFT)

class Media(AbstractCommonModel):
    cloud_url = models.URLField()
    post = models.OneToOneField(verbose_name=_('Post'), to=Post, on_delete=CASCADE)

class Comment(AbstractCommonModel):
    author = models.ForeignKey(verbose_name=_("Author"), to=Blogger, on_delete=CASCADE)
    post = models.ForeignKey(verbose_name=_("Post"), to=Post, on_delete=CASCADE)
    body = models.TextField(verbose_name=_('Body'))
    is_deleted = models.BooleanField(verbose_name=('Deleted'), default=False)

    def __str__(self) -> str:
        return f"{self.author.username}'s comment on {self.post.blogger.username}'s post - {self.post.title}"

class Like(AbstractCommonModel):
    post = models.ForeignKey(verbose_name=("Post"), to=Post, on_delete=CASCADE)
    amount = models.IntegerField(_("Number Of Likes"))

class Tag(AbstractCommonModel):
    pass
