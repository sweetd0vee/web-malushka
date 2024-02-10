from django.shortcuts import redirect
from django.urls import reverse

from .python_auth import verify_headers, make_token_verifier
from rest_framework.permissions import BasePermission

verificator = make_token_verifier(issuer="https://sso-test.o3.ru/auth/realms/dev",
                                  client_id="k8s.web-malushka")

authorization_sso = 'https://sso-test.o3.ru/auth/realms/dev/protocol/openid-connect/auth?client_id=k8s.web-malushka&redirect_uri=http%3A%2F%2Fweb-malushka-test.dev.a.o3.ru'


class IsAdministrator(BasePermission):

    def has_permission(self, request, view):
        vf = verify_headers(request.headers, verificator)
        if not vf["username"]:
            return redirect(reverse(authorization_sso))

        if "administrator" not in vf["roles"]:
            return redirect('malushka-home')

        else:
            return True


class IsGuest(BasePermission):

    def has_permission(self, request, view):
        vf = verify_headers(request.headers, verificator)
        if not vf["username"]:
            return redirect(reverse(authorization_sso))

        elif "administrator" not in vf["roles"] and "ClickHouseSuperAdmin" not in vf[
            "roles"] and "ClickHouseAdmin" not in \
                vf["roles"] and "Calc3Editor" not in vf["roles"] and "guest" not in vf["roles"]:
            return redirect('malushka-home')

        else:
            return True


def check_click_admin(view):
    def wrapper(request, *args, **kwargs):
        vf = verify_headers(request.headers, verificator)
        if "administrator" not in vf["roles"] and "ClickHouseSuperAdmin" not in vf["roles"] and "ClickHouseAdmin" not in vf["roles"]:
            return redirect('malushka-home')

        else:
            return view(request, *args, **kwargs)

    return wrapper


def check_guest(view):
    def wrapper(request, *args, **kwargs):
        vf = verify_headers(request.headers, verificator)
        if "administrator" not in vf["roles"] and "ClickHouseSuperAdmin" not in vf["roles"] and "ClickHouseAdmin" not in \
                vf["roles"] and "Calc3Editor" not in vf["roles"] and "guest" not in vf["roles"]:
            return redirect('malushka-home')

        else:
            return view(request, *args, **kwargs)

    return wrapper
