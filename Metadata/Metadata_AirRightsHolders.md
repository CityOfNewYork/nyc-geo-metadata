# Air Rights Holders
Geometry Type: SDE Table<br><br>

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Air_Rights_Holders table is a lot attribute table. The Air_Rights_Holder table contains one record for every unique combination of a tax lot (with a record in Tax_Lot_Polygon) that has received air rights and the air rights lot.
**Description** |The Air_Rights_Holders table contains one record for every unique combination of a tax lot (with a record in Tax_Lot_Polygon) that has received air rights and the air rights lot.
**Source(s)** |Tax Map Unit, NYC Department of Finance
**Publication Dates** |**Data**: 2008<br>**Last Update**: Weekly<br>**Metadata**: 12/22/2016<br>**Update Frequency**: Weekly
**Available Formats** |Zipped DTM includes Feature Classes and Tables. Available on the [NYC Open Data Portal](https://data.cityofnewyork.us/Housing-Development/Department-of-Finance-Digital-Tax-Map/smk3-tmxj)
**Use Limitations** |Not specified
**Access Rights** |Public
**Links** |[DOF Digital Tax Map](http://gis.nyc.gov/taxmap/map.htm)
**Tags** |Air Rights Holders
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
| AIR_RIGHTS | Air Rights BBL is a concatenation of Boro-Block-Lot for the given feature. | String | 
| HOLDING_BB | Holding BBL is a concatenation of Boro-Block-Lot for the given feature. This field relates to a BBL in the Tax_Lot_Polygon feature. | String | 
| AIR_RIGH_1 |  | Long Int | 
| CREATED_BY | A field that can be used to identify the operator who created the specific feature. | String | 
| CREATED_DA | The date the feature was created | Date | 
| LAST_MODIF | This field can be used to identify the operator who last modified the specific feature. | String | 
| LAST_MOD_1 | The date the feature or any attribute value associated with it was changed. | Date | 
| AV_CHANGE |  |  | 
| BW_CHANGE |  |  | 
