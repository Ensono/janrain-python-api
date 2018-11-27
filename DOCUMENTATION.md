# janrain.api

## Api
```python
Api(self, defaults={})
```

### get_clients
```python
Api.get_clients(self)
```

Get all the available clients from Janrain

Args:
  * None

Returns:
  * JSON Object: List of all information about all the clients

### get_client
```python
Api.get_client(self, client_id)
```

Get a specific client from Janrain

Args:
  * `client_id`: The ID of the client

Returns:
  * JSON Object: All the information about a single client

### create_client
```python
Api.create_client(self, client_config)
```

Create a new client in Janrain

Args:
  * `client_config`: A JSON block including Name, IP Whitelist and Features

Returns:
  * JSON Object: The properties that have been used to set up the new client

### update_client
```python
Api.update_client(self, client_id, client_config)
```

Update an existing client in Janrain

Args:
  * `client_id`: The ID of the client to update
  * `client_config`: A JSON block with parameters to change in Janrain

Returns:
  * JSON Object: The updated properties in the affected client

### delete_client
```python
Api.delete_client(self, client_id)
```

Delete an existing client from Janrain

Args:
  * `client_id`: The ID of the client to delete

Returns:
  * Boolean: `True` if the client has been deleted, `False` if there was an error

### get_client_settings
```python
Api.get_client_settings(self, client_id)
```

Get the settings for a client currently stored in Janrain. Missing settings in the JSON will be removed in the
Janrain console.

Args:
  * `client_id`: The ID of the client to query

Returns:
  * JSON Object: List of all settings attributed to a client

### update_client_settings
```python
Api.update_client_settings(self, client_id, settings_config)
```

Update the stored settings for a client in Janrain

Args:
  * `client_id`: The ID of the client to update
  * `settings_config`: A JSON block of settings to change in Janrain

Returns:
  * JSON Object: List of the updated settings in the affected client

### update_client_setting
```python
Api.update_client_setting(self, client_id, setting_key, setting_value)
```

Update a single setting for a client in Janrain

Args:
  * `client_id`: The ID of the client to update
  * `settings_key`: A string represents the key of a setting
  * `settings_value`: A string represents the value of a setting

Returns:
  * JSON Object: Status of the request

### update_flow_field
```python
Api.update_flow_field(self, flow_name, locale, field_name, field_config)
```

Update an existing field in a flow

Args:
  * `flow_name`: The ID of the client to delete
  * `locale`: The locale code of the flow
  * `field_name`: The name of the field to update
  * `field_config`: A JSON block of configuration to update the field with

Returns:
  * Boolean: `True` if the flow has been updated, `False` if there was an error

