# integrity-guard-key-api

The integrity-guard-key-api project is the portion of the Secure Channel which retrieves the public key for a domain through a RESTful API.

The path to retrieve the public key is 
```
GET /keys/{domain} 
```
which will retrieve the pubilc key if it exists. If not, an empty string is returned.
