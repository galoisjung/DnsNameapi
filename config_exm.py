NHN_APIKEY = "{Your apikey here}"
NHN_ZONE = "https://dnsplus.api.nhncloudservice.com/dnsplus/v1.0/appkeys/{0}/zones"
NHN_RECORD = "https://dnsplus.api.nhncloudservice.com/dnsplus/v1.0/appkeys/{0}/zones/{1}/recordsets"

HEADER = {'Content-Type': 'application/json'}

CF_APIKEY = "{Your Apikey here}"
CF_ZONE = "https://api.cloudflare.com/client/v4/zones"
X_AUTH_KEY = "{Your Auth key here}"
X_AUTH_EMAIL = "{Your Email here"

CF_RECORD = "https://api.cloudflare.com/client/v4/zones/{0}/dns_records/{1}"

CF_HEADER = {'Content-Type': 'application/json',
             'X-Auth-Key': X_AUTH_KEY,
             'X-Auth-Email': X_AUTH_EMAIL
             }


CF_ZONE_NAME = "{Your zone name}"
NHN_ZONE_NAME = "{Your zone name}"
