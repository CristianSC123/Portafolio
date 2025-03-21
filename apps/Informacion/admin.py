from django.contrib import admin
from .models import Informacion, SocialMedia

@admin.register(Informacion)
class InformacionAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'email', 'phone', 'urlWeb', 'specialty')
    search_fields = ('fullName', 'email', 'phone')
    list_filter = ('email',)

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'idInformation')
    search_fields = ('name', 'url')
    list_filter = ('idInformation',)

