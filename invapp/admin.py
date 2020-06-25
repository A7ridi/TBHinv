from django.contrib import admin

from .models import Storage, Item_choices

from .forms import StorageForm

class StorageAdmin(admin.ModelAdmin):
    list_display = ('item', 'amount', 'expected_need_in', 'issue_date', 'location')
    form = StorageForm
    list_filter = ('item', )
    search_fields = ('item', )

admin.site.register(Storage, StorageAdmin)
admin.site.register(Item_choices)
