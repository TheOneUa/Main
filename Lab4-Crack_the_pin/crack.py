import hashlib

password = "86aa400b65433b608a9db30070ec60cd"
#in hash

# MD5-hash convert
def calculate_md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

for num in range(100000):
  num_str = f'{num:05}'
  # MD5-hash with 00001
  md5_hash = calculate_md5_hash(num_str)
  if md5_hash == password:
    print('Число:', num_str)