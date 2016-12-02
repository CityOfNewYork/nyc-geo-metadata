# Railroad Structure
Filename: RAILROAD_STRUCTURE<br>Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/raw/master/Images/FeatureViews/RR_sta.JPG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |This feature class contains the following Railroad structures:<br>SUBWAY/TRAIN STATION - Stand-alone subway and train stations and platforms.<br>ELEVATED SUBWAY/TRAIN STATION - Elevated subway and train stations and platforms.<br>VENTILATION GRATE - Ventilation grates within the ROW area.<br> EMERGENCY EXIT - Emergency Exit locations.<br>TRANSIT ENTRANCE - Entrance locations.
**Source(s)** |Current imagery and previous planimetric database
**Publication Dates** |**Data**: 11/17/14<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: 
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/City-Government/Railroad-Structure/5dic-xnxs)
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/City-Government/Railroad-Structure/5dic-xnxs
**Tags** |structure, Planimetric, Transportation, Basemap, Subway Station, Station, imageryBaseMapsEarthCover, Landbase, Rail, Subway, Rail Station, transportation, NYCMap
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |
**Features Captured** |The following features were captured for each subtype: <br> Subway/Train Station: Updated all stand-alone subway and train stations, and their platforms. These structures were found on terrain level or lower.<br>Elevated Subway/Train Station: Updated all elevated subway and train stations, and their platforms.<br> Ventilation Grate: Ventilation grates were be captured throughout the city.<br>Emergency Exit: Updated all emergency exits on railroad structures.<br>Transit Entrance: Updated all transit entrances.
**Features Excluded** |The following features were excluded from each subtype: <br>
**Capture and Update Notes** |The following capture notes for each subtype captured: <br>Subway/Train Station: Roof outlines were delineated to include any underlying stairways. <br>Elevated Subway/Train Station: Roof outlines were delineated to include any underlying stairways. <br>Ventilation Grate: These locations are not dependent on vicinity to subway centerline or subway entrance / exit.<br>Emergency Exit: Usually identified as painted yellow plates/grates for subways. Used ROW of existing subway centerlines as guide.<br>Transit Entrance: Usually identified as painted stairs for subways. Used ROW of existing subway centerlines as guide.
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SOURCE_ID | Unique Feature Identification Number. | double | No
| FEATURE_CODE | Type of feature.<br>2140 = Elevated subway/train station<br>2160 = Subway/train station<br>2470 = Ventilation grate<br>2480 = Emergency exit<br>2485 = Transit entrance | integer | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set. <br>214000 = Elevated subway/train station<br>214010 = Elevated subway/train station canopy<br>216000 = Subway/train station<br>216010 = Subway/train station canopy<br>247000 = Ventilation grate<br>248000 = Emergency exit<br>248500 = Transit Entrance | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
| NAME | Name of Railroad Structure | text | No
