NHN_APIKEY = "{your_apikey}"
NHN_ZONE = "https://dnsplus.api.nhncloudservice.com/dnsplus/v1.0/appkeys/{0}/zones".format(NHN_APIKEY)
NHN_RECORD = "https://dnsplus.api.nhncloudservice.com/dnsplus/v1.0/appkeys/{0}/zones/{1}/recordsets"

HEADER = {'Content-Type': 'application/json'}

CF_APIKEY = "{your_api_key}"
CF_ZONE = "https://api.cloudflare.com/client/v4/zones"
X_AUTH_KEY = "{your_auth_key}"
X_AUTH_EMAIL = "{your_email}"

CF_RECORD = "https://api.cloudflare.com/client/v4/zones/{0}/dns_records/{1}"

CF_HEADER = {'Content-Type': 'application/json',
             'X-Auth-Key': X_AUTH_KEY,
             'X-Auth-Email': X_AUTH_EMAIL
             }

CF_ZONE_NAME = "{your_zone_name} e.g. t3q.ai"
NHN_ZONE_NAME = "{your_zone_name}"
