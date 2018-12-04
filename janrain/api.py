import base64
import janrain.application
import janrain.clients
import janrain.flows
import janrain.schema
import janrain.forms
import janrain.entity_type
import janrain.templates
import janrain.translations


class Api(object):
    def __init__(self, defaults={}):

        self.verbose = False
        if 'verbose' in defaults:
            self.verbose = defaults['verbose']
        self.janrain_app_id = defaults['janrain_app']
        
        self.base_url = "https://v1.api.%s.janrain.com/config/%s" % (defaults['janrain_region'], defaults['janrain_app'])
        self.capture_base_url = "https://%s.janraincapture.com" % defaults['janrain_registration_realm']

        auth_string = "%s:%s" % (defaults['janrain_id'], defaults['janrain_secret'])
        self.auth_header = base64.b64encode(auth_string.encode("utf-8")).decode('utf-8')

    # APPLICATION
    # Manage application settings
    def get_application_settings(self):
        """
        Get all application settings for a Janrain application

        Args:
          * None

        Returns:
          * JSON Object: List of all settings about a Janrain application
        """
        return janrain.application.get_settings(self.auth_header, self.base_url, self.verbose)

    def update_application_settings(self, update_application_settings):
        """
        Update application settings to a Janrain application

        Args:
          * None

        Returns:
          * JSON Object: List of all settings about a Janrain application
        """

        application_settings_options = self.get_application_settings_options()
        application_settings_options_dictionary = {}
        for application_setting_option in application_settings_options:
            application_settings_options_dictionary[application_setting_option['name']] = application_setting_option['group']

        existing_application_settings = self.get_application_settings()

        for update_application_setting_name in update_application_settings:
            isCustom = False
            if update_application_setting_name in application_settings_options_dictionary:
                group = application_settings_options_dictionary[update_application_setting_name]
                isCustom = 'Custom' == group
            else:
                isCustom = True

            update_application_setting = update_application_settings[update_application_setting_name]

            if isCustom:
                existing_application_settings['custom'][update_application_setting_name] = update_application_setting
            else:
                existing_application_settings[update_application_setting_name] = update_application_setting

        return janrain.application.update_settings(self.auth_header, self.base_url, self.verbose, existing_application_settings)

    def get_application_settings_options(self):
        """
        Get all application settings options for a Janrain application

        Args:
          * None

        Returns:
          * JSON Object: List of all settings options for a Janrain application
        """
        return janrain.application.get_settings_options(self.auth_header, self.base_url, self.verbose)


    # CLIENTS
    # Lookup and configuration paths to the Janrain clients
    def get_clients(self):
        """
        Get all the available clients from Janrain

        Args:
          * None

        Returns:
          * JSON Object: List of all information about all the clients
        """
        return janrain.clients.get_clients(self.auth_header, self.base_url, self.verbose)

    def get_client(self, client_id):
        """
        Get a specific client from Janrain

        Args:
          * `client_id`: The ID of the client

        Returns:
          * JSON Object: All the information about a single client
        """
        return janrain.clients.get_client(self.auth_header, self.base_url, self.verbose, client_id)

    def create_client(self, client_config):
        """
        Create a new client in Janrain

        Args:
          * `client_config`: A JSON block including Name, IP Whitelist and Features

        Returns:
          * JSON Object: The properties that have been used to set up the new client
        """
        return janrain.clients.create_client(self.auth_header, self.base_url, self.verbose, client_config)

    def update_client(self, client_id, client_config):
        """
        Update an existing client in Janrain

        Args:
          * `client_id`: The ID of the client to update
          * `client_config`: A JSON block with parameters to change in Janrain

        Returns:
          * JSON Object: The updated properties in the affected client
        """
        return janrain.clients.update_client(self.auth_header, self.base_url, self.verbose, client_id, client_config)

    def delete_client(self, client_id):
        """
        Delete an existing client from Janrain

        Args:
          * `client_id`: The ID of the client to delete

        Returns:
          * Boolean: `True` if the client has been deleted, `False` if there was an error
        """
        return janrain.clients.delete_client(self.auth_header, self.base_url, self.verbose, client_id)

    def get_client_settings(self, client_id):
        """
        Get the settings for a client currently stored in Janrain. Missing settings in the JSON will be removed in the
        Janrain console.

        Args:
          * `client_id`: The ID of the client to query

        Returns:
          * JSON Object: List of all settings attributed to a client
        """
        return janrain.clients.get_client_settings(self.auth_header, self.base_url, self.verbose, client_id)

    def update_client_settings(self, client_id, settings_config):
        """
        Update the stored settings for a client in Janrain

        Args:
          * `client_id`: The ID of the client to update
          * `settings_config`: A JSON block of settings to change in Janrain

        Returns:
          * JSON Object: List of the updated settings in the affected client
        """
        return janrain.clients.update_client_settings(self.auth_header, self.base_url, self.verbose, client_id, settings_config)

    def update_client_setting(self, client_id, setting_key, setting_value):
        """
        Update a single setting for a client in Janrain

        Args:
          * `client_id`: The ID of the client to update
          * `settings_key`: A string represents the key of a setting
          * `settings_value`: A string represents the value of a setting

        Returns:
          * JSON Object: Status of the request
        """
        return janrain.clients.update_client_setting(self.auth_header, self.capture_base_url, self.verbose, client_id, setting_key, setting_value)

    # FLOWS
    # Lookup and configuration paths to the Janrain flows
    def get_flows(self):
        return janrain.flows.get_flows(self.auth_header, self.base_url, self.verbose)

    def get_flow(self, flow_name):
        return janrain.flows.get_flow(self.auth_header, self.base_url, self.verbose, flow_name)

    def duplicate_flow(self, source_flow, new_flow_name):
        return janrain.flows.duplicate_flow(self.auth_header, self.base_url, self.verbose, source_flow, new_flow_name)

    def get_flow_fields(self, flow_name):
        return janrain.flows.get_flow_fields(self.auth_header, self.base_url, self.verbose, flow_name)

    def add_flow_field(self, flow_name, locale, field_config):
        return janrain.flows.add_flow_field(self.auth_header, self.base_url, self.verbose, flow_name, locale, field_config)

    def update_flow_field(self, flow_name, locale, field_name, field_config):
        """
        Update an existing field in a flow

        Args:
          * `flow_name`: The ID of the client to delete
          * `locale`: The locale code of the flow
          * `field_name`: The name of the field to update
          * `field_config`: A JSON block of configuration to update the field with

        Returns:
          * Boolean: `True` if the flow has been updated, `False` if there was an error
        """
        return janrain.flows.update_flow_field(self.auth_header, self.base_url, self.verbose, flow_name, locale, field_name, field_config)

    def get_flow_field(self, flow_name, field_name):
        return janrain.flows.get_flow_field(self.auth_header, self.base_url, self.verbose, flow_name, field_name)

    def delete_flow_field(self, flow_name, field_name):
        return janrain.flows.delete_flow_field(self.auth_header, self.base_url, self.verbose, flow_name, field_name)

    def create_flow_form(self, flow_name, form_name, form_config):
        return janrain.flows.create_flow_form(self.auth_header, self.base_url, self.verbose, flow_name, form_name, form_config)

    # FORMS
    # Update form configuration
    def update_form(self, flow_name, form_name, form_config):
        return janrain.forms.update_form(self.auth_header, self.base_url, self.verbose, flow_name, form_name, form_config)

    # TEMPLATES
    # Update email template
    def update_template(self, flow_name, flow_locale, template_name, template_body):
        return janrain.templates.update_template(self.auth_header, self.base_url, self.verbose, flow_name, flow_locale, template_name, template_body)

    # TRANSLATIONS
    # Get all translations for a flow
    def get_translations(self, flow_name):
        return janrain.translations.get_translations(self.auth_header, self.base_url, self.verbose, flow_name)

    # Add a new translation
    def add_translation(self, flow_name, translation):
        return janrain.translations.update_translation(self.auth_header, self.base_url, self.verbose, flow_name, translation)

    # Update an existing translation
    def update_translation(self, flow_name, translation):
        return janrain.translations.update_translation(self.auth_header, self.base_url, self.verbose, flow_name, translation)

    # SCHEMAS
    # Lookup and configuration paths to the Janrain schemas
    def get_schemas(self):
        return janrain.schema.get_schemas(self.auth_header, self.base_url, self.verbose)

    def get_schema(self, schema_name):
        return janrain.schema.get_schema(self.auth_header, self.base_url, self.verbose, schema_name)

    def get_attribute(self, schema_name, schema_element_name):
        return janrain.schema.get_attribute(self.auth_header, self.base_url, self.verbose, schema_name, schema_element_name)

    def create_attribute(self, schema_name, schema_element_name, schema_element_config):
        return janrain.schema.create_attribute(self.auth_header, self.base_url, self.verbose, schema_name, schema_element_name, schema_element_config)

    def delete_attribute(self, schema_name, schema_element_name):
        return janrain.schema.delete_attribute(self.auth_header, self.base_url, self.verbose, schema_name, schema_element_name)

    # Entity type
    # Managing entity type schema in Janrain
    def set_access_schema(self, type_name, for_client_id, access_type, attributes):
        return janrain.entity_type.set_access_schema(self.auth_header, self.capture_base_url, self.verbose, type_name, for_client_id, access_type, attributes)

    def set_attribute_constraints(self, type_name, attribute_name, constraints):
        return janrain.entity_type.set_attribute_constraints(self.auth_header, self.capture_base_url, self.verbose, type_name, attribute_name, constraints)