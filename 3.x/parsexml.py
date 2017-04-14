# 27 Mar 2017 | Parser - XML [ElementTree / lxml]

'''
http://www.diveintopython3.net/xml.html
For large xml documents, lxml is significantly faster than the built-in ElementTree library. If you’re only using the ElementTree api and want to use the fastest available implementation, you can try to import lxml and fall back to the built-in ElementTree.

try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
But lxml is more than just a faster ElementTree. Its findall() method includes support for more complicated expressions.
'''

#import xml.etree.ElementTree as ET
from lxml import etree as ET
from pprint import pprint

tree = ET.parse('sample_movies.xml')
root = tree.getroot()

#print('Root Element', root.tag)
#print('Root Attributes', root.attrib['shelf'])
#print(len(root))

# Output Format: Tabular
for child1 in root:
    print(str(child1.tag).capitalize() + ': ' + str(child1.attrib['title']))

    for child2 in child1:
        print('\t' + str(child2.tag).capitalize() + ': ' + child2.text)

# Output Format: Delimited
for child1 in root:
    rec = {}
    rec['type'] = rec['year'] = rec['rating'] = rec['stars'] = rec['description'] = ''
    rec['title'] = '"' + str(child1.attrib['title'])

    for child2 in child1:
        if child2.tag in ('type', 'year', 'rating', 'stars', 'description'):
            rec[child2.tag] = str(child2.text)

    print(rec['title'] + '","'
          + rec['type'] + '","'
          + rec['year'] + '","'
          + rec['rating'] + '","'
          + rec['stars'] + '","'
          + rec['description'] + '"')
