from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def admin_required(view_func):
    @login_required
    def wrapped_view(request, *args, **kwargs):
        if not (request.user.is_admin or request.user.is_superadmin):
            return HttpResponseForbidden("You are not authorized to access this page.")
        return view_func(request, *args, **kwargs)
    return wrapped_view
