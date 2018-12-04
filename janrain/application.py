import janrain.api_requests as api_requests

def get_settings(auth_token, base_url, verbose):
    settings_get_json = api_requests.get(
        auth_token, base_url, verbose, "settings"
    )
    return settings_get_json

def update_settings(auth_token, base_url, verbose, update_settings):
    settings_update_json = api_requests.put(
        auth_token, base_url, verbose, "settings", update_settings
    )
    return settings_update_json

def get_settings_options(auth_token, base_url, verbose):
    settings_options_get_json = api_requests.get(
        auth_token, base_url, verbose, "settings/options"
    )
    return settings_options_get_json