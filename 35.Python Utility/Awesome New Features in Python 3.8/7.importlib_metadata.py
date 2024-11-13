from importlib import metadata

# pip version
print(metadata.version('pip'))
data = metadata.metadata('pip')
print()
print(data)
