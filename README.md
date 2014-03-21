coldbox.dashdocs
================

DashDocs generator for ColdBox API documentation

###To Install DocSet:

1. Clone this project
2. In Dash, go to Manage DocSets
3. Click (+) in lower left
4. Browse to this project and select the .docset folder corresponding to version you want to install

###To Create a DocSet For a Different Version of ColdBox (ex 3.5.1)

This process has only been tested on OSX 10.9. Pre-requisites:

- Python (should be available on OSX already)
- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) python library (download, then `python setup.py install`)

1. Clone this project
2. Duplicate one of the existing docset folders, renaming to your version (ColdBox 3.5.1.docset)
3. Edit ./ColdBox 3.5.1.docset/Contents/Info.plist, change the version in CFBundleName key.
4. Delete everything in ./ColdBox 3.5.1.docset/Contents/Resources/Documents/
5. Download the API docs for your version from [http://www.coldbox.org/api](http://www.coldbox.org/api)
6. Copy the API docs for your version to ./ColdBox 3.5.1.docset/Contents/Resources/Documents/
7. Run the search index populator script included in this project, passing your docset directory name as second arg: 

	`python cbdoc2set.py ColdBox\ 3.5.1.docset`

