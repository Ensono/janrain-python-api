import json
import janrain.api_requests as api_requests

def update_template(auth_token, base_url, verbose, flow_name, flow_locale, template_name, template_body):
    update_form = api_requests.put(
        auth_token, base_url, verbose, "flows/%s/locales/%s/mailTemplates/%s" % (flow_name, flow_locale, template_name), template_body
    )
    return update_form