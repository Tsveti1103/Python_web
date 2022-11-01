from django.contrib import admin

from petstagram.photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'pets')

    # take pets
    @staticmethod
    def pets(current_photo_obj):
        # get all pets through tagged_pets because it is related to pet
        tagged_pets = current_photo_obj.tagged_pets.all()
        # if we have pets show their names join with ,
        if tagged_pets:
            return ', '.join(p.name for p in tagged_pets)
        # if not show No Pets
        return 'No Pets'
