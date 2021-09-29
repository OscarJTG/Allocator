import os
import sys

if __name__ == "__main__":
	cwd = os.getcwd()
	util_path = f"{cwd}/../util"
	sys.path.insert(0, util_path)
	import read_inputs

	filename_json = "preferences_test.json"

	student_object_list = read_inputs.read_json(filename_json, cwd)
	names_expected = ["Student1", "Student2"]
	preferences_expected = [{"1": "Project1", "2": "Project2"},
							{"1": "Project1", "2": "Project4"}]

	names = []
	preferences = []
	for student in student_object_list:
		names.append(student.name)
		preferences.append(student.preferences)

	if names == names_expected:
		print("Passed name test")
	else:
		print("Failed name test:")
		print(f"Names read are: {names},\nexpected: {names_expected}")

	if preferences == preferences_expected:
		print("Passed preferences test")
	else:
		print("Failed preferences test:")
		print(f"preferences read are: {preferences},\nexpected: {preferences_expected}")
		print(f"preferences type = {type(preferences)}, expected type = {type(preferences_expected)}")