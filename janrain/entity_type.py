import json
import janrain.api_requests as api_requests

def set_access_schema(auth_token, base_url, verbose, type_name, for_client_id, access_type, attributes):
    schema = api_requests.post(
        auth_token, base_url, verbose, "entityType.setAccessSchema?type_name=%s&for_client_id=%s&access_type=%s&attributes=%s" % (type_name, for_client_id, access_type, attributes), ''
    )
    return schema

def set_attribute_constraints(auth_token, base_url, verbose, type_name, attribute_name, constraints):
    updated_attributes = api_requests.post(
        auth_token, base_url, verbose, "entityType.setAttributeConstraints?type_name=%s&attribute_name=%s&constraints=%s" % (type_name, attribute_name, constraints), ''
    )
    return updated_attributes