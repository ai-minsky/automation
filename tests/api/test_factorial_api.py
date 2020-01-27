#  Copyright (c) 2020. This code has been written by Andrei Izbavitelev
import math
import pytest
import requests


def print_request(request):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '============Request============',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
    )


def print_response(response):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '============Response============',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text)
    )

@pytest.mark.api
@pytest.mark.parametrize("number", [i for i in range(0, 171)])
def test_api(number):
    url = "http://qainterview.pythonanywhere.com/factorial?Type=application/x-www-form-urlencoded&Content-Type=UTF-8"

    payload = 'number=' + str(number)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    resp = requests.request("POST", url, headers=headers, data=payload)
    print_request(resp.request)

    assert resp.status_code == 200
    assert resp.json()['answer'] == math.factorial(number)
    print_response(resp)
