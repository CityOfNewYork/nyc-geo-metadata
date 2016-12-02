# Hydrography
Filename: HYDROGRAPHY<br>Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/raw/master/Images/FeatureViews/Lake.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |This feature class contains water bodies (types listed below) and is generally only updated when the actual shape has changed. These are not updated due to different water levels (e.g., high/low tide). This feature class includes the following subtypes:<br>LAKE/RESERVOIR = lake/reservoir hydro features<br>POND = pond hydro features<br>RIVER = river hydro features<br>STREAM = stream hydro features<br>WETLAND/MARSH = wetland/marsh hydro features<br>BEACH/SHORELINE = beach/shoreline hydro features<br>BAY/OCEAN = bay/ocean hydro features
**Source(s)** |Current imagery
**Publication Dates** |**Data**: 06/25/14<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: 
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/Environment/Hydrography/drh3-e2fd)
**Use Limitations** |Limited to use defined by the Department of Information Technology and Telecommunication, City of New York
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/Environment/Hydrography/drh3-e2fd
**Tags** |hydrography, water, gis, doitt, planimetrics
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |
**Features Captured** |
**Features Excluded** |
**Capture and Update Notes** |
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| NAME |  | text | No
| SOURCE_ID | Unique feature Identification Number. | double | No
| FEAT_CODE |  | integer | No
| SUB_CODE |  | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
| NAME | Name of feature | text | No
| SOURCE_ID | Unique Identification Number | double | No
| FEATURE_CODE | Type of feature. <br>2600 = Lake/Reservoir<br>2610 = Pond<br>2620 = River<br>2630 = Stream wider than 8 feet<br>2640 = Wetland<br>2650 = Beach/Shoreline<br>2660 = Bay/Ocean | integer | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set. <br>260000 = Lake/Reservoir<br>261000 = Pond<br>262000 = River<br>263000 = Stream wider than 8 feet<br>264000 = Wetland<br>265000 = Beach/Shoreline<br>266000 = Bay/Ocean | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
