import requests

r = requests.get('http://data.iana.org/TLD/tlds-alpha-by-domain.txt')
lines = r.text.splitlines()
tlds = [ '"%s"' % line.lower() for line in lines if not line.startswith('#') ]

print('[' + ', '.join(tlds) + ']')
