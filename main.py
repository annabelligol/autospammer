import requests

payload = {
    'content': 'Hello'
}

headers = {
    'authorization' : 'NzkyNzQxNTg3MDM3MDYxMTQw.GIK_Ba.0YGripuLS9O_chBLHAwLNhQfsopC6tFbUGekzE'

}
for i in range(1000):
    # Send a message to the channel
    r = requests.post('https://discord.com/api/v9/channels/1372450197946503270/messages', headers=headers, data=payload)
