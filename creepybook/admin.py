from django.contrib import admin
from .models import UserProfile, Post, Friendship, Comment, Like, ChatRoom, MediaFile, Room


#

# Register your models here.

# I wrote this code

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'birthdate', 'website', 'profile_picture')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'timestamp')

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('follower', 'followed', 'timestamp')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'timestamp')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'timestamp')

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp')

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('post', 'file', 'timestamp', 'user')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

# end of code I wrote