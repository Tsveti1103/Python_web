class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        return ', '.join(
            # take the field from the tuple and join them by ,
            f'{str_field}={getattr(self, str_field, None)}' for str_field in self.str_fields
        )