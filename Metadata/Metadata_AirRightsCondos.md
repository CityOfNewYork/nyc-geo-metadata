# Air Rights Condos
Geometry Type: SDE Table<br><br>

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Air_Rights_Condos table is a lot attribute table. The Air_Rights_Condos table contains one record for each air rights lot that a condominium is built on. An air rights lot cannot be the 'base lot' of a condominium. A record can only exist in this table if the Air_Rights_Condo_Flag is set to "Yes".
**Description** |The Air_Rights_Condos table is a 'child' of the condominium table and contains one record for each air rights lot that a condominium is built on.
**Source(s)** |Tax Map Unit, NYC Department of Finance
**Publication Dates** |**Data**: 2008<br>**Last Update**: Weekly<br>**Metadata**: 12/22/2016<br>**Update Frequency**: Weekly
**Available Formats** |Zipped DTM includes Feature Classes and Tables. Available on the [NYC Open Data Portal](https://data.cityofnewyork.us/Housing-Development/Department-of-Finance-Digital-Tax-Map/smk3-tmxj)
**Use Limitations** |Not specified
**Access Rights** |Public
**Links** |[DOF Digital Tax Map](http://gis.nyc.gov/taxmap/map.htm)
**Tags** |Air Rights Condos
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |Dataset was created in 2008
**Positional Accuracy** |
**Features Captured** |
**Features Excluded** |
**Capture and Update Notes** |
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| OID | Internal feature number. | OID | 
| CONDO_KEY | This field is a concatenation of the Condo_boro and Condo_Number fields. | Long Int | 
| CONDO_BASE | This field is the BBL for the base ot on which the condo is built. BBL is a concatenation of Boro-Block-Lot. | String | 
| CONDO_BA_1 |  | String | 
| AIR_RIGHTS | This field is the BBL for the air lot on which the condo is built. BBL is a concatenation of Boro-Block-Lot | String | 
| AV_CHANGE |  |  | 
| BW_CHANGE |  |  | 
