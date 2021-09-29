"""Reads preferences.json"""

import os
import sys
import json

if __name__ == "__main__":
	cwd = os.getcwd()
else:
	cwd = os.path.dirname(__file__)

debug = True


class Student(object):
	def __init__(self, name, preferences):
		self.name = name
		self.preferences = preferences

	def set_name(self, name):
		self.name = name

	def set_preferences(self, preferences):
		self.preferences = preferences

	def set_score(self, score):
		self.score = score


def json_to_dict(cwd):
	filename = "preferences.json"
	path = f"{cwd}/../inputs/{filename}"
	with open(path) as serialized:
		spec = json.load(serialized)
	if debug:
		print(spec, type(spec))
	return spec


def initialise_students(dict_):
	object_list = []
	for key in dict_.keys():
		name = key
		preferences = dict_[key]
		new_student = Student(name, preferences)
		object_list.append(new_student)
		if debug:
			print(f"name is {name}")
			print(f"preferences are {preferences}")
	return object_list


def read_json(cwd):
	student_dict = json_to_dict(cwd)
	student_list = initialise_students(student_dict)
	return student_list


