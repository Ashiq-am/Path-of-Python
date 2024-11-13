from string import Template

log_template = Template("User: $user, Action: $action")

parsed = log_template.safe_substitute(user="Geek", action="Login")
print(parsed)
