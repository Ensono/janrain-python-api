import janrain.api_requests as api_requests

def get_translations(auth_token, base_url, verbose, flow_name):
    translations = api_requests.get(
        auth_token, base_url, verbose, "flows/%s/translations" % flow_name
    )
    return translations

def add_translation(auth_token, base_url, verbose, flow_name, translation):
    payload = [translation]
    updated_translation = api_requests.post(auth_token, base_url, verbose, "flows/%s/translations" % flow_name, payload)
    return updated_translation

def update_translation(auth_token, base_url, verbose, flow_name, translation):
    payload = [translation]
    updated_translation = api_requests.patch(auth_token, base_url, verbose, "flows/%s/translations" % flow_name, payload)
    return updated_translation