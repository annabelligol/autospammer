import requests

payload = {
    'content': 'Hello'
}

headers = {
    'authorization' : 'NzkyNzQxNTg3MDM3MDYxMTQw.Gs0YsS.tFObg7rB6mSL0EIL2kg3hU5Z1e2GAzXXS-DeSc'

}
for i in range(1000):
    # Send a message to the channel
    r = requests.post('https://discord.com/api/v9/channels/1372450197946503270/messages', headers=headers, data=payload)