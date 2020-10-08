from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class blogger(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=30)
    msg = models.TextField()
    re_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Message by "+str(self.email)

class blogcontent(models.Model):
    blog_s_no = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    slug = models.CharField(max_length=100)
    blog_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title

class blogcomment(models.Model):
    s_no = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(blogcontent, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:20]+ " by " +str(self.user)


    # def __str__(self):
    #     return self.comment_date

# class blogreplay(models.Model):
#     comment_no = models.AutoField(primary_key=True)
#     comment_content = models.TextField()
