# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:04:08 2018

@author: kate
"""

from lxml import etree

#Validation
#Validating the dtd file.
#Open the dtd file.
dtd_file = open("map1.dtd.txt")
#Open xml1
xml1 = open("map1.xml").read() 
#Take out some of the text from the file so that it can be processed.
xml1 = xml1.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
dtd = etree.DTD(dtd_file)
root = etree.XML(xml1)
print(dtd.validate(root))

#Validating the xsd file.
xsd_file = open("map2.xsd.txt")
xml2 = open("map2.xml").read()
xml2 = xml2.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
xsd = etree.XMLSchema(etree.parse(xsd_file))
root = etree.XML(xml2)
print(xsd.validate(root))

#Printing out results.
#Parsing (reading elements from the file).
root = etree.XML(xml1)
print (root.tag)
print (root[0].tag)			# "polygon"
print (root[0].get("id"))		# "p1"
print (root[0][0].tag)		# "points"
print (root[0][0].text)	

#Creating a new polygon
#Creating the XML file root.
root = etree.XML(xml1)
#Create element tree class. In this case it is a polygon.
p2 = etree.Element("polygon")
#Create an unique id for the polygon.
p2.set("id", "p2");
#Creating child elements for the parent element.
#This child item defines the location points of the polygon.
#Naming of the child item.
p2.append(etree.Element("points"))
#Defining the point locations of the child item "points".
p2[0].text = "100,100 100,200 200,200 200,100"	# Set points text
#Add this child item to the polygon.
root.append(p2)	
#Check this has worked.					
print (root[1].tag)	

#Printing out the values of both polygons nicely.
#This method puts linebreaks between the objects.
out = etree.tostring(root, pretty_print=True)
print(out)
#Writing the values of the second polygon to the map1.xml.
#Open up the file to write/create it if doesn't already exist.
writer = open('xml3.xml', 'wb')
#Write to the file.
writer.write(out)
#Close the file. Relase it back to the computer to be used for other applications.
writer.close()


#Changing an xsl file to html.
#Converting an xsl file to text
#Open and read the xsl file.
xsl3 = open("map3.xsl").read()
#Get rid of the prolog.
xsl3 = xsl3.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
#Parse in the stylesheet.
xslt_root = etree.XML(xsl3)
#Convert the stylesheet to an xslt transformer.
transform = etree.XSLT(xslt_root)		
#Transform the xslt root.
result_tree = transform(root)		
#Convert the transformed xslt root into html text.
transformed_text = str(result_tree)

#writing the html text to a file.
print(transformed_text)
writer = open('map3.html', 'w')		
writer.write(transformed_text)
writer.close()



