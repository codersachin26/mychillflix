from django.contrib import admin
from .models import Web_series,Series_info,Seasons,Episode,Episode_file,Season_pics



class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'web_series'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)










admin.site.register(Web_series, MultiDBModelAdmin)
admin.site.register(Series_info, MultiDBModelAdmin)
admin.site.register(Seasons, MultiDBModelAdmin)
admin.site.register(Episode, MultiDBModelAdmin)
admin.site.register(Episode_file, MultiDBModelAdmin)
admin.site.register(Season_pics, MultiDBModelAdmin)