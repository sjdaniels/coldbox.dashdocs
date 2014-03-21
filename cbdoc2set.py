#!/usr/local/bin/python

import os, re, sqlite3, sys
from bs4 import BeautifulSoup, NavigableString, Tag 

docsetroot = sys.argv[1]
print docsetroot

db = sqlite3.connect(os.path.join(docsetroot,'Contents/Resources/docSet.dsidx'))
cur = db.cursor()

print 'Rebuilding Search Index'

try: cur.execute('DROP TABLE searchIndex;')
except: pass
cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = os.path.join(docsetroot,'Contents/Resources/Documents')
funcpages = []

page = open(os.path.join(docpath,'allclasses-frame.html')).read()
soup = BeautifulSoup(page)

any = re.compile('.*')
for tag in soup.find_all('a', {'href':any}):
    name = tag.text.strip()
    if len(name) > 0:
        path = tag.attrs['href'].strip()
        if path.split('#')[0] not in ('index.html', 'allclasses-frame.html', 'overview-frame.html', 'overview-summary.html'):
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Class', path))
            funcpages.append(path)
            print 'name: %s, path: %s' % (name, path)


page = open(os.path.join(docpath,'overview-frame.html')).read()
soup = BeautifulSoup(page)

any = re.compile('.*')
for tag in soup.find_all('a', {'href':any}):
    name = tag.text.strip()
    if len(name) > 0:
        path = tag.attrs['href'].strip()
        if path.split('#')[0] not in ('index.html', 'allclasses-frame.html', 'overview-frame.html', 'overview-summary.html'):
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Package', path))
            print 'name: %s, path: %s' % (name, path)

for funcpage in funcpages:
	pagepath = funcpage.split('/')
	pagefile = pagepath[len(pagepath)-1]
	page = open(os.path.join(docpath,funcpage)).read()
	soup = BeautifulSoup(page)
	any = re.compile('.*')
	for tag in soup.find_all('a', {'href':any}):
	    name = tag.text.strip()
	    if len(name) > 0:
	        path = tag.attrs['href'].strip()
	        if path.split('#')[0] == pagefile:
	            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Method', ''.join([funcpage,'#',path.split('#')[1]])))
	            print 'name: %s, path: %s' % (name, ''.join([funcpage,'#',path.split('#')[1]]))

db.commit()
db.close()