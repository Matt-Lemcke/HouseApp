from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin

from houseapp.models import Membership


class HouseNameChanger(MiddlewareMixin):
    def process_response(self, request, response):
        name = 'House Name'

        print(request.user)

        if request.user.is_authenticated:
            name = Membership.objects.get(person=request.user).house

        response.content = response.content.replace('House Name', name)
        return response
