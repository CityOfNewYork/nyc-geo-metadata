# Zip Code Boundaries
Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/main/Images/ZipCodeBoundaries.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |
**Description** |Geographic approximation of USPS zip code boundaries. 
**Source(s)** |Office of Technology and Innovation (OTI)
**Publication Dates** |**Data**: 04/08/14<br>**Last Update**: 09/08/14<br>**Metadata**: 12/22/2016<br>**Update Frequency**: As needed
**Available Formats** |Multiple formats. See links below.
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html)
**Access Rights** |Public
**Links** |[Public](https://nycmaps-nyc.hub.arcgis.com/datasets/nyc::zip-code/about) <br> [REST service](https://services6.arcgis.com/yG5s3afENB5iO9fj/arcgis/rest/services/ZipCode_view/FeatureServer) <br> [City employees](https://nyc.maps.arcgis.com/home/item.html?id=d4885672c5c949eabfb79c10ac51d3a8) <br>
**Tags** |zip, postal code, zip code boundaries, zip code, area, oti, doitt, gis
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
| AREA | Area of zip code boundary in square feet | double | No
| STATE | State of zip code boundary | text | No
| COUNTY | County of zip code boundary | text | No
| ST_FIPS | State FIPS code | text | No
| CTY_FIPS | County FIPS code | text | No
| URL | Link to USPS website | text | No
