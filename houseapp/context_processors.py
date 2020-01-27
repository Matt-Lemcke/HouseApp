from houseapp.models import Membership


def add_variable_to_context(request):
    name = 'House Name'
    members = ['placeholder']
    address = 'placeholder'

    # try:
    #     if request.user.is_authenticated:
    #         name = Membership.objects.get(person=request.user).house
    # except Exception:
    #     name = 'No House'

    # return {
    #     'housename': name
    # print(request.user)
    
    try:
        if request.user.is_authenticated:
            name = Membership.objects.get(person=request.user).house
            members = Membership.objects.get(
                person=request.user).house.members.all()
            address = Membership.objects.get(
                person=request.user).house.address
    except Exception:
        name = ''
        members = ['']
        address = ''
    return {
        'housename': name,
        'members': members,
        'address': address
    }
