import janrain.api_requests as api_requests


def get_schemas(auth_token, base_url):
    schema_get_json = api_requests.get(auth_token, base_url, "schemas")
    return schema_get_json


def get_schema(auth_token, base_url, schema_name):
    schema_get_json = api_requests.get(auth_token, base_url, "schemas/%s" % schema_name)
    return schema_get_json


def add_to_schema(auth_token, base_url, schema_name, schema_element_name, schema_element_json):
    schema_add_json = api_requests.put(auth_token, base_url, "schemas/%s/%s" % (schema_name, schema_element_name), schema_element_json)
    return schema_add_json

