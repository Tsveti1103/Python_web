from petstagram.pets.models import Pet


def get_pet_by_name_adn_user(pet_slug, username):
    #     TODO fix username whe auth
    return Pet.objects.get(slug=pet_slug)
