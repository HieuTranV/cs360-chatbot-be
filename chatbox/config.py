from dynaconf import Dynaconf
import os

class OpenAIConfig:
  key: str

class ElasticsearchConfig:
  name: str
  password: str
  host: str

class Settings(Dynaconf):
  openai: OpenAIConfig
  elasticsearch: ElasticsearchConfig

# config_path = os.getenv('CONFIG_PATH', None)

# if not config_path:
#   raise Exception('CONFIG_PATH not found')
# if config_path.split('.')[-1] != 'toml':
#   raise Exception('Config file must be *.toml')

# print('loading config: %s' %config_path)

settings = Settings(
  settings_file = ['chatbox/config.toml']
)