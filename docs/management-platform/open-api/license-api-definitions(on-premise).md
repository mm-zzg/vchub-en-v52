# License API Definitions

## WAGOEmsLicense /ws/v1/node

Get the current WAGO EMS license information and receive updates when it changes.

Protocol: WebSockets (SignalR)

Request Payload: NA

Response Payload(JsonObject):

| Name | Type | Description |
|------|------|-------------|
| licenseItems | JsonArray | The EMS license information, containing at most one item. |
| version | String | The VC Hub software version. |
| signature | String | The Base64-encoded digital signature. |
| timestamp | String | The response timestamp in UTC. |
| nonce | String | A unique identifier for the response. |

License Item:

| Name | Type | Description |
|------|------|-------------|
| licenseKey | String | The masked license key. |
| articleNumber | String | The license article number. |
| licenseType | String | The license type: Permanent or Subscription; empty for a trial fallback. |
| licenseItem | String | The license package: WAGO EMS - S, WAGO EMS - M, or WAGO EMS - L. |
| status | String | The license status: Activated, Expired, Invalid, or None. |
| statusDescription | String | Additional license status information. |
| expirationTime | String or null | The expiration time in UTC; null for a permanent license. |
