from typing_extensions import TypedDict, Literal

class AppConfig(TypedDict):
    app_name: str
    version: str
    environment: Literal['development', 'production']

def show_app_config(config: AppConfig) -> None:
    print(f"App: {config['app_name']}, Version: {config['version']}, Environment: {config['environment']}")

config = {'app_name': 'MyApp', 'version': '1.0', 'environment': 'development'}
show_app_config(config)
