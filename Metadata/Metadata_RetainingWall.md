# Retaining Wall
Filename: RETAILINGWALL<br>Geometry Type: polyline<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/raw/master/Images/FeatureViews/Retaining_Wall_1.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |This feature class contains the following Retaining Wall features:<br>RETAINING WALL - Walls that retain earth from falling on transportation features.<br>RAILROAD RETAINING WALL - Walls that retain earth from falling on railroad bed.
**Source(s)** |Current imagery and previous planimetric database
**Publication Dates** |**Data**: 03/15/16<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: 
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/City-Government/Retaining-Wall/uvgd-xsc8)
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/City-Government/Retaining-Wall/uvgd-xsc8
**Tags** |structure, Wall, Planimetric, Basemap, imageryBaseMapsEarthCover, Landbase, Retaining Wall, transportation, NYCMap
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |The following features were captured for each subtype: <br> Retaining Wall: Walls built to retain earth from falling on transportation features with a height of ten (10) feet or greater.<br>Railroad Retaining Wall: Walls built to retain earth from falling on railroad bed.
**Features Captured** |The following features were excluded from each subtype: <br>Retaining Wall: Walls in backyards used for landscape were not captured. Walls in areas under construction (excavation) were not captured.
**Features Excluded** |
**Capture and Update Notes** |The following capture notes for each subtype captured:<br>
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SOURCE_ID | Unique Feature Identification Number. | double | No
| FEATURE_CODE | Type of feature.<br>2460 = Railroad Retaining Wall<br>4000 = Other Retaining Wall | integer | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set.<br>246000 = Railroad Retaining Wall<br>400000 = Other Retaining Wall | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
