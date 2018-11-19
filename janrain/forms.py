import json
import janrain.api_requests as api_requests

def update_form(auth_token, base_url, verbose, flow_name, form_name, form_config):
    update_form = api_requests.put(
        auth_token, base_url, verbose, "flows/%s/forms/%s" % (flow_name, form_name), form_config
    )
    return update_form