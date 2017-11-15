import json
s = 'core.start({"hola": "mundo"})'

print(json.loads(s[11:-1]))
