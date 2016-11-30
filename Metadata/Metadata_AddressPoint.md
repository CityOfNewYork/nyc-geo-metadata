# ADDRESS POINT
AddressPoint.shp

![image](https://github.com/ekamptner/test-repo/blob/master/Images/AddressPoint.PNG)

Geometry Type: Point
### Table of Contents
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Organization**](#data-quality)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#attribute-information)

## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** | Address points were developed to supplement the address information supplied by the CSCL centerline. Some computer aided dispatch systems use address points as the primary source for locating an address.
**Description** | Address points were initially created from data in the Department of City Planning Property Address Directory (PAD) file. Points were created approximately five feet inside building footprints along the correct street frontage. A field collection/verification process was undertaken to validate "multi-valued" addresses contained in the PAD file (i.e. those locations with a range of addresses). Additionally, a statistical sample of PAD single valued addresses was field checked. Approximately 100,000 locations were visited (about 10% of the total).
**Source(s)** |	Department of City Planning Property Address Directory (PAD), DOITT
**Publication  Dates** | **Data**: 2009 **Last Update**: 10/26/2016 <br> **Metadata**: 11/14/2016 <br> **Update Frequency**: As needed
**Spatial Coverage** | New York City, NY
**Temporal Coverage** | Database is current as of last update date. 
**Available Formats** | .shp. Additional data formats are available for download on the OpenData Portal.
**Use Limitations** | While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** | Public
**Contact Information** | **Name**: Department of Information Technology and Telecommunication (DOITT), GIS <br>**Phone**: ###-###-#### <br> **Email**: gis-group@doitt.nyc.gov
**Links** | The building footprint data layer is available for download on NYC Open Data Portal -- https://data.cityofnewyork.us/City-Government/NYC-Address-Points
**Tags** | address, BIN, New York City, NYC, Brooklyn, Bronx, Manhattan, Queens, Staten Island
	
## 2. Data Quality and Organization
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** | New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** | NA	
**Features Captured** |	All possible measures have been taken to ensure all registered address points are collected. 
**Features Excluded** | Only registered address points are included in the dataset.
**Positional Accuracy** | 
**Capture and Update Notes** | Address points were initially created from data in the Department of City Planning Property Address Directory (PAD) file. Points were created approximately five feet inside building footprints along the correct street frontage. A field collection/verification process was undertaken to validate "multi-valued" addresses contained in the PAD file (i.e. those locations with a range of addresses). Additionally, a statistical sample of PAD single valued addresses was field checked. Approximately 100,000 locations were visited (about 10% of the total).


## 3. Attribute Information
-----------------------------------
Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes
------------ | ------------- | -------- | ----------- | ----------
FID | Unique feature Identification Number. | Integer | Y | NA
SHAPE | Geometry Field | Geometry | Y | NA
ADDRESS_ID |   | Numeric | Y | NA
BIN |   | Numeric | Y | NA
H_NO |  | Text | Y | NA
HNO_SUFFIX |   | Text | Y | NA
HYPHEN_TYP |   | Text | Y | NA
SIDE_OF_ST |    | Text | Y | NA
SPECIAL_CO |   | Text | Y | NA
BOROCODE | Borough identification code. | Text | Y | NA
ZIPCODE | Zip code | Text | Y | NA
CREATED | Date Created | Date | Y | NA
MODIFIED | Date Modified | Date | Y | NA
ST_NAME | Street name | Text | Y | NA
HN_RNG |  | Text | Y | NA
HN_RNG_SUF |  | Text | Y | NA
PHYSICALID | Physical ID | Integer | Y | NA

