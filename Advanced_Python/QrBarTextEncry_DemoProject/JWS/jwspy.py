import jws

header = { 'alg': 'HS256' }
payload = { 'name': 'Kuntal Samanta', 'age': '25' }
# Creating signature
signature = jws.sign(header, payload, 'key')
# Validating signature
res = jws.verify(header, payload, signature, 'key')
print(res)