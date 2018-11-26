import janrain.api_requests as api_requests


def get_clients(auth_token, base_url, verbose):
    clients_get_json = api_requests.get(
        auth_token, base_url, verbose, "clients"
    )
    return clients_get_json


def get_client(auth_token, base_url, verbose, client_id):
    client_get_json = api_requests.get(
        auth_token, base_url, verbose, "clients/%s" % client_id
    )
    return client_get_json


def create_client(auth_token, base_url, verbose, client_config):
    client_create_json = api_requests.post(
        auth_token, base_url, verbose, "clients", client_config
    )
    return client_create_json


def update_client(auth_token, base_url, verbose, client_id, update_config):
    client_update_json = api_requests.put(
        auth_token, base_url, verbose, "clients/%s" % client_id, update_config
    )
    return client_update_json


def delete_client(auth_token, base_url, verbose, client_id):
    client_delete_json = api_requests.delete(
        auth_token, base_url, verbose, "clients/%s" % client_id
    )
    return client_delete_json


def get_client_settings(auth_token, base_url, verbose, client_id):
    client_setting_get_json = api_requests.get(
        auth_token, base_url, verbose, "clients/%s/settings" % client_id
    )
    return client_setting_get_json


def update_client_settings(auth_token, base_url, verbose, client_id, settings_config):
    client_setting_update_json = api_requests.put(
        auth_token, base_url, verbose, "clients/%s/settings" % client_id, settings_config
    )
    return client_setting_update_json

def update_client_setting(auth_token, base_url, verbose, client_id, setting_key, setting_value):
    client_setting_update_json = api_requests.post(
        auth_token, base_url, verbose, "settings/set?for_client_id=%s&key=%s&value=%s" % (client_id, setting_key, setting_value), ""
    )
    return client_setting_update_json