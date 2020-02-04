# Import json library
import json

data = '''{
    "name" : "Gregory",
    "phone" : {
        "type" : "intl",
        "number" : "+1 253 579 4244"
    },
    "email" : {
    "hide" : "yes"
    }
}'''

# loads == load from string
# Returns a python dictionary

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])



print('\r\n\r\n')

# Example of a list
inpt = '''[
    { "id" : "001",
    "x" : "2",
    "name" : "Gregory"
    },
    {
    "id" : "009",
    "x" : "7",
    "name" : "Michele"
    }
]'''

info = json.loads(inpt)
print('User count:', len(info))
for item in info :
    print('Name', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])