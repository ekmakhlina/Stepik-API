# Run with Python 3

import json
import requests

# 1. Get your keys at https://stepik.org/oauth2/applications/ (client type = confidential, authorization grant type = client credentials)
client_id = '...'
client_secret = '...'

# 2. Get a token
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
resp = requests.post('https://stepik.org/oauth2/token/', data={'grant_type': 'client_credentials'}, auth=auth)
token = json.loads(resp.text)['access_token']

# 3. Call API (https://stepik.org/api/docs/) using this token.
# Example:

# 3.1. Create a new lesson

api_url = 'https://stepik.org/api/lessons'
data = {
	'lesson': {
		'title': 'My Lesson'
	}
}
# Use POST to create new objects
r = requests.post(api_url, headers={'Authorization': 'Bearer '+ token}, json=data)
lesson_id = r.json()['lessons'][0]['id']
print('Lesson ID:', lesson_id)

# 3.2. Add new code step to this lesson

api_url = 'https://stepik.org/api/step-sources'
data = {
    'stepSource': {
        "block":{
            "name":"code",
            "text":"<h1 style=\"text-align: center;\">Задача на программирование</h1>Чтобы понять, как выглядит задача на программирование со стороны студента, давайте рассмотрим пример.<br>Ниже от вас потребуется написать код, который считал бы сумму двух данных чисел.<br>Вы можете написать программу на любом языке из списка \"Select programming language\" ниже.",
            "source":{
                "execution_time_limit":5,
                "templates_data":"",
                "is_time_limit_scaled":True,
                "manual_time_limits":[],
                "code":"import random\n\ndef generate():\n    num_tests = 12\n    tests = []\n    for test in range(num_tests):\n        a = random.randrange(10)\n        b = random.randrange(10)\n        test_case = \"{} {}\\n\".format(a, b)\n        tests.append(test_case)\n    return tests\n\ndef solve(dataset):\n    a, b = dataset.split()\n    return str(int(a) + int(b))\n\ndef check(reply, clue):\n    reply, clue = int(reply), int(clue)\n    if reply == clue:\n        return 1\n    feedback = \"You answer was: {}. Correct answer was: {}\".format(reply, clue)\n    return False, feedback",
                "is_memory_limit_scaled":True,
                "execution_memory_limit":256,
                "test_archive":[],
                "manual_memory_limits":[],
                "samples_count":1,
            },
        },
            'lesson': lesson_id,
            'position': 1
    }
}


r = requests.post(api_url, headers={'Authorization': 'Bearer '+ token}, json=data)
step_id = r.json()['step-sources'][0]['id']
print('Step ID:', step_id)

# 3.2. Add new code step to this lesson (optional fields included)

