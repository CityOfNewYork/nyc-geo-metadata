# Zip Code Boundaries
Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/ZipCodeBoundaries.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |
**Description** |Geographic approximation of USPS zip code boundaries. 
**Source(s)** |Department of Information Technology & Telecommunications (DOITT)
**Publication Dates** |**Data**: 04/08/14<br>**Last Update**: 09/08/14<br>**Metadata**: 12/22/2016<br>**Update Frequency**: As needed
**Available Formats** |Shapefile. Additional data formats are available for download on the [NYC Open Data Portal](https://data.cityofnewyork.us/Business/Zip-Code-Boundaries/i8iw-xf4u).
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html)
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/Business/Zip-Code-Boundaries/i8iw-xf4u
**Tags** |zip, postal code, zip code boundaries, zip code, area, doitt, doitt gis
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |Data is current as of last update date.
**Positional Accuracy** |
**Features Captured** |All zip codes within the five boroughs of New York City. 
**Features Excluded** |NA
**Capture and Update Notes** |
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| ZIPCODE | Five-digit postal zip code. | text | No
| BLDGZIP | Binary field (0,1) indicating whether the zip is unique to a building. 0 = NO, 1 = YES | text | No
| PO_NAME | Postal city of zip code | text | No
| POPULATION | Estimate population per zip code | double | No
| AREA | Area of zip code boundary in square feet | double | No
| STATE | State of zip code boundary | text | No
| COUNTY | County of zip code boundary | text | No
| ST_FIPS | State FIPS code | text | No
| CTY_FIPS | County FIPS code | text | No
| URL | Link to USPS website | text | No
