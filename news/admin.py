from django.contrib import admin

from .models import Editor,Article,tags

class EditorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email')
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'editor', 'pub_date')
    list_filter = ('editor', 'tags')
    search_fields = ('title', 'editor__name', 'tags__name')
    fieldsets = (
        (None, {'fields': ('title', 'post', 'editor', 'tags')}),
    )
    filter_horizontal = ('tags',)
    
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Editor, EditorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(tags, TagsAdmin)
