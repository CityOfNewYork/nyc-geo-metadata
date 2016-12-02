# Median
Filename: MEDIAN<br>Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Images/FeatureViews/Median_Painted.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |All medians that physically divide a roadbed are collected and include medians, traffic islands, and Jersey barriers as well as painted medians to separate the traffic flow. Medians can be paved and are normally elevated (have a curb) or have dirt or grass. Subtypes include:<br>MEDIAN_PAINTED = Medians that have white paved marking (fishbone or striped) shall be collected as Median-painted. Double yellow lines in the middle of a road are NOT medians. Single independent white medians hatched used to direct traffic are NOT medians.<br>MEDIAN_CURB = Median with curb edge regardless of interior content (grass, pavement, concrete, etc.).<br>MEDIAN_RAIL = Median with guardrail.<br>MEDIAN_FENCE = Median with fence. <br>MEDIAN_GRASS = Median with grass/vegetation inside and no curb.<br>MEDIAN_BARRIER = Jersey barriers must be of "permanent nature,"i.e., in place to regulate the traffic, and must be displayed with a constant width of three (3) feet centered on the barrier. This does not include jersey barriers in construction areas or being used to block-off road access.
**Source(s)** |Current Imagery
**Publication Dates** |**Data**: 03/14/16<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: As needed
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/Transportation/Median/27b5-th78)
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/Transportation/Median/27b5-th78
**Tags** |median, roads, transportation, doitt, gis, planimetrics
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |All medians that physically divide a roadbed were collected; which includes medians, traffic islands, "Jersey Barriers", and painted areas that are used to separate traffic flow.
**Features Captured** |The following features were not captured as medians:<br>Barriers in front of buildings<br>Jersey Barriers used to regulate traffic in construction areas<br>Jersey Barriers used to block-off road access.
**Features Excluded** |
**Capture and Update Notes** |
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SOURCE_ID | Unique feature Identification Number. | double | No
| STREET_NAME | Name of street where median exists.  |  | No
| FEATURE_CODE | Type of feature.<br>3600 = Median |  | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set.<br>360000 = Median<br>360010 = Painted/Striped<br>360020 = Curb<br>360030 = Rail<br>360040 = Fence<br>360050 = Grass<br>360060 = Barrier<br>360070 = Other 
 |  | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
