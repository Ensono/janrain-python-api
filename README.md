# Janrain Python API

A python implementation of the Janrain configuration API to allow simpe creating and management of clients, flows and schemas

## Setup

The API uses a series of environment variables to execute queries and changes. These are the required environment variables

| Variable       | Contents                                                                                                             |
|---             |---                                                                                                                   |
| JANRAIN_REGION | The region where the Janrain instance is running. This is available on the console homepage                          |
| JANRAIN_APP    | The ID of the Janrain application instance. This is available on the console homepage                                |
| JANRAIN_CLIENT | The client ID to use to execute the queries and updates. This is available under "Manage Properties" in the console  |
| JANRAIN_SECRET | The secret assigned to the above client ID, this is available under "Manage Properties" in the console               |

