#!/bin/python
import urllib
import os
import xml.etree.ElementTree as ET 

#####################
# Helper functions
#####################

# Check for directory
def ensure_empty_dir(f):
	if os.path.exists(f):
		for fileName in os.listdir(f):
			os.remove(f+"/"+fileName)
	else:
		os.makedirs(f)

# Nicely indents the XML output 
def indent(elem, level=0):
    i = "\n" + level*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


# Removes empty nodes from the tree
def removeemptytags(elem):
    if elem.text:
        elem.text = elem.text.strip()
    toberemoved = []
    for child in elem:
        if len(child) == 0 and child.text is None and len(child.attrib) == 0:
            toberemoved.append(child)
    for child in toberemoved:
        elem.remove(child)
    for child in elem:
        removeemptytags(child)
        # Convert error to errorminus and errorplus
    if 'ep' in elem.attrib:
        err = elem.attrib['ep']
        del elem.attrib['ep']
        elem.attrib['errorplus'] = err
    if 'em' in elem.attrib:
        err = elem.attrib['em']
        del elem.attrib['em']
        elem.attrib['errorminus'] = err
    if 'error' in elem.attrib:
        err = elem.attrib['error']
        del elem.attrib['error']
        elem.attrib['errorminus'] = err
        elem.attrib['errorplus'] = err
    if 'e' in elem.attrib:
        err = elem.attrib['e']
        del elem.attrib['e']
        elem.attrib['errorminus'] = err
        elem.attrib['errorplus'] = err
