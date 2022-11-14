'''
JSON is a syntax for storing and exchanging data.
 - it stores data in key: value pair

JSON in Python
to work with json data in python i can import and use a built in package called json
'''
import json

# Parse JSON - Convert from JSON to Python
user_data_json_format =  '{ "name":"John", "age":30, "city":"New York"}'
print(f"type of user_data_json_format : {type(user_data_json_format)}")
print(user_data_json_format)

user_data_python_dict = json.loads(user_data_json_format)
print(f"type of user_data_python_dict using loads: {type(user_data_python_dict)}")
print(user_data_python_dict)

user_data_python_back_to_json = json.dumps(user_data_python_dict, indent=2, sort_keys=True)
print(f"type of user_data_python_back_to_json with dumps : {type(user_data_python_back_to_json)}")
print(user_data_python_back_to_json)