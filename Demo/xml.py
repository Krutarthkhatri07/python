import xml.etree.ElementTree as ET
data='''<person>
    <name>krutarth</name>
    <phone>7043619737
    </phone>
    <email hide="yes"/>
    </person>
'''

tree=ET.fromstring(data)
print('name:', tree.find('name').text)
print('attr:', tree.find('email').get('hide'))
