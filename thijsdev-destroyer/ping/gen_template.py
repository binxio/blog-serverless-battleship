from jinja2 import Environment
from jinja2 import FileSystemLoader

j2_env = Environment(loader=FileSystemLoader('.'),                                                                                                                            
                     trim_blocks=True)
template = j2_env.get_template('step_template.yml')


ping_script = open("index.py", "r") 

state_machines = []
for i in range(1, 101):
    state_machines.append({"name": "Ping_{}".format(i)})

rendered_template = template.render(ping_script=ping_script.read(), state_machines=state_machines)

print(rendered_template)