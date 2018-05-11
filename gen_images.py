from jinja2 import Environment, FileSystemLoader
from os import makedirs, path
from datetime import datetime
import json

with open('images.json') as f:
  config_data = json.load(f)

now_utc = datetime.utcnow().isoformat()

env = Environment(
  loader=FileSystemLoader('./templates'),
  trim_blocks=True,
  lstrip_blocks=True,
)

for dockerfile_config in config_data.get('configs', []):
  # extend local image list with global lists (both are optional)
  for key in ['pythonConfigureOptions', 'cflags', 'systemPackages']:
    dockerfile_config[key] = config_data.get(key, []) + dockerfile_config.get(key, [])

  template = env.get_template('Dockerfile.jinja')
  dockerfile_dir = 'images/{}'.format(dockerfile_config.get('imageTag'))
  if not path.isdir(dockerfile_dir):
        makedirs(dockerfile_dir)

  template.stream({
    'now': now_utc,
    **dockerfile_config
  }).dump('{}/Dockerfile'.format(dockerfile_dir))
