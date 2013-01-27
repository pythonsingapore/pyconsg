"""Views for the ``pyconsg`` project."""
from account.views import LogoutView


class PyconSGLogoutView(LogoutView):
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
