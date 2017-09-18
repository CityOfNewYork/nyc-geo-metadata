# Condo
Geometry Type: SDE Table<br><br>

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Condo table is a lot attribute table. The Condo table contains one or more records for each condominium complex in the City as identified in RPAD and on the scanned tax maps. The unique key for this table is Condo_Key + Condo_Base_BBL which is the concatenation of the Condo_Boro, Condo_Number and the Condo_Base_BBL fields. In those instances where a condominium exists on multiple base lots, multple records will exist in this table. Each record can only have a single billing lot. If a condominium is built on air rights, the Air Rights Condo Flag will be set and the Condo Key and Air Rights BBL(s) will be entered in the Air Rights Condos table.
**Description** |The Condo table contains one or more records for each condominium complex in the City as identified in RPAD and in the scanned tax maps. NOTE: If a condominium is built on air rights, the Air Rights Condo Flag will be set and the Condo Key and Air Rights BBL(s) will be entered in the AirRights Condos table.
**Source(s)** |Tax Map Unit, NYC Department of Finance
**Publication Dates** |**Data**: 2008<br>**Last Update**: Weekly<br>**Metadata**: 12/22/2016<br>**Update Frequency**: Weekly
**Available Formats** |Zipped DTM includes Feature Classes and Tables. Available on the [NYC Open Data Portal](https://data.cityofnewyork.us/Housing-Development/Department-of-Finance-Digital-Tax-Map/smk3-tmxj)
**Use Limitations** |Not specified
**Access Rights** |Public
**Links** |[DOF Digital Tax Map](http://gis.nyc.gov/taxmap/map.htm)
**Tags** |Condo
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
| CONDO_BORO | Borough in which the condominium resides. | String | 
| CONDO_KEY | This field is a concatenation of the Condo_Boro and Condo_number fields. | Long Integer | 
| CONDO_NAME | This field represents the name of the condominium. | String | 
| CONDO_BASE | This field is the BBL for the base lot on which the condo is built. BBL is a concatenation of Borough Block and Lot numbers.  | String | 
| CONDO_BILL | This field is the concatenation of the billing lot's (series 7501, 7502, 7503, etc.) borough, block, and lot. Each record can only have a single Billing lot | String | 
| CONDO_BA_1 |  |  | 
| AIR_RIGHTS | This flag is used to identify condominiums which are built on air rights lots. | Short Integer | 
| BILLING_LO | The flag field is populated during the conversion process to indicate that the billing lot number for this condominium was not found in the COGIS file. | Short Integer | 
| CREATED_BY | a fiedl that can be used to identify the operatior who created that specific feature | String | 
| CREATED_DA | The date the record was created | Date | 
| LAST_MODIF | A field that can be used to identify the operator that last modified the field` | String | 
| LAST_MOD_1 | The date the record was last modified | Date | 
| AV_CHANGE |  |  | 
| BW_CHANGE |  |  | 
| CONDO_NUMB | Five digit unique identifier for each condominium | Short Integer | 
