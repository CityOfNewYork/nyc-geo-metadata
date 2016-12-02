# Pavement Edge
Filename: PAVEMENT_EDGE<br>Geometry Type: Polyline<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/raw/master/Images/FeatureViews/Road_Edge.JPG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |This feature class contains lines representing the edge of pavement.<br>EDGE OF PAVEMENT - Line features placed between the roadbed and other features (i.e. Curbs, sidewalks, or grass.) Each segment is continuous across a blockface (typically from one intersection to the next -along that side of the road).<br>AIRPORT RUNWAY -Line features representing the outer-edge of all paved airport features, including runways, taxiways and aprons.<br>ALLEY - edge of pavement along narrow unnamed street that allows access to buildings/garages other than from the road. 
**Source(s)** |Current imagery and previous planimetric database
**Publication Dates** |**Data**: 06/25/14<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: 
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/Environment/Pavement-Edge/x9uq-u3qs)
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/Environment/Pavement-Edge/x9uq-u3qs
**Tags** |
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |The following features were captured for each subtype: <br>Edge of Pavement: Updated all segments between pavement and other surfaces or features (i.e. Curbs, sidewalks, or grass).<br><br> Airport Runway: The outer-edge of all paved features associated with airports, including runways, taxiways and aprons. <br><br>Alley: These features represent a narrow unnamed street that allows access to buildings/garages other than from the road. When captured, these features were snapped to the road edge.

**Features Captured** |
**Features Excluded** |
**Capture and Update Notes** |The following capture notes for each subtype captured:<br>Edge of Pavement: Each segment was captured as a continuous feature across a blockface (typically from one intersection to the next - along that side of the road). The vertex between two segments was often located at the street corner. Edge of Pavement features are continuous across driveways, alleys, or access to parking. The one exception to this rule is where a street segment changes names (as determined by CSCL Centerline names) outside of any street intersections. In these cases, the existing CSCL break (node) was used to create corresponding breaks in Pavement Edge segments. For cul-de-sacs, two segments were created. The CSCL centerline was used to define the breakpoints of the Pavement Edge segments. Dead end streets were terminatde where the tax map crosses the road. Two segments were created on left and right sides of CSCL. On highways, Pavement Edge corresponds to the 'roadbed' sub-feature class in Roadbed, and does not include the shoulder.<br><br> The features often share an edge with a building feature. Airport features were collected up to the surrounding fence or gates. <br><br> Alley: These feature typically allow access to the interior of a block or to the back of a house. As a general rule of thumb, the CSCL value of: RW_TYPE=10 was used to determine the alley pavement edge. However, there were still alleys captured that did not have this field attribute value from the CSCL.
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SOURCE_ID | Unique Feature Identification Number. | double | No
| FEATURE_CODE | Type of feature.<br>2230 = Airport Runways<br>2260 = Road Edge<br>2270 = Alley
 | integer | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set. <br>223000 = Airport Runways<br>226000 = Road Edge<br>226020 = Road Edge, Unpaved<br>227000 = Alley | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
| BLOCKFACEID | Unique Identification Number for city block corresponding to street center line | integer | No
| CONFLATED | Indicates if blockface ID corresponds with a street center line.<br>0 = No<br>1 = Yes | integer | No
