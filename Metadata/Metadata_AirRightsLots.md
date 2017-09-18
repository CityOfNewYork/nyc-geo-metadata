# Air Rights Lots
Geometry Type: SDE Table<br><br>

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Air_Rights_Lots table contains one record for every air rights lot in the City.  The associated information is the donating BBL. Air rights lot numbers must be between 9000 and 9989.
**Description** |The Air_Rights_Lots table contains one record for every air rights lot in the City. The associated information is the donating BBL.
**Source(s)** |Tax Map Unit, NYC Department of Finance
**Publication Dates** |**Data**: 2008<br>**Last Update**: Weekly<br>**Metadata**: 12/22/2016<br>**Update Frequency**: Weekly
**Available Formats** |Zipped DTM includes Feature Classes and Tables. Available on the [NYC Open Data Portal](https://data.cityofnewyork.us/Housing-Development/Department-of-Finance-Digital-Tax-Map/smk3-tmxj)
**Use Limitations** |Not specified
**Access Rights** |Public
**Links** |[DOF Digital Tax Map](http://gis.nyc.gov/taxmap/map.htm)
**Tags** |
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
| DONATING_B | This is a one digiti number field that identifies the borough in which the associated feature (donor lot) exists. Boro values range from one (1) to five (5) and are validated against the D_BORO domain. | String | 
| DONATING_1 | Donating block is a five digit numberic field that identifies the blokc on which the associated feature (donor lot) exists. | Long Integer | 
| DONATING_L | Four digit numeric filed that identifies a unique donating lot within a tax block. | Short Int | 
| DONATING_2 | Donating BBL is a concatenation of Boro-Block-Lot and is stored with every instance of those threee fields. Although the BBL value can always be determined dynamically, this field is maintained in order to simplify indexing, searching, and the use of the files by other, as yet undetermined applications.  | String | 
| AIR_RIGHTS | Air Rights BBL is a concatenation of Boro-Block-Lot for the Air lot. Air rights lot numbers must be between 9000 and 9989. | String | 
| AIR_RIGH_1 |  | Long Int | 
| USED_BY_DO |  | Short Integer | 
| CREATED_BY | A field that can be used to identify the operator who created the specific feature. | String | 
| CREATED_DA | The date the record was created | Date | 
| LAST_MODIF | A field that can be used to identify the operator who last modified the specific feature. | String | 
| LAST_MOD_1 | The date the feature or any attribute associated with it was changed. | Date | 
| AV_CHANGE |  | Short Integer | 
| BW_CHANGE |  | Short Integer | 
| EFFECTIVE_ |  | String | 
| AIR_RIGH_2 |  |  | 
