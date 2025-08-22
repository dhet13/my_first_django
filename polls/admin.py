from django.contrib import admin
from .models import Article, Memo

@admin.register(Article)
class AritcleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    list_filter = ['created_at']

@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_important', 'created_at']
    list_filter = ['is_important', 'created_at']
    search_fields = ['title', 'content']
    list_editable = ['is_important']
