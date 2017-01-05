import xlrd

def open_file(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)

    sheet = book.sheets()[1]
    sheet2 = book.sheets()[2]

#build .md file
    for row in xrange(3, sheet.nrows):
		row_value = sheet.row_values(row)
		if row_value[0] == "":
			datanamelookup = row_value[1]
			dataname = "# " + row_value[1] + "\n"
			filename = "Filename: " + row_value[2] + "<br>"
			geometrytype = "Geometry Type: " + row_value[3] + "<br><br>"
			image = "![image](" + row_value[4] + ")" + "\n" + "\n"
			TOC = "### Table of Contents" + "<br><br>" + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)" + "<br>" + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)" + "<br>"+ "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)" + "<br><br>"  + "\n"      

			identification = "## 1. Identification" + "\n" + "---------------------------------------------" + "\n" + "|     |     |" + "\n" + "| --- | --- |" + "\n"
			purpose = "**Purpose** |" + row_value[5] + "\n" 
			description = "**Description** |" + row_value[6] + "\n" 
			source = "**Source(s)** |" + row_value[7] + "\n" 
			dates = "**Publication Dates** |" + "**Data**: " + str(row_value[8]) + "<br>" + "**Last Update**: " + str(row_value[9]) + "<br>**Metadata**: " + str(row_value[10]) + "<br>**Update Frequency**: " + row_value[11] + "\n" 
			availableformat = "**Available Formats** |" + row_value[12] + "\n" 
			uselimitation = "**Use Limitations** |" + row_value[13] + "\n" 
			accessright = "**Access Rights** |" + row_value[14] + "\n" 
			contactinfo = "**Contact Information** |" + "**Name**: " + row_value[15] + "<br>**Email**: " + row_value[17] + "\n" 
			links = "**Links** |" + row_value[18] + "\n" 
			tags = "**Tags** |" + row_value[19] + "\n"

			dataquality = "## 2. Data Quality and Specifications" + "\n" + "---------------------------------------------" + "\n" + "|     |     |" + "\n" + "| --- | --- |" + "\n"
			horizontal =  "**Horizontal Coordinate System** |" + row_value[20] + "\n" 
			resolution =  "**Resolution** |" + row_value[21] + "\n"
			spatial =  "**Spatial Coverage** |" + row_value[22] + "\n"
			temporal =  "**Temporal Coverage** |" + str(row_value[23]) + "\n"
			accuracy = "**Positional Accuracy** |" + row_value[24] + "\n"
			captured = "**Features Captured** |" + row_value[25] + "\n"
			excluded = "**Features Excluded** |" + row_value[26] + "\n"
			capturenotes = "**Capture and Update Notes** |" + row_value[27] + "\n"

			attributesheader = "## 3. Attribute Information" + "\n" + "---------------------------------------------" + "\n" + "| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| " + "\n" + "|------------ | ------------- | -------- | ----------- | ----------|" + "\n"

			f = row_value[28]
			attributelist = ''
			
			for row in xrange(1, sheet2.nrows):
				row_value = sheet2.row_values(row)
				if row_value[0] == datanamelookup:
					attributes = "| " + row_value[1] + " | " + row_value[2] + " | " + row_value[3]+ " | " + row_value[4] + "\n" 
					attributelist += attributes

			metadata_print = dataname + filename + geometrytype + image + TOC + identification + purpose + description + source + dates + availableformat + uselimitation + accessright + contactinfo + links + tags + dataquality + horizontal + resolution + spatial + temporal + accuracy + captured + excluded + capturenotes + attributesheader + attributelist
		
			metadata_print = metadata_print.replace(u'\xa0', u' ')
			metadata_print = metadata_print.replace(u'\u2013', u'-')
			metadata_print = metadata_print.replace(u'\u2019', u'\'')
			metadata_print = metadata_print.replace(u'\u2018', u'\'')
			metadata_print = metadata_print.replace(u'\u201d', u'\"')
			metadata_print = metadata_print.replace(u'\u201c', u'\"')
			metadata_print = metadata_print.replace(u'\u2022', u'')

			file = open("Metadata_"+str(f)+".md","w")
			file.write(metadata_print.encode('utf8'))
			file.close()
        
if __name__ == "__main__":
    path = "T:\GIS\Projects\DoITT\Metadata-GitHub\DOITT_Metadata.xlsx"
    open_file(path)

