import urequests
#ENTER IP ADDRESS OF THE SERVER(in this case Raspberry pi)
response = urequests.get('http:// ')
print("GET!!!!")
#print(type(response))
print(response.text)
#print(type(response.text))
#parsed = response.json()
print(response.json())


#print(parsed["userId"])
#print(parsed["id"])
#print(parsed["title"])

#print(response.content)
#print(type(response.content))

print(response.status_code)
print(response.reason)
