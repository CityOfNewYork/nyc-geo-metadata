# Landmarks
Filename: LPC_LL_OpenData_2015Nov<br>Geometry Type: point<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/Landmarks.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |
**Description** |This dataset contains information on all items designated or under consideration for designation (i.e. calendared) by the New York City Landmarks Preservation Commission (LPC), including items that may have been denied designation or overturned. The dataset contains records for each individual, scenic, or interior landmark, as well as properties or sites located within the boundaries of historic districts. Please note that points in this dataset represent individual buildings in addition to non-building sites (such as vacant lots or monuments) regulated by LPC. It is possible for a single property to have multiple designations (such as individual and interior designations, or individual and historic district). For this reason, it is not uncommon to see multiple points on a single tax lot and multiple records for a single property within the database. Please pay close attention to the "MOST_CURRENT," "BBL_STATUS and "LAST_ACTION_ON_LP" fields, which together denote the designation status of a site/property (see Attribute Definitions for more information). The geographic locations of the points in this dataset are derived primarily from the Department of City Planning's PLUTO data in combination with the Department of Information Technology & Telecommunication's building footprint information. Because this dataset is not automatically updated when changes occur in the underlying dataset, BIN numbers and tax lot information are potentially out of date. Please pay close attention to the field descriptions present in the file's metadata to understand how to use this data set.
**Source(s)** |Landmarks Perservation Commission (LPC)
**Publication Dates** |**Data**: 03/11/15<br>**Last Update**: 08/11/15<br>**Metadata**: 12/02/16<br>**Update Frequency**: As needed
**Available Formats** |Shapefile. Additional data formats are available for download on the [NYC Open Data Portal](https://data.cityofnewyork.us/Recreation/Individual-Landmarks/ch5p-r223).
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/Recreation/Individual-Landmarks/ch5p-r223
**Tags** |landmark, historic districts, landmarks preservation comission, historic preservation, LPC, landmark list, individual landmark, interior landmark, scenic landmark
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
**Capture and Update Notes** |
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| BIN_NUMBER | Department of Buildings "Building Identification Number;" Note: numbers in this field are not auto-updated and so some may be outdated; BINs here are derived using building footprint GIS shapefiles from the NYC Department of Information Technology and Telecommunication (DoITT) (2007-2009); because this file contains both building and non-building landmarks (such as monuments or vacant lots), some records display "dummy" BIN numbers; the following BIN #s serve only as "dummy" BIN #s: 1000000, 2000000, 3000000, 4000000, 5000000 | double | No
| BBL | Concatenation of the borough code (1=MN, 2=BX,3=BK,4=QN,5=SI), the five digit tax map block and four digit tax map lot numbers (ex. Manhattan Tax Map Block 123 Lot 45 would appear as 1001230045); Note: numbers in this field are no auto-updated and so some may be outdated; because this file contains both building and non-building landmarks (such as monuments or vacant lots) as well as some landmarks not located on tax map lots (such as bridges), some records display "dummy" BBLs; the following BBLs serve only as "dummy" BBLs: 1000000000, 2000000000, 3000000000, 4000000000, 5000000000 | text | No
| BOROUGHID | Borough expressed as a two character abbreviation:<br>MN = Manhattan<br>BX = Bronx<br>BK = Brooklyn<br>QN = Queens<br>SI = Staten Island | text | No
| BLOCK | The five digit tax map block number, without leading zeros (ex. tax lot 00123 appears as 123) | double | No
| LOT | The four digit tax map lot number, without leading zeros (ex. Lot 0456 appears as 456) | double | No
| LP_NUMBER | Internal LPC identifier (LP-XXXXX) used to identify a single action (ex. designation), such as an Historic District or Individual Landmark; Note: Buildings within Historic Districts share a single LP number; multiple buildings designated as part of  the same Individual or Scenic landmark will also share a single LP number | text | No
| LM_NAME | Official name of the Individual, Scenic, or Interior landmark or of the Historic District as it appears in the designation report | text | No
| PLUTO_ADDR | Pluto Address | text | No
| DESIG_ADDR | Designated Address | text | No
| DESIG_DATE | Date of designation; Note: This field will be blank for items not designated | date | No
| CALEN_DATE | Date of calendaring; Note: Not all items have a date of calendaring (date of calendaring was not tracked until the 1990s) | date | No
| PUBLIC_HEA |  | text | No
| LM_TYPE | Type of landmark: Individual, Scenic, Interior, or Historic District; Note: Properties can have multiple designations, e.g. Individual and Interior, or Historic District and Individual; each designation type will have its own entry (i.e. record) in the database | text | No
| HIST_DISTR |  | text | No
| OTHER_HEAR |  | text | No
| BOUNDARIES | Whether the landmark site is the entire tax lot ("Block & Lot") or part of the lot ("Partial lot" or "See designation report" or "See public hearing record") | text | No
| MOST_CURRE |  |  | No
| STATUS | Present designation status of the specific BIN/building (**NOT** the status of/last action on the LP number); all items are either NOMINATED, CALENDARED, or DESIGNATED, or NOT DESIGNATED; NOTE: To determine the present status of any item on the Landmark List, "MOST_CURRENT", "STATUS" and "LAST_ACTION_ON_LP" must be looked at collectively. DESIGNATED records will appear as "MOST_CURRENT"=1, "STATUS"=DESIGNATED and "LAST_ACTION_ON_LP"=DESIGNATED | text | No
| LAST_ACTIO |  | text | No
| STATUS_NOT |  | text | No
| COUNT_BLDG | Binary field (0,1) indicating whether a record should be counted as a building; Note: This field is only valid for designated items; note, this field should never be used alone as the basis of public-facing queries | integer | No
| NON_BLDG | Text field indicating whether a record is a non-building site and describing the entity; Note: This field contains text markers that are an integral part of the complex queries that comprise the official LPC count of "buildings and sites" | text | No
| VACANT_LOT | Binary field (0,1) indicating whether a record is a vacant lot; Note: This field is not consistently maintained, meaning items vacant at time of designation but later built upon are not consistently updated (therefore, should never become the basis of its own public-facing query; use PLUTO instead) | integer | No
| SECND_BLDG | Binary field (0,1) indicating whether a record could be considered a secondary building (ex. Garage, shed, etc.); Note: Secondary buildings are counted as part of LPC's definition of "buildings and sites" and the field is not consistently updated (therefore, should never become the basis of its own public-facing query) | integer | No
