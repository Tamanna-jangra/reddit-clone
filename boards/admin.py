from django.contrib import admin
from .models import SubReddits,Subscriptions,Posts,Comments,Votes
# Register your models here.
admin.site.register(SubReddits)
admin.site.register(Subscriptions)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Votes)