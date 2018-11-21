import json
import janrain.api_requests as api_requests

def set_attribute_constraints(auth_token, base_url, verbose, type_name, attribute_name, constraints):
    print(base_url)
    updated_attributes = api_requests.post(
        auth_token, base_url, verbose, "entityType.setAttributeConstraints?type_name=%s&attribute_name=%s&constraints=%s" % (type_name, attribute_name, constraints), ''
    )
    return updated_attributes