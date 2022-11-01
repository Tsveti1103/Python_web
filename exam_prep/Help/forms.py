from django import forms

from music.web.models import Profile, Album


# I can create base form. If the form has the same fields like the model I just use Meta class.
class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


# Inherit the base class
class ProfileCreateForm(BaseProfileForm):
    pass


"""
For delete the profile first add privet function that hide the fields
Then overwrite the save method. When save the form delete all things and the profile
"""


class ProfileDeleteForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Album.objects \
                .all() \
                .delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()
            field.required = False


# If I need a placeholders add them by widgets
class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    widgets = {
        'album_name': forms.TextInput(
            attrs={
                'placeholder': 'Album Name',
            }
        ),
        'artist': forms.TextInput(
            attrs={
                'placeholder': 'Artist',
            }
        ),
        'description': forms.Textarea(
            attrs={
                'placeholder': 'Description',
            }
        ),
        'image_url': forms.URLInput(
            attrs={
                'placeholder': 'Image URL',
            }
        ),
        'price': forms.NumberInput(
            attrs={
                'placeholder': 'Price',
            }
        ),
    }


class AlbumAddForm(BaseAlbumForm):
    pass


class AlbumEditForm(BaseAlbumForm):
    pass


"""
For delete album first add privet function that make the fields readonly
Then overwrite the save method. When save the form delete the thing"""


class AlbumDeleteForm(BaseAlbumForm):
    # better way
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.__set_disabled_fields()
    #
    # def save(self, commit=True):
    #     if commit:
    #         self.instance.delete()
    #
    #     return self.instance
    #
    # def __set_disabled_fields(self):
    #     for _, field in self.fields.items():
    #         field.widget.attrs['readonly'] = 'readonly'
