from django.contrib import admin
from player_polls.models import Team, Player, Comment

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from player_polls.models import EndUser

# --------------------------- End User -------------------------------|
class EndUserInline(admin.StackedInline):
    model = EndUser
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (EndUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# --------------------------- End User --------------------------------|

class PlayerInline(admin.TabularInline):
    model = Player


class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Location', {'fields': ['location']}),
        ('Team Branding', {'fields': ['primary_color', 'secondary_color'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'location')
    inlines = [PlayerInline]
    list_filter = ['name']
    search_fields = ['name']


class CommentInline(admin.TabularInline):
    model = Comment
    list_filter = ['player', 'user']
    search_fields = ['player', 'user']
    

class PlayerComments(admin.ModelAdmin):

    list_display = ('name', 'team', 'comment_count')
    inlines = [CommentInline]
    list_filter = ['team']
    search_fields = ['name']
                 

admin.site.register(Player, PlayerComments)
admin.site.register(Team, TeamAdmin)

