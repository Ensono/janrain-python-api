import json
import janrain.api_requests as api_requests


def get_flows(auth_token, base_url):
    flows_get_json = api_requests.get(
        auth_token, base_url, "flows"
    )
    return flows_get_json


def get_flow(auth_token, base_url, flow_name):
    flow_get_json = api_requests.get(
        auth_token, base_url, "flows/%s" % flow_name
    )
    return flow_get_json


def duplicate_flow(auth_token, base_url, current_flow_name, new_flow_name):
    new_flow_name_json = json.loads('{"name": "%s"}' % new_flow_name)
    flow_copy_json = api_requests.post(
        auth_token, base_url, "flows/%s/copy" % current_flow_name, new_flow_name_json
    )
    return flow_copy_json


def get_flow_fields(auth_token, base_url, flow_name):
    flow_fields_get_json = api_requests.get(
        auth_token, base_url, "flows/%s/fields" % flow_name
    )
    return flow_fields_get_json


def get_flow_field(auth_token, base_url, flow_name, field_name):
    flow_fields_get_json = api_requests.get(
        auth_token, base_url, "flows/%s/fields/%s" % (flow_name, field_name)
    )
    return flow_fields_get_json


def add_flow_field(auth_token, base_url, flow_name, locale, field_config):
    flow_add_field_json = api_requests.post(
        auth_token, base_url, "flows/%s/locales/%s/fields" % (flow_name, locale), field_config
    )
    return flow_add_field_json


def update_flow_field(auth_token, base_url, flow_name, locale, field_name, field_config):
    flow_update_field_json = api_requests.put(
        auth_token, base_url, "flows/%s/locales/%s/fields/%s" % (flow_name, locale, field_name), field_config
    )
    return flow_update_field_json


def delete_flow_field(auth_token, base_url, flow_name, field_name):
    flow_delete_field_json = api_requests.delete(
        auth_token, base_url, "flows/%s/fields/%s" % (flow_name, field_name)
    )
    return flow_delete_field_json


def create_flow_form(auth_token, base_url, flow_name, form_name, form_data):
    flow_create_form_json = api_requests.put(
        auth_token, base_url, "flows/%s/forms/%s" % (flow_name, form_name), form_data
    )
    return flow_create_form_json
