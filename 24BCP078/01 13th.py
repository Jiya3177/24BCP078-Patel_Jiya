# onverts bytes into KB, MB and GB
bytes = float(input("enter bytes: "))
kb = bytes / 1024
mb = kb / 1024
gb = mb / 1024
print(bytes , "bytes =", kb , "KB")
print(bytes , "bytes =", mb , "MB")
print(bytes , "bytes =", gb , "GB")
