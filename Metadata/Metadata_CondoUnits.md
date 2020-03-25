# Condo Units
Geometry Type: SDE Table<br><br>

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Condo_Units table is a lot attribute table. The Condo_Units table contains a single record for each condominium unit within the City.
**Description** |
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
| CONDO_BORO | This is a one digit numeric field that identifies the borough in which the associated feature exists. Boro values range from one (1) to five (5) and are validated against the D_BORO domain.  | String | 
| CONDO_NUMB | A unique identifier for each condominium assigned at the time the condominium is created. Separated by Boro.  | Short Integer | 
| CONDO_KEY | A concatenation of the Condo Boro and Condo Number Fields  | Long Integer | 
| CONDO_BASE | The concatenation of the borough block and lot of the parent lot for the condominium. | String | 
| CONDO_BA00 | A concatenation of the Borough Block and Billing lot that the condo is built on. In the case of a condo on multiple parent lots, one billing lot can represent multiple base lots.  | String | 
| CONDO_BA01 | A concatenation of the Condo_Boro, Condo_Number and the Condo_Base_BBL fields. | String | 
| CONDO_BA02 |  |  | 
| CONDO_BA03 |  |  | 
| UNIT_BORO | This is a one digit numeric field that identifies the borough in which the associated feature exists. Boro values range from one (1) to five (5) and are validated against the D_BORO domain. | String | 
| UNIT_BLOCK | This is a 5 digit numeric field that identifies the block on which the associated feature exists. | String | 
| UNIT_LOT | Lot is a 4 digit numeric field that identifies a unique lot within a tax block.  | String | 
| UNIT_BBL | BBL is a concatenation of Borough Block Lot and is stored with every instance of those three fields.  | String | 
| CREATED_BY | A field that can be used to identify the operator who created the feature. | String | 
| CREATED_DA | The date the feature was created | Date | 
| LAST_MODIF | A field that can be used to identify the operator who last modified the specific feature. | String | 
| LAST_MOD00 | The date the feature or any attribute value associated with it was changed. | Date | 
| AV_CHANGE |  | Short Integer | 
| BW_CHANGE |  | Short Integer | 
| EFFECTIVE_ | Effective tax year for the associated feature.  | String | 
| UNIT_DESIG | The official unit designation for the associated feature | String | 
| GLOBALID | | String |
