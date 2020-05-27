import json
import os

# The default save when a new save is created. Changing this should add any new values to old saves
default_save = {
	'name': 'New Save',
	'coins': 10
}

# Creates a <name> save file
def create_save(name):
	write_data(name, default_save)

# Returns dictionary of <name> save file
def get_save(name):
	check_data_for_updates(name)
	
	save_file = open('data/saves/%s' % name, 'r')
	binary_data = save_file.read()

	json_data = ''.join(chr(int(x, 2)) for x in binary_data.split())

	save_file.close()

	return json.loads(json_data)

# Changes the <name> save file to have the values in <options>
def edit_save(name, options):
	check_data_for_updates(name)

	json_data = get_save(name)

	new_keys = options.keys()
	for key in new_keys:
		json_data[key] = options[key]

	write_data(name, json_data)

# Checks whether the data in <default_save> is not in the <name> save file and updates it
# This function is kinda inefficient and could be improved further, but it works for now
def check_data_for_updates(name):
	save_file = open('data/saves/%s' % name, 'r')
	binary_data = save_file.read()

	json_data = ''.join(chr(int(x, 2)) for x in binary_data.split())
	save_data = json.loads(json_data)

	for key in default_save.keys():
		if not (key in save_data):
			save_data[key] = default_save[key]

	save_file.close()

	write_data(name, save_data)

# Overwrites the <data> to the <name> save file
def write_data(name, data):
	new_file = open('data/saves/%s' % name, 'w+')

	save_file = json.dumps(data)
	save_file_bytes = ' '.join(format(ord(letter), 'b') for letter in save_file)

	new_file.write(save_file_bytes)

	new_file.close()

# Delete save <name>
def delete_save(name):
	if (save_exists(name)):
		os.remove('data/saves/%s' % name)

# Returns boolean of whether save <name> exists
def save_exists(name):
	return os.path.exists('data/saves/%s' % name)
	