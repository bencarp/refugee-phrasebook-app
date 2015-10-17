import csv , xlrd, xml.etree.ElementTree as xmlTree
import re, sys
import pandas as pd

xmlFile = '/home/ben/refphrasebook2/BasicConversationsXML.xml'
xlsFile = '/home/ben/Refugee_Phrasebook.xls'

#Read xls and get value of one field
ab = pd.read_excel(xlsFile, sheetname=0, header=0, skiprows=None, skip_footer=0, index_col=0, engine=None)
ab = ab.fillna('')
row = ab.ix[1,len(ab.columns)-1]

root = xmlTree.Element('xlsdata')

for reihe in range (len(ab.index)):
	phrase = xmlTree.SubElement(root, 'phrase')
	for spalte in range (1, len(ab.columns)):
		wort = ab.ix[reihe, spalte]
		sprache = xmlTree.SubElement(phrase, ab.ix[0, spalte])
		sprache.text = wort
		
xmlTree.ElementTree(root).write(xmlFile, 'utf-8')



