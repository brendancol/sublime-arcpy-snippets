import sys
import os
import re


def get_trigger(snippet):
	with open(snippet, 'r') as f:
		snippet_xml = f.read()
		trigger = re.search('<tabTrigger>(.*)</tabTrigger>', snippet_xml).group(1)
	return trigger

markdown = '''
sublime-arcpy-snippets
======================

**Collection of Sublime Text snippets for esri arcpy library**

##Installation
1. fork / clone repository (git clone https://github.com/brendancol/sublime-arcpy-snippets)
2. clone into local Sublime "User" folder
  * **Windows:** C:\Users\<user>\AppData\Roaming\<Sublime Text 2 or 3>\Packages\User.
3. Done...
\n
\n
'''

markdown += '##Keyboard Triggers'
markdown += '| Snippet        | Type           | Trigger  |\n'
markdown += '| ------------- |:-------------:| -----:|\n'

folder = sys.path[0]
snippets = [s for s in os.listdir(folder) if s.endswith('.sublime-snippet')]
print snippets

for s in snippets:
	path = os.path.join(folder, s)
	markdown += '|{} |{} |{} | \n'.format(os.path.splitext(s)[0], s.split('-')[0], get_trigger(path))

with open('README.md', 'w') as f:
	f.write(markdown)