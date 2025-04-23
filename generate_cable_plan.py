from jinja2 import Environment, FileSystemLoader
import json
from datetime import datetime

# Load JSON data
with open('device_info.json') as f:
    new_device_data = json.load(f)

with open('existing_device_info.json') as f:
    existing_device_data = json.load(f)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Add strftime filter
def strftime_filter(date, fmt=None):
    if fmt is None:
        fmt = '%Y-%m-%d'
    return date.strftime(fmt)

env.filters['strftime'] = strftime_filter
env.globals['now'] = datetime.now

# Load template
template = env.get_template('cable_plan_template.j2')

# Render template
output = template.render(
    device=new_device_data['data']['device'],
    existing_device=existing_device_data['data']['device']
)

# Write to file using UTF-8 encoding
with open('cable_plan.txt', 'w', encoding='utf-8') as f:
    f.write(output) 