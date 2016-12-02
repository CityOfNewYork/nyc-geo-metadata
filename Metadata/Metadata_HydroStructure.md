# Hydro Structure
Filename: HYDRO_STRUCTURE<br>Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/raw/master/Images/FeatureViews/Pier.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |This feature class contains the following Hydro structures:<br>PIERS = Deck supported by posts extending into the water.<br>JETTY = Structure, usually stone, earth, or concrete extending from shore to lessen erosion, in continuation of river channels at their outlets or into docks, and outside their entrances. Delineated at the water level.<br>SEAWALL = Typically, a seawall is built on the land parallel to the coast, but may also apply to breakwaters that are built into the water.
**Source(s)** |Current imagery and previous planimetric database
**Publication Dates** |**Data**: 11/17/14<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: As needed
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/City-Government/Hydrography-Structures/53au-zf7x)
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/City-Government/Hydrography-Structures/53au-zf7x
**Tags** |structure, NYCMap, Hydrography, Hydro Structures, imageryBaseMapsEarthCover, transportation, Pier, Water, Landbase, Seawall, Basemap, Jetty, Hydrography Structures, Planimetric, Hydro
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |
**Features Captured** |Decks supported by posts extending into the water (Piers). Structures, usually comprised of stone, earth, or concrete; extending from shore to lessen erosion. They are often installed in continuation of river channels at their outlets or into docks, and outside their entrances (Jetty). Seawalls are typically built on the land parallel to the coast, but may also include breakwaters that are built into the water.
**Features Excluded** |Individual/private docks for recreational watercraft were not captured, unless they had already been captured as such in existing planimetric data.
**Capture and Update Notes** |Piers, commercial piers, and docks were updated using existing planimetrics data as guide. Jetty features are delineated at the water level.
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SOURCE_ID | Unique feature Identification Number. | double | No
| FEATURE_CODE | Type of feature.<br>2800 = Piers<br>2810 = Jetty<br>2820 = Seawall | integer | No
| SUB_FEATURE_CODE | A subset of features within a given "Feature_Code" set.<br>280000 = Pier<br>280010 = Pier, Breakwater<br>280020 = Pier, Causeway<br>280030 = Pier, Dock<br>280040 = Pier, Structure on <br>280050 = Pier, Wharf<br>281000 = Jetty, Regular<br>281010 = Jetty, Structure on<br>282000 = Seawall | integer | No
| ELEVATION | Field measuring surface elevation above sea level (in feet).  | double | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
