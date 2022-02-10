from django.contrib import admin

from busa.models import Executive, cabinet, gallery, home_slide, latest_news, parliament, speakership

# Register your models here.

@admin.register(home_slide)
class HomeSlideAdmin(admin.ModelAdmin):
    list_display = ("s_title", "s_description", "s_button", "s_image")
    list_filter = ("s_button",)
    fields = ("s_title", "s_description", "s_button", "s_image")

# latest news 
@admin.register(latest_news)
class latest_news(admin.ModelAdmin):
    list_display = ("ln_title", "ln_description","ln_image")
    list_filter = ("ln_title",)
    fields = ("ln_title", "ln_description", "ln_image")

# gallery

@admin.register(gallery)
class Gallery(admin.ModelAdmin):
    list_display = ("g_image",)

# guild leadership executives

@admin.register(Executive)
class GuildExecutives(admin.ModelAdmin):
    list_display = ("Names", "E_Position","E_picture")
    list_filter = ("E_Position",)
    fields = ("Names", "E_Position","E_picture")

# guild cabinet ministers

@admin.register(cabinet)
class GuildCabinet(admin.ModelAdmin):
    list_display = ("Name", "position", "picture")
    list_filter = ("position",)
    fields = ("Name", "position", "picture")

#parliament 
@admin.register(speakership)
class Speakership(admin.ModelAdmin):
    list_display = ("Name", "Position", "m_picture")
    list_filter = ("Position",)
    fields = ("Name", "Position", "m_picture")


#parliamentarian 
@admin.register(parliament)
class Parliament(admin.ModelAdmin):
    list_display = ("name", "departement", "m_picture")
    list_filter = ("departement",)
    fields = ("name", "departement", "m_picture")

