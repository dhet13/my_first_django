from django.contrib import admin
from .models import DailyPhoto

@admin.register(DailyPhoto)
class DailyPhotoAdmin(admin.ModelAdmin):
    """DailyPhoto 관리자 설정"""
    list_display = ['title', 'author', 'photo_date', 'category', 'is_public', 'created_at']
    list_filter = ['category', 'is_public', 'photo_date', 'created_at']
    search_fields = ['title', 'description', 'author__username']
    list_editable = ['is_public']
    date_hierarchy = 'photo_date'
    ordering = ['-created_at']
    
    # 읽기 전용 필드
    readonly_fields = ['thumbnail', 'created_at', 'updated_at']
    
    # 필드셋 구성
    fieldsets = (
        ('기본 정보', {
            'fields': ('title', 'author', 'photo', 'thumbnail')
        }),
        ('상세 정보', {
            'fields': ('description', 'photo_date', 'category', 'is_public')
        }),
        ('메타 정보', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
