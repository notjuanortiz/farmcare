from allauth.account.adapter import DefaultAccountAdapter


class FarmcareAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit=commit)
        data = form.cleaned_data
        user.zipcode = data.get('zipcode')
        user.crops = data.get('crops')
        user.save()
        return user