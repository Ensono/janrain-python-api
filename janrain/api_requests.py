import json
import requests


# GET
def get(auth_token, base_url, url):
    api_url = "%s/%s" % (base_url, url)
    print("Calling GET on %s" % api_url)
    get_response = requests.get(api_url, headers={'Authorization': 'Basic %s' % auth_token})
    api_response = json.loads(get_response.text)
    return api_response


# PUT
def put(auth_token, base_url, url, data_payload):
    api_url = "%s/%s" % (base_url, url)
    print("Calling PUT on %s" % api_url)
    put_response = requests.put(api_url,
       headers={
        'Authorization': 'Basic %s' % auth_token,
        'Content-Type': 'application/json'
        },
        json=data_payload
    )
    api_response = json.loads(put_response.text)
    return api_response


# POST
def post(auth_token, base_url, url, data_payload):
    api_url = "%s/%s" % (base_url, url)
    print("Calling POST on %s" % api_url)
    post_response = requests.post(api_url,
       headers={
        'Authorization': 'Basic %s' % auth_token,
        'Content-Type': 'application/json'
        },
        json=data_payload
    )
    if post_response.text != "":
        api_response = json.loads(post_response.text)
        return api_response
    elif post_response.status_code == 200:
        return True
    else:
        return False


# DELETE
def delete(auth_token, base_url, url):
    api_url = "%s/%s" % (base_url, url)
    print("Calling DELETE on %s" % api_url)
    delete_response = requests.delete(api_url, headers={'Authorization': 'Basic %s' % auth_token})
    if delete_response.text != "":
        api_response = json.loads(delete_response.text)
        return api_response
    elif delete_response.status_code == 204:
        return True
    else:
        return False
