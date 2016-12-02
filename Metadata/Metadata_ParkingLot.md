# Parking Lot
Filename: PARKING_LOT<br>Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/raw/master/Images/FeatureViews/Parking_Lot.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |This feature class contains parking lots (paved or unpaved) greater than 2,000 sq. feet. Traffic islands within parking lots are not delineated. This feature class does not include gas stations, private lots, storage areas, etc as parking lots.Additionally, Parking areas adjacent to the travel-way BUT NOT separated from the travel-way by a curb or other obstruction are not parking lots. These parking areas are to be part of the roadbed. Parking areas adjacent to the travel-way AND separated from the travel-way by a curb or other obstruction are parking lots. 
**Source(s)** |Current imagery and previous planimetric database
**Publication Dates** |**Data**: 10/07/14<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: 
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/City-Government/Parking-Lot/h7zy-iq3d)
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/City-Government/Parking-Lot/h7zy-iq3d
**Tags** |structure, NYCMap, imageryBaseMapsEarthCover, transportation, Landbase, Basemap, Parking, Planimetric, Outdoor Parking, Parking Lot
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |All parking lots (paved or unpaved) greater than 2,000 sq. feet. Parking areas adjacent to the travel-way and separated from the travel-way by a curb or other obstruction were captured as parking lots. In these cases, the Roadbed and Pavement Edge end or wrap around the parking lot. The parking lot is not included as part of the Roadbed.
**Features Captured** |Traffic islands within parking lot were not captured. When a building of > 400 sq. feet was present, the building area was excluded from the parking lot polygon. Parking areas adjacent to the travel-way, but not separated from the travel-way by a curb or other obstruction, were not captured. Instead, those parking areas were included as part of the Roadbed and the Pavement Edge extends to the outside edge of such area. Gas stations, private parking areas (e.g., for condos), and storage areas (e.g., for boats) were not captured.
**Features Excluded** |
**Capture and Update Notes** |These features connect to road edge (Curb or Edge of Pavement) only at entrances and exits.
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SOURCE_ID | Unique Feature Identification Number. | double | No
| FEATURE_CODE | Type of feature.<br>5000 = Parking Lots > 2000 Square Feet

 | integer | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set. <br>500000 = Parking Lots > 2000 Square Feet | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
