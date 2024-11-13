from jproperties import Properties

configs = Properties()

with open('example.properties', 'rb') as read_prop:
    configs.load(read_prop)

print(configs.get("DB_User"))
print(f'Database User: {configs.get("DB_User").data}')
print(f'Database Password: {configs["DB_PWD"].data}')
print(f'Properties Count: {len(configs)}')
