# History Storage API Definitions

## GET /api/v1/historystorage/databases

Get the configured database history providers.

Protocol: Https

Request Payload: NA

Response Payload(JsonArray):

| Name | Type | Description |
|------|------|-------------|
| id | String | The unique ID of the database provider. |
| type | String | The database provider type. |
| name | String | The database provider name. |
| allowStorage | Boolean | Whether the provider can be used for storage. If false, it is available for queries only. |

## GET /api/v1/historystorage/alarms

Get the configured alarm history providers.

Protocol: Https

Request Payload: NA

Response Payload(JsonArray):

| Name | Type | Description |
|------|------|-------------|
| id | String | The ID of the alarm provider. |
| name | String | The alarm provider name. |
| queryOnly | Boolean | Whether the provider is available for queries only. If true, it cannot be used for storage. |
