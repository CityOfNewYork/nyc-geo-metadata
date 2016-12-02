# Roadbed
Filename: ROADBED<br>Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/raw/master/Images/FeatureViews/Roadbed.JPG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |This feature class contains the following Roadbed features:<br>ROADBED - Roadbed feature.<br>INTERSECTION - Intersection of roadways.<br>DRIVEWAY - Driveway feature.<br>SHOULDER - Shoulder along roadway.
**Source(s)** |Current imagery and previous planimetric database
**Publication Dates** |**Data**: 06/25/14<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: 
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/City-Government/Roadbed/xgwd-7vhd)
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/City-Government/Roadbed/xgwd-7vhd
**Tags** |structure, Planimetric, Transportation, Roadway, Basemap, imageryBaseMapsEarthCover, Landbase, Road, transportation, NYCMap, Roadbed
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |
**Features Captured** |The following features were captured for each subtype: <br> Roadbed: Roadbed represents the interior polygon of pavement edge. The edges of these features are coincident with the linear feature class Pavement Edge.<br> Intersection: Portion of roadbed where three (3) or more roadways meet up with one another. Intersections were composed using features compiled and updated in Pavement Edge.<br>Driveway: All driveways > 200 feet in length and a minimum width of eight feet.<br>Shoulder: All shoulders on the roadway that may be used as a "break-down" area for vehicles or used by emergency vehicles to pass traffic. Shoulders are paved or gravel areas outside of the travel lane (as determined by paint markings) suitable for emergency vehicles to pass.
**Features Excluded** |The following features were excluded from each subtype: <br>Intersection: When two (2) roadways form a "T", the ending road was closed off so that the continuing roadbed edge forms a straight line (in Pavement Edge). Note, these "T" locations were not captured as intersection roadbed.
**Capture and Update Notes** |The following capture notes for each subtype captured:<br>Roadbed: Converging roadbeds were not split when it crossing one another at different elevations (e.g. on ramps that cross each other). Roadbed was usually cut by Median features (e.g., curb & grass) with the exception of painted, barrier and fence medians. Special care was applied to ensure that highway shoulders were not confused as sidewalk features.<br>Intersection: Special care was applied at intersections with a slight offset to ensure that such areas were captured and attributed as an intersection. The location where two alleys meet is considered an intersection and was captured as intersection roadbed. Intersection polygons were created by establishing the shortest distance from the intersection node to Pavement Edge. <br>Driveway: These driveways may service one or multiple buildings and there is no distiction between paved or unpaved surfaces. Driveways were compiled from Pavement Edge. Since Driveways have centerlines, if the corresponding CSCL has a name, that name is part of the main roadbed feature code. <br>Shoulder: Shoulders were collected along highways (as determined by CSCL "RW_TYPE" = 2, 3, or 9 and excluding "SEGMENT_TYPE" = G or F.) only. A curb separating an elevated paved surface from the roadway and between the roadway and a barrier median is a shoulder. Painted areas are considered shoulders. Should a painted shoulder area be tapered, the entire shoulder was captured as long as the shape was at least 8 feet wide.
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SOURCE_ID | Unique Feature Identification Number. | double | No
| FEATURE_CODE | Type of feature.<br>3500 = Roadbed | integer | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set:<br>350000 = Roadbed<br>350010 = Intersection<br>350020 = Shoulder<br>350030 = Driveway | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
