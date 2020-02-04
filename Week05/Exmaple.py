import xml.etree.ElementTree as ET
data = '''<person>
    <name>Gregory</name>
    <phone type ="intl">
        +1 253 579 4244
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

print('\r\n')

input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Gregory</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Michele</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User Count:', len(lst))
for item in lst :
    print('Name', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get("x"))

