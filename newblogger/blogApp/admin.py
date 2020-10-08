from django.contrib import admin
from .models import blogger,blogcontent,blogcomment

admin.site.site_header = "iBlog Admin Panal!"
admin.site.index_title = "iBlogger"
# Register your models here.
admin.site.register(blogger)
admin.site.register(blogcontent)
admin.site.register(blogcomment)

