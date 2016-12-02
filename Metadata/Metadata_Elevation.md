# Elevation
Filename: ELEVATION<br>Geometry Type: point<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Images/FeatureViews/Elevation_Build.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |This feature class contains elevation points throughout the city of the following types: <br>BUILDING ELEVATION - Elevation of the highest portion of the roof of a building, excluding antennae and roof fixtures such as air conditioning (AC), elevator shafts, chimneys, etc.<br>WATER ELEVATION - Elevation on standing water (ponds, reservoirs, lakes).<br>SPOT ELEVATION -Elevation points collected in the center of the roadbed (coincident with CSCL), captured at beginning, mid-point, end, and at 200'spacing of the visible roadbed. Spot elevations are captured on paved, unpaved, alley subtypes in CSCL Centerline and all of Interior Sidewalk Centerline. Spot elevations will not be captured to a CSCL if no roadbed exists.<br>BRIDGE ELEVATION - Elevation points captured at beginning, mid-point, end, and at 200'spacing of the visible bridge deck. 
**Source(s)** |Current imagery
**Publication Dates** |**Data**: 03/14/16<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: As needed
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/Transportation/Elevation-points/szwg-xci6)
**Use Limitations** |Limited to use defined by the Department of Information Technology and Telecommunication, City of New York
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/Transportation/Elevation-points/szwg-xci6
**Tags** |elevation, height, building elevation, water elevation, spot elevation, bridge elevation, gis, doitt, planimetrics
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |Elevation points were captured for all building footprint features (Building), bridges, and standing water (ponds, reservoirs, lakes). Spot elevations were captured on paved, unpaved, and alley subtypes in CSCL centerline and all Interior Sideswalk CSCL feature classes. Elevation points were placed in the center of the roadbed (coincident with CSCL features). These points were captured at the beginning, middle, and end of length of visible roadbed. Additional elevation points were added at 200' spacing when the distance between the beginning, middle, or end was greater than 200 linear feet.
**Features Captured** |Elevation points were not collected for pedestrian/bike bridges. Spot elevations were not captured on a CSCL feature if no roadbed exists.
**Features Excluded** |The vertical accuracy was set to the following standard: ASPRS 1"=100' Class 2.
**Capture and Update Notes** |Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. The images were captured with 80% forward lap and side lap to support 1"=100' mapping and meet the distortion free requirements within New York City. Planimetrics are developed to meet American Society for Photogrammetry and Remote Sensing (ASPRS) Class 1 (one) horizontal mapping standards and ASPRS vertical Class 2 (two) accuracy specifications. Planimetrics are delivered via an ESRI geodatabase in New York State Plane Coordinates, Long Island East Zone, NAD83, US foot.
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| ELEVATION | Field measuring surface elevation above sea level (in feet).  | double | No
| SOURCE_ID | Unique feature Identification Number. | double | No
| FEATURE_CODE | Type of feature. <br>3000 = Spot Elevation<br>3010 = Water Elevation<br>3020 = Building Elevation | integer | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set. <br>300000 = Spot Elevation<br>300020 = Spot, bridge<br>301000 = Water Elevation<br>302000 = Building Elevation
 | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
