from django.shortcuts import render, redirect
from django.urls import reverse
from pyperclip import copy

from petstagram.common.models import PhotoLike
from petstagram.common.utils import get_user_liked_photos, get_photo_url
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo



def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    context = {
        'photos': photos,
    }
    return render(request, 'common/home-page.html', context)


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photos(photo_id)
    # if user liked this photo already delete it(dislike it)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        # if user is not like this photo already create it(like it)
        # Variant 1
        PhotoLike.objects.create(
            photo_id=photo_id,
        )
    return redirect(get_photo_url(request, photo_id))

    # # Variant 2
    # photo_like = PhotoLike(
    #     photo_id=photo_id,
    # )
    # photo_like.save()


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id
    })
    copy(get_photo_url(request, photo_id))
    return redirect(get_photo_url(request, photo_id))
