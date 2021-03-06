from django.contrib import messages

from .models import SlackOAuthRequest, SlackUser


def log_request(request, api_data):
        SlackOAuthRequest.objects.create(
            access_token=api_data.pop('access_token'),
            extras=api_data
        )
        return request, api_data


def debug(request, api_data):
    print("request: {}, api_data: {}".format(request, api_data))
    return request, api_data
