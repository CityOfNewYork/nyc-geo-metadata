# REUC Lots
Geometry Type: SDE Table<br><br>

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The REUC_Lots table is a lot attribute table. The REUC_Lots contains one record for each REUC on a tax lot. For a lot with multiple REUC easements, multiple records will exist in this table. A tax lot can have none, one, or multiple REUCs.
**Description** |The REUC_Lots table contains one record for each REUC (Real Estate of Utility Companies) on a tax lot.
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
| OBJECTID | Internal feature number. | Object ID | 
| APPURTENAN | This is a one digit numeric field that identifies the borough to which the attribute is appurtenant.  Boro values range from one (1) to five (5) | String | 
| APPURTEN00 | Block is a five digit numeric field that identifies the block to which the attribute is appurtenant. | Long Integer | 
| APPURTEN01 | Lot is a four digit numberic field that identifies a unique lot within a tax block to which the attribute is appurtenant. | Short Integer | 
| APPURTEN02 | BBL is a cocatenation of Boro-Block-Lot and is stored with every instance of those three fields. Although the BBL value can always be determined dynamically, this field is maintained in order to simplify indexing.  | String | 
| REUC_NUMBE |  |  | 
| DELETED_FL |  |  | 
| CREATED_BY | A field that can be used to identify the operator who created the specific attribute | String | 
| CREATED_DA | The date the record was recorded. | Date | 
| LAST_MODIF | A field that can be used to identify the operator who last modified the specific attribute | String | 
| LAST_MOD00 | The date the attribute was changed | Date | 
| AV_CHANGE |  |  | 
| BW_CHANGE |  |  | 
| EFFECTIVE_ |  |  | 
| GLOBALID | | String |
