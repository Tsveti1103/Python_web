from django import forms

from music.web.models import Profile, Album


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(BaseProfileForm):
    pass


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


class AlbumDeleteForm(BaseAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
