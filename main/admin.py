from django.contrib import admin
from main.models import Quote, ScrapyItem

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', )


class ScrapyItemAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'data', 'date', )
# Register your models here.
admin.site.register(Quote, QuoteAdmin)
admin.site.register(ScrapyItem, ScrapyItemAdmin)

