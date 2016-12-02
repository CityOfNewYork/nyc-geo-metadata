# Sidewalk
Filename: SIDEWALK<br>Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/raw/master/Images/FeatureViews/Sidewalk_1.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |This feature class contains the following Sidewalk features:<br>ROW SIDEWALK - All paved sidewalks that are located along or adjacent to the ROW (i.e. building to building).<br>INTERIOR SIDEWALK - All paved sidewalks for all interior sidewalk that are located interior to the ROW.  The business use of this feature is to identify potential areas, outside of the public Right of Way (ROW), that could permit emergency vehicles through travel.
**Source(s)** |Current imagery, previous planimetric database, NYCHA Development, DPR Parks Properties, CSCL, Forts, Hospitals, Schools
**Publication Dates** |**Data**: 07/07/14<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: 
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/City-Government/Sidewalk/vfx9-tbb6)
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/City-Government/Sidewalk/vfx9-tbb6
**Tags** |
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |
**Features Captured** |The following features were captured for each subtype: <br> Row Sidewalk: All paved sidewalks that are located within the ROW (i.e. building to building). <br> Interior Sidewalk: All paved sidewalks that are located outside of the ROW.
**Features Excluded** |The following features were excluded from each subtype: <br>Row Sidewalk: Openings in sidewalk (for landscaping and trees) were ignored. Large, paved open spaces in front of buildings and outside of the public ROW (may have trees and landscaping) will be included in Plaza and were not captured as sidewalk.<br>Interior Sidewalk: Openings in sidewalk (for landscaping and trees) were ignored. Since the intended purpose of such features is to support emergency through travel, any spurs or dead-ends (e.g., walkways leading to a building) were not captured. These features were not captured in office parks or other similar commercial areas.
**Capture and Update Notes** |The following capture notes for each subtype captured:<br>Row Sidewalk: In areas of construction, sidewalks were collected along an imaginary line to complete polygon. In areas where equipment is stored or installed on sidewalk, the full extent of sidewalk was approximated. In areas where protection or scaffolding (pedestrian protection from overhead construction) is placed over sidewalk, sidewalk remained unchanged from existing data (not updated). Sidewalks were collected when crossing large medians or traffic islands. Sidewalks overlap the exit and entrance portion(s) of parking lot features. Sidewalks overlap driveways, but not alleys. Sidewalk will be continued under bridges and overpasses if they are visible on both sides of the structure.<br>Interior Sidewalk: Interior sidewalks followed the same general capture rules as other sidewalk features. These features were captured in the following areas: <br>1. NYC Parks<br>2. NYCHA Properties<br>3. Other Residential areas<br>4. Hospital campuses<br>5. School campuses<br>6. Federal Fort<br>The business use of this feature is to identify potential areas, outside of the public Right of Way (ROW), that could permit emergency vehicles through travel.
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SOURCE_ID | Unique Feature Identification Number. | double | No
| FEATURE_CODE | Type of feature.<br>3800 = Sidewalk

 | integer | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set:<br>380000 = ROW Sidewalk<br>380010 = Interior Sidewalk
 | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
