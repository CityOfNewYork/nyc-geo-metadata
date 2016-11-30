# Metadata Template (GitHub)
------------------
# NYC Planimetric Database
NYC_DoITT_Planimetric_OpenData.gdb

[image of fc here]

Geometry Type: [Point/Line/Polygon]
### Table of Contents
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](##identification)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Organization**](##data-quality)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](##attribute-information)

## Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |  The purpose of this document is twofold. First, it is intended to define the capture rules for each planimetric feature collected as part of the planimetric update project. As such, this document is meant to clarify questions regarding how the features were captured, provide feature descriptions, and illustrate any exceptions that may apply. Second, since this document provides a wealth of information that would benefit users working with the data, we decided to make it accessible as a secondary source of documentation.
**Description** | One of the core functions of the NYC Department of Information Technology and Telecommunications (DoITT) GIS group is to maintain and distribute an accurate 'basemap' for NYC. Collectively, the basemap includes the digital orthophotography and planimetric features. The basemap provides the foundation upon which virtually all other geospatial data within New York government is registered. Ensuring its completeness and accuracy is fundamental to the Group’s core mission.	
**Source(s)** |	DOITT
**Publication  Dates** | **Data**: 2014 (see Capture notes). **Last Update**: 06/02/2016 **Metadata**: 01/01/2016 **Update Frequency**: As needed
**Spatial Coverage** | New York City, NY
**Temporal Coverage** | Database is current as of 2016. Previous downloads of the data are available here:
**Available Formats** | The planimetric database is a geodatabase file format. Individual data sets are also available for download. 
**Use Limitations** | NA
**Access Rights** | Public
**Contact Information** | **Name**: Department of Information Technology and Telecommunication (DOITT), GIS **Phone**: ###-###-#### **Email**: 
**Links** | NYC Planimetric Data may be downloaded through the NYC OpenData Portal- https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d/data
**Tags** |planimetric database, basemap, NYC, DOITT, GIS
	
## 2. Data Quality and Organization
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** | New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** | 1”=100’	
**Features Captured** |	The following features are captured in the planimetric database: Boardwalk, Bulding Footprint, Cooling Towers, Curb, Elevation, Hyrdo Structure, Media, Misc Struct Poly, Open Space, Park, Parking Lot, Pavement Edge, Plaza, Railroad, Railroad Structure, Retaining Wall, Roadbed, Shoreline, Sidewalk, Sidewalk Centerline, Swimming Pool, Transport Structure, Under Construction (links to separate metadata pages)
**Features Excluded** | For each of the features captured, some features were excluded based on class definitions. For more information, see individual feature class metadata notes. 
**Positional Accuracy** | Planimetrics are developed to meet American Society for Photogrammetry and Remote Sensing (ASPRS) Class 1 (one) horizontal mapping standards and ASPRS vertical Class 2 (two) accuracy specifications.
**Capture and Update Notes** | Digital planimetrics were derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Introduction for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. The images were captured with 80% forward lap and side lap to support 1”=100’ mapping and meet the distortion free requirements within New York City. The source imagery for the current planimetric update was captured on the following dates: • Manhattan - June 24, 2014• The Bronx, Brooklyn, Queens and Staten Island - April 1st through April 25th, 2014• Final delivery of all imagery – April 10, 2015 Based on the stereo models developed from the raw imagery and aerotriangulation, the planimetric features were updated or new features captured for the entire City. The project began March 2015 and was completed February 2016. 

## 3. Attribute Information
---------------------------------------------
Include a description and table of attributes and descriptions if metadata is for multiple feature classes. This section should make note of attributes that exist in all feature classes -- ie source_id, feature_code, sub_feature_code, status, etc. List all attributes if only one feature class included in metadata. 
Attribute | Description | Field Type | Required Field (Y/N) | Notes
------------ | ------------- | -------- | ----------- | ----------
SOURCE_ID | Unique feature Identification Number. | Integer | Y | 
FEATURE_CODE | Indicates the type of feature. | Integer | Y | 
SUB_FEATURE_CODE | (where applicable) indicates a subset of features within a given “Feature_Code” set.| Integer | Y
STATUS | Field indicating the feature status as it fits into one of the following categories:a) NEW. A feature captured for the first time during the 2014 planimetrics update project.b) UPDATED. The feature existed previously but has been updated during the 2014 planimetrics update project.c) UNCHANGED. The feature is unchanged from the source planimetrics database. | Text | Y

