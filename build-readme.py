import sys
import os
import re
import lxml.etree

def get_trigger(snippet):
    with open(snippet, 'r') as f:
        snippet_xml = lxml.etree.parse(f).getroot()
        snippet_dict = dict(((elt.tag,elt.text) for elt in snippet_xml))
    
    return snippet_dict.get('tabTrigger'), snippet_dict.get('description'), snippet_dict.get('scope')
        

markdown = '''
sublime-arcpy-snippets
======================

**Collection of Sublime Text snippets for esri arcpy library**

###Installation
1. fork / clone repository (git clone https://github.com/brendancol/sublime-arcpy-snippets)
2. clone into local Sublime "User" folder
  * **Windows:** C:\Users\<user>\AppData\Roaming\<Sublime Text 2 or 3>\Packages\User.
3. Done...
\n
\n
'''

markdown += '###Keyboard Triggers\n'
markdown += '| Snippet        | Trigger           | Description  | Scope| \n'
markdown += '| ------------- |-------------| -----| -----|\n'

folder = sys.path[0]
snippets = [s for s in os.listdir(folder) if s.endswith('.sublime-snippet')]
print snippets

for s in snippets:
    path = os.path.join(folder, s)
    trigger, desc, src = get_trigger(path)
    markdown += '|{} |{} |{} | {}| \n'.format(os.path.splitext(s)[0], trigger, desc, src)

with open('README.md', 'w') as f:
    f.write(markdown)