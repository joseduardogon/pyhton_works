message = "Hello pyhton world!"
print(message)
print(message.title())
print(message.upper())
print(message.lower())
message = f"    {message}   "
print(message)
message = message.strip()
print(message)
print(message.removeprefix('He'))
print(message.removesuffix('world!'))