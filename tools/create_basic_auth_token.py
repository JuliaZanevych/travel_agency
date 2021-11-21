import base64

encoding='utf-8'

username = 'Julia479'
password = 'Ju234lia9'

credentials = f'{username}:{password}'
encode_credentials = str(base64.b64encode(credentials.encode(encoding)), encoding)
token = f'Basic {encode_credentials}'

print(token)
