# Historic Districts
Filename: LPC_HD_OpenData_2015Nov<br>Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/HistoricDistricts.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |Provides information regarding all historic districts that have calendared, heard, or designated by the Landmarks Preservation Commission, or for which an LP number has been issued, as well as many proposed districts in the study area phase.
**Description** |This dataset contains boundaries and associated attribute information for all designated historic districts or areas under consideration for historic district designation (i.e. calendared) by the New York City Landmarks Preservation Commission (LPC), including items that may have been denied designation or overturned. Please note that some areas may have multiple records in the database if different actions were taken over time. Please pay close attention to the "CURRENT" and "LAST_ACTION_ON_BOUNDARY" fields to determine the status of a particular area. The geographic locations of the polygons in this dataset are derived primarily from the Department of City Planning's PLUTO dataset, and therefore discrepancies may arise where the LPC dataset has not been updated with information from the most recent PLUTO releases. Please pay close attention to the field descriptions present in the file's metadata to understand how to use this dataset. And please contact LPC if there are questions or concerns
**Source(s)** |Landmarks Perservation Commission (LPC)
**Publication Dates** |**Data**: 03/11/15<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: As needed
**Available Formats** |Shapefile. Additional data formats are available for download on the [NYC Open Data Portal](https://data.cityofnewyork.us/Recreation/Historic-Districts/xbvj-gfnw).
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/Recreation/Historic-Districts/xbvj-gfnw
**Tags** |Landmark, Landmarks, Landmarks Preservation Commission, Historic Preservation, Preservation, LPC, Landmark List, Individual Landmark, Interior Landmark, Scenic Landmark, Historic District, Historic Districts, Boundaries
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |
**Positional Accuracy** |
**Features Captured** |
**Features Excluded** |
**Capture and Update Notes** |The geographic locations of the polygon boundaries in this dataset are derived primarily from the Department of City Planning's PLUTO data. These locations are not necessariliy updated with changes to the aforementioned datasets, and so discrepancies are possible.
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| BOROUGH | Borough expressed as a two character abbreviation (MN=Manhattan, BX=Bronx, BK=Brooklyn, QN=Queens, and SI=Staten Island) | text | No
| LP_NUMBER | Internal LPC identifier (LP-XXXXX) used to identify a single designation (one LP number is assigned per Historic District, Individual, Scenic, or Interior Landmark) | text | No
| CURRENT_ | Indicates whether a record in the database is presently active/current (No=Not active/current; Yes=Active/current) | text | No
| AREA_NAME | Name of the calendared, heard, or designated historic district or study area | text | No
| EXTENSION | Denotes (either yes or no) whether the item is an extension of a previously designated historic district | text | No
| STATUS_OF_ |  | text | No
| LAST_ACTIO | Last Action | text | No
| BOUNDARY_N | Boundary Name | text | No
| DESIG_DATE | Date of designation; Note: This field will be blank for items not designated | date | No
| PUBLIC_HEA |  | text | No
| CALEN_DATE | Date of calendaring; Note: Not all items have a date of calendaring (date of calendaring was not tracked until the 1990s) | text | No
| OTHER_HEAR |  | text | No
