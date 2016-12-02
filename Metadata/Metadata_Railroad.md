# Railroad
Filename: RAILROAD<br>Geometry Type: polyline<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/raw/master/Images/FeatureViews/RR.JPG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |This feature class contains the following Railroad features:<br>RAILROAD - Visible and Hidden Railroad centerlines.<br>ELEVATED RAILROAD - Elevated Railroad centerlines.<br>EMBANKMENT RAILROAD- Embankment Railroad centerlines.<br>VIADUCT CENTERLINE- Viaduct Railroad centerlines.<br>DEPRESSION RAILROAD- Open Cut Depression Railroad centerlines.<br>RAILWAY FENCE- Railroad Fencing centerlines.<br>ABANDONED RAILROAD- Abandoned Railroad centerlines.
**Source(s)** |Current imagery and previous planimetric database
**Publication Dates** |**Data**: 06/25/14<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: 
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/Transportation/Railroad-Line/i7a5-bsik)
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/Transportation/Railroad-Line/i7a5-bsik
**Tags** |structure, Planimetric, Basemap, imageryBaseMapsEarthCover, Landbase, Train Tracks, Railroad, Rail, Train, transportation, NYCMap
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |The following features were captured for each subtype: <br>Railroad: Updated railroad centerlines. <br><br>Elevated Railroad: Updated elevated railroad centerlines.<br><br>Embankment Railroad: Updated embankment railroad centerlines. <br><br>Viaduct Centerline: Updated viaduct railroad centerlines.  <br><br>Open Cut Depression Railroad: Updated open cut depression railroad centerlines. <br><br>Railway Fence: Updated open railway fence lines. <br><br>Abandoned Railroad: Updated abandoned railroad centerlines.
**Features Captured** |--
**Features Excluded** |
**Capture and Update Notes** |The following capture notes for each subtype captured:<br>Railroad: All visible railroad centerlines were collected/updated. Hidden railroad centerlines (in tunnels) were copied from existing data with no elevation value or change.<br><br>Elevated Railroad: No elevation value was calculated.
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SOURCE_ID | Unique Feature Identification Number. | double | No
| FEATURE_CODE | Type of feature.<br>2400 = Railroad<br>2410 = Elevated railroad<br>2420 = Embankment railroad<br>2430 = Viaduct centerline<br>2440 = Open cut depression railroad<br>2450 = Railway fence<br>2465 = Abandoned railroad
 | integer | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set. <br>240000 = Railroad<br>240010 = Railroad, Hidden<br>241000 = Elevated Railroad<br>242000 = Embankment railroad<br>243000 = Viaduct centerline<br>244000 = Open cut depression railroad<br>245000 = Railway fence<br>246500 = Abandoned railroad
 | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
| NAME | Name of Railroad | text | No
