import janrain.api_requests as api_requests


def get_schemas(auth_token, base_url, verbose):
    schema_get_json = api_requests.get(
        auth_token, base_url, verbose, "schemas"
    )
    return schema_get_json


def get_schema(auth_token, base_url, verbose, schema_name):
    schema_get_json = api_requests.get(
        auth_token, base_url, verbose, "schemas/%s" % schema_name
    )
    return schema_get_json


def create_attribute(auth_token, base_url, verbose, schema_name, schema_element_name, schema_element_json):
    schema_create_attribute_json = api_requests.put(
        auth_token, base_url, verbose, "schemas/%s/%s" % (schema_name, schema_element_name), schema_element_json
    )
    return schema_create_attribute_json


def delete_attribute(auth_token, base_url, verbose, schema_name, schema_element_name):
    schema_delete_attribute_json = api_requests.delete(
        auth_token, base_url, verbose, "schemas/%s/%s" % (schema_name, schema_element_name)
    )
    return schema_delete_attribute_json

