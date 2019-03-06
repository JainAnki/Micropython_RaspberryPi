import http_client

r = http_client.post('http://192.168.43.254/post', json={'hello': 'world'})
print(r.json())


r = http_client.get('http://localhost/get')
r.raise_for_status()
print(r.status_code)
print(r.text)  # r.content for raw bytes

