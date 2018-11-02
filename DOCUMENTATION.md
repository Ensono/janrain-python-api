<h1 id="janrain.api">janrain.api</h1>


<h2 id="janrain.api.Api">Api</h2>

```python
Api(self, defaults={})
```

<h3 id="janrain.api.Api.get_clients">get_clients</h3>

```python
Api.get_clients(self)
```

Get all the available clients from Janrain

Args:
  * None

Returns:
  * JSON Object: List of all information about all the clients

<h3 id="janrain.api.Api.get_client">get_client</h3>

```python
Api.get_client(self, client_id)
```

Get a specific client from Janrain

Args:
  * `client_id`: The ID of the client

Returns:
  * JSON Object: All the information about a single client

<h3 id="janrain.api.Api.create_client">create_client</h3>

```python
Api.create_client(self, client_config)
```

Create a new client in Janrain

Args:
  * `client_config`: A JSON block including Name, IP Whitelist and Features

Returns:
  * JSON Object: The properties that have been used to set up the new client

<h3 id="janrain.api.Api.update_client">update_client</h3>

```python
Api.update_client(self, client_id, client_config)
```

Update an existing client in Janrain

Args:
  * `client_id`: The ID of the client to update
  * `client_config`: A JSON block with parameters to change in Janrain

Returns:
  * JSON Object: The updated properties in the affected client

<h3 id="janrain.api.Api.delete_client">delete_client</h3>

```python
Api.delete_client(self, client_id)
```

Delete an existing client from Janrain

Args:
  * `client_id`: The ID of the client to delete

Returns:
  * Boolean: `True` if the client has been deleted, `False` if there was an error

<h3 id="janrain.api.Api.get_client_settings">get_client_settings</h3>

```python
Api.get_client_settings(self, client_id)
```

Get the settings for a client currently stored in Janrain. Missing settings in the JSON will be removed in the
Janrain console.

Args:
  * `client_id`: The ID of the client to query

Returns:
  * JSON Object: List of all settings attributed to a client

<h3 id="janrain.api.Api.update_client_settings">update_client_settings</h3>

```python
Api.update_client_settings(self, client_id, settings_config)
```

Update the stored settings for a client in Janrain

Args:
  * `client_id`: The ID of the client to update
  * `settings_config`: A JSON block of settings to change in Janrain

Returns:
  * JSON Object: List of the updated settings in the affected client

