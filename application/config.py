# This file is gonna contain a config utility
# that will be used to read configuration files based on specific criteria.

import os
import yaml


# print(os.environ['HOME'])
# print(os.environ.get('HOME'))
# print(os.getenv('HOME', 'hello'))

# 1: Get the full file path
# 2: Get the directory for the full file path
# 3: Get the parent directory for step 2.
# 4: Append the environment.yml to the end of the parent path
# 5: Supply this path to the open method 
full_filepath = os.path.realpath(__file__)
full_path_directory = os.path.dirname(full_filepath)
print(full_path_directory)
parent_directory = os.path.dirname(full_path_directory)
print(parent_directory)
config_file = os.path.join(parent_directory, 'environment.yml')
print(config_file)


# exit
# parent_directory =""
# # and then append environment.yaml to 
chosen_environment = os.environ.get('ENV')
print(chosen_environment)

with open(config_file) as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data[chosen_environment]['gender'])



