# Transport Structure
Filename: TRANSPORT_STRUCTURE<br>Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/raw/master/Images/FeatureViews/Bridge.JPG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |This feature class contains the following Transportation structures:<br>BRIDGE - Structure erected over obstacle for road traffic (road, railroad, hydrography).<br>TUNNEL - Underground throughways.<br>RAIL BRIDGE - Structure erected over obstacle for railroad traffic (road, railroad, hydrography).<br>PEDESTRIAN/BIKE BRIDGE - Structure erected over obstacle for pedestrian and / or bicycle traffic (road, railroad, hydrography).<br>RAILROAD VIADUCT - Bridge composed of several small arches, mostly over water.<br>OVERPASS - Structure erected over road, whereas the lower road has been excavated and has retaining walls on the side. Overpass is at terrain level.
**Source(s)** |Current imagery and previous planimetric database
**Publication Dates** |**Data**: 11/17/14<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: 
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/City-Government/Transportation-Structures/h9sf-7bej)
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/City-Government/Transportation-Structures/h9sf-7bej
**Tags** |structure, Planimetric, Transportation, Overpass, Basemap, Transportation Structures, Tunnel, imageryBaseMapsEarthCover, Landbase, Bridge, transportation, NYCMap
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |
**Features Captured** |The following features were captured for each subtype: <br> Bridge: Structures erected over obstacles for road traffic (road, railroad, hydrography). Bridge deck outlined from joint to joint when on-and off-ramp(s) are on ground. Large bridges with on-ramps and off-ramps were collected from bridge elevation points (Bridge Elevation).<br>Tunnel: Used tunnel portal to digitize. <br>Rail Bridge: Structure erected over obstacle for railroad traffic (road, railroad, hydrography).<br>Pedestrian/Bike Bridge: Strutures allowing pedestrians/bicycles to cross transportation features.<br>Railroad Viaduct: Bridge composed of several small arches, mostly over water.<br>Overpass: Structure erected over road, whereas the lower road has been excavated and has retaining walls on the side.
**Features Excluded** |The following features were excluded from each subtype: <br>Pedestrian/Bike Brige: Skybridges connecting buildings were collected as buildings.
**Capture and Update Notes** |The following capture notes for each subtype captured:<br>Bridge: Features can overlap so that bridge is not split where it crosses another bridge feature.<br>Tunnel: Maintained delineation from existing data when available.<br>Pedestrian/Bike Bridge: Where applicable, outline includes stairs. Can connect between buildings (snapped to building footprint).<br>Railroad Viaduct: Visible changeover from solid ground to viaduct is outlined.<br>Overpass: Overpass is at terrain level.
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SOURCE_ID | Unique Feature Identification Number. | double | No
| FEATURE_CODE | Type of feature.<br>2300 = Bridge<br>2310 = Tunnel<br>2320 = Rail Bridge<br>2330 = Pedestrian Bridge<br>2340 = Railroad Viaduct<br>2350 = Overpass

 | integer | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set:<br>230000 = Bridge<br>231000 = Tunnel<br>232000 = Rail Bridge<br>233000 = Pedestrian Bridge<br>234000 = Railroad Viaduct<br>235000 = Overpass
 | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
| NAME | Name of Transportation Strucutre | text | No
