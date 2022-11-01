
def apply_user_liked_photo(photo):
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def apply_likes_count(photo):
    # photolike_set (is query set) exists because model PhotoLike(in common) is related with Photo
    photo.likes_count = photo.photolike_set.count()
    return photo
