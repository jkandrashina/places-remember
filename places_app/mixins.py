from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect

class UserAccessMixin(AccessMixin):
    def test_func(self):
        raise NotImplementedError(
            '{} is missing the implementation of the test_func() method.'.format(self.__class__.__name__)
        )

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name()
            )

        user_test_result = self.test_func()
        if not user_test_result:
            return redirect('my_places')
        return super().dispatch(request, *args, **kwargs)