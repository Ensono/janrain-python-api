import base64
import janrain.clients
import janrain.flows
import janrain.schema


class Api(object):
    def __init__(self, defaults={}):

        self.janrain_app_id = defaults['janrain_app']
        
        self.base_url = "https://v1.api.%s.janrain.com/config/%s" % (defaults['janrain_region'], defaults['janrain_app'])

        auth_string = "%s:%s" % (defaults['janrain_id'], defaults['janrain_secret'])
        self.auth_header = base64.b64encode(auth_string.encode("utf-8")).decode('utf-8')

    # CLIENTS
    # Lookup and configuration paths to the Janrain clients
    def get_clients(self):
        return janrain.clients.get_clients(self.auth_header, self.base_url)

    def get_client(self, client_id):
        return janrain.clients.get_client(self.auth_header, self.base_url, client_id)

    def create_client(self, client_config):
        return janrain.clients.create_client(self.auth_header, self.base_url, client_config)

    def update_client(self, client_id, client_config):
        return janrain.clients.update_client(self.auth_header, self.base_url, client_id, client_config)

    def delete_client(self, client_id):
        return janrain.clients.delete_client(self.auth_header, self.base_url, client_id)

    def get_client_settings(self, client_id):
        return janrain.clients.get_client_settings(self.auth_header, self.base_url, client_id)

    def update_client_settings(self, client_id, settings_config):
        return janrain.clients.update_client_settings(self.auth_header, self.base_url, client_id, settings_config)

    # FLOWS
    # Lookup and configuration paths to the Janrain flows
    def get_flows(self):
        return janrain.flows.get_flows(self.auth_header, self.base_url)

    def get_flow(self, flow_name):
        return janrain.flows.get_flow(self.auth_header, self.base_url, flow_name)

    def duplicate_flow(self, flow_name, new_flow_name):
        return janrain.flows.duplicate_flow(self.auth_header, self.base_url, flow_name, new_flow_name)

    # SCHEMAS
    # Lookup and configuration paths to the Janrain schemas
    def get_schemas(self):
        return janrain.schema.get_schemas(self.auth_header, self.base_url)

    def get_schema(self, schema_name):
        return janrain.schema.get_schema(self.auth_header, self.base_url, schema_name)

    def add_to_schema(self, schema_name, schema_element_name, schema_element_config):
        return janrain.schema.add_to_schema(self.auth_header, self.base_url, schema_name, schema_element_name, schema_element_config)