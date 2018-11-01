import json
import janrain.api_requests as api_requests


def get_flows(auth_token, base_url):
    flows_get_json = api_requests.get(auth_token, base_url, "flows")
    return flows_get_json


def get_flow(auth_token, base_url, flow_name):
    flow_get_json = api_requests.get(auth_token, base_url, "flows/%s" % flow_name)
    return flow_get_json


def duplicate_flow(auth_token, base_url, current_flow_name, new_flow_name):
    new_flow_name_json = json.loads('{"name": "%s"}' % new_flow_name)
    flow_copy_post_json = api_requests.post(auth_token, base_url, "flows/%s/copy" % current_flow_name, new_flow_name_json)
    return flow_copy_post_json