api_url = 'https://stepik.org/api/step-sources'
data = {
    'stepSource': {
        "block":{
            "name":"code",
            "text":"<h1 style=\"text-align: center;\">Задача на программирование</h1>Чтобы понять, как выглядит задача на программирование со стороны студента, давайте рассмотрим пример.<br>Ниже от вас потребуется написать код, который считал бы сумму двух данных чисел.<br>Вы можете написать программу на любом языке из списка \"Select programming language\" ниже.",
            "options":{
                "execution_time_limit":5,
                "execution_memory_limit":256,
                "limits":{
                    "python3":{"time":15,"memory":256},
                    "c":{"time":5,"memory":256},
                    "c++":{"time":5,"memory":256},
                    "c++11":{"time":5,"memory":256},
                    "haskell":{"time":10,"memory":256},
                    "haskell 7.10":{"time":10,"memory":256},
                    "haskell 8.0":{"time":10,"memory":256},
                    "java":{"time":8,"memory":256},
                    "java8":{"time":8,"memory":256},
                    "java9":{"time":8,"memory":256},
                    "java11":{"time":8,"memory":256},
                    "julia":{"time":8,"memory":256},
                    "octave":{"time":13,"memory":256},
                    "asm32":{"time":5,"memory":256},
                    "asm64":{"time":5,"memory":256},
                    "shell":{"time":5,"memory":256},
                    "rust":{"time":5,"memory":256},
                    "r":{"time":8,"memory":256},
                    "ruby":{"time":15,"memory":256},
                    "clojure":{"time":10,"memory":256},
                    "mono c#":{"time":8,"memory":256},
                    "javascript":{"time":15,"memory":256},
                    "scala":{"time":9,"memory":256},
                    "kotlin":{"time":8,"memory":256},
                    "go":{"time":8,"memory":256},
                    "pascalabc":{"time":8,"memory":256},
                    "perl":{"time":15,"memory":256},
                    "php":{"time":15,"memory":256},
                    "swift":{"time":5,"memory":256}
                },
                "code_templates":{
                    "python3":"# put your python code here",
                    "c":"#include <stdio.h>\n\nint main() {\n    // put your code here\n    return 0;\n}",
                    "c++":"#include <iostream>\n\nint main() {\n    // put your code here\n    return 0;\n}",
                    "c++11":"#include <iostream>\n\nint main() {\n    // put your code here\n    return 0;\n}",
                    "haskell":"main :: IO ()\n-- put your code here",
                    "haskell 7.10":"main :: IO ()\n-- put your code here",
                    "haskell 8.0":"main :: IO ()\n-- put your code here",
                    "java":"class Main {\n    public static void main(String[] args) {\n        // put your code here\n    }\n}",
                    "java8":"class Main {\n    public static void main(String[] args) {\n        // put your code here\n    }\n}",
                    "java9":"class Main {\n    public static void main(String[] args) {\n        // put your code here\n    }\n}",
                    "java11":"class Main {\n    public static void main(String[] args) {\n        // put your code here\n    }\n}",
                    "julia":"# put your Julia code here",
                    "octave":"% put your octave code here",
                    "asm32":"# put your asm32 code here",
                    "asm64":"# put your asm64 code here",
                    "shell":"# put your shell (bash) code here",
                    "rust":"fn main() {\n    // put your Rust code here\n}",
                    "r":"# put your R code here",
                    "ruby":"# put your ruby code here",
                    "clojure":";; put your clojure code here",
                    "mono c#":"using System;\n\npublic class MainClass\n{\n    public static void Main()\n    {\n        // put your c# code here\n    }\n}",
                    "javascript":"// put your javascript (node.js) code here",
                    "scala":"object Main {\n  def main(args: Array[String]) {\n    // put your code here\n  }\n}",
                    "kotlin":"fun main(args: Array<String>) {\n    // put your code here\n}",
                    "go":"package main\n\nfunc main() {\n    // put your code here\n}",
                    "pascalabc":"begin\n  // put your code here\nend.",
                    "perl":"use 5.024; # strict enabled by default\nuse warnings;\n\n# put your Perl code here",
                    "php":"<?php\n// put your PHP code here\n?>",
                    "swift":"// put your swift code here"
                },
                "code_templates_header_lines_count":{
                    "python3":0,
                    "c":0,
                    "c++":0,
                    "c++11":0,
                    "haskell":0,
                    "haskell 7.10":0,
                    "haskell 8.0":0,
                    "java":0,
                    "java8":0,
                    "java9":0,
                    "java11":0,
                    "julia":0,
                    "octave":0,
                    "asm32":0,
                    "asm64":0,
                    "shell":0,
                    "rust":0,
                    "r":0,
                    "ruby":0,
                    "clojure":0,
                    "mono c#":0,
                    "javascript":0,
                    "scala":0,
                    "kotlin":0,
                    "go":0,
                    "pascalabc":0,
                    "perl":0,
                    "php":0,
                    "swift":0
                },
                "code_templates_options":{},
                "samples":[["4 1\n","5"]],
                "is_run_user_code_allowed":True
            },
            "subtitle_files":[],
            "source":{
                "execution_time_limit":5,
                "templates_data":"",
                "is_time_limit_scaled":True,
                "manual_time_limits":[],
                "code":"import random\n\ndef generate():\n    num_tests = 12\n    tests = []\n    for test in range(num_tests):\n        a = random.randrange(10)\n        b = random.randrange(10)\n        test_case = \"{} {}\\n\".format(a, b)\n        tests.append(test_case)\n    return tests\n\ndef solve(dataset):\n    a, b = dataset.split()\n    return str(int(a) + int(b))\n\ndef check(reply, clue):\n    reply, clue = int(reply), int(clue)\n    if reply == clue:\n        return 1\n    feedback = \"You answer was: {}. Correct answer was: {}\".format(reply, clue)\n    return False, feedback",
                "is_memory_limit_scaled":True,
                "execution_memory_limit":256,
                "test_archive":[],
                "manual_memory_limits":[],
                "samples_count":1,
                "are_all_tests_run":True,
                "are_all_tests_scored":False
            },
            "feedback_correct":"",
            "feedback_wrong":""
        },
            'lesson': lesson_id,
            'position': 2
    }
}


r = requests.post(api_url, headers={'Authorization': 'Bearer '+ token}, json=data)
step_id = r.json()['step-sources'][0]['id']
print('Step ID:', step_id)



###

# Your lesson is ready!
print('--> Check https://stepik.org/lesson/{}'.format(lesson_id))

###

# 3.4. Create a new course

api_url = 'https://stepik.org/api/courses'
data = {
	'course': {
		'title': 'My Course'
	}
}
r = requests.post(api_url, headers={'Authorization': 'Bearer '+ token}, json=data)
course_id = r.json()['courses'][0]['id']
print('Course ID:', course_id)

# 3.5. Add new module (section) to this course

api_url = 'https://stepik.org/api/sections'
data = {
	'section': {
		'title': 'My Section',
		'course': course_id,
		'position': 1
	}
}
r = requests.post(api_url, headers={'Authorization': 'Bearer '+ token}, json=data)
section_id = r.json()['sections'][0]['id']
print('Section ID:', section_id)

# 3.6. Add your existing lesson to this section (it is called unit)

api_url = 'https://stepik.org/api/units'
data = {
	'unit': {
		'section': section_id,
		'lesson': lesson_id,
		'position': 1
	}
}
r = requests.post(api_url, headers={'Authorization': 'Bearer '+ token}, json=data)
unit_id = r.json()['units'][0]['id']
print('Unit ID:', unit_id)

###

# Your course is ready
print('--> Check https://stepik.org/course/{}'.format(course_id))

###
