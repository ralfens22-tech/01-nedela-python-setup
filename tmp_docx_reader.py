import zipfile
import os
import xml.etree.ElementTree as ET

path = 'C:/Users/ralfe/Downloads/05 - week 05 final project (1).docx'
print('exists', os.path.exists(path))
if not os.path.exists(path):
    raise SystemExit(1)
with zipfile.ZipFile(path) as z:
    names = z.namelist()
    print('files count', len(names))
    if 'word/document.xml' not in names:
        print('missing document.xml')
        raise SystemExit(1)
    xml = z.read('word/document.xml')
    root = ET.fromstring(xml)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    texts = [t.text for t in root.findall('.//w:t', ns) if t.text]
    print('---')
    print('\n'.join(texts[:200]))
