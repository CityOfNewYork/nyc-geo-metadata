# Subterranean Lots
Geometry Type: SDE Table<br><br>

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Subterranean_Lots table is a lot attribute table. The Subterranean_Lots table contains one record for every subterranean rights lot in the City. The associated information is the donating BBL. A tax lot can have none, one, or multiple subterranean lots. 
**Description** |The Subterranean_Lots table contains one record for every subterranean rights lot in the City. The associated information is the donating BBL. The associated information is the donating BBL. Subterranean rights lot numbers must be between 8000 and 8999.
**Source(s)** |Tax Map Unit, NYC Department of Finance
**Publication Dates** |**Data**: 2008<br>**Last Update**: Weekly<br>**Metadata**: 12/22/2016<br>**Update Frequency**: Weekly
**Available Formats** |Zipped DTM includes Feature Classes and Tables. Available on the [NYC Open Data Portal](https://data.cityofnewyork.us/Housing-Development/Department-of-Finance-Digital-Tax-Map/smk3-tmxj)
**Use Limitations** |Not specified
**Access Rights** |Public
**Links** |[DOF Digital Tax Map](http://gis.nyc.gov/taxmap/map.htm)
**Tags** |Subterranean Lot
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
| APPURTENAN | This is a one digit numeric field that identifies the borough in which the associated feature is appurtenant to.  Boro values range from one (1) to five (5)  | String | 
| APPURTEN_1 | Block is a five digit numeric field that identifies the block on which the associated feature is appurtenant to.  | Long Integer | 
| APPURTEN_2 | Lot is a four digit numeric field that identifies a unique lot within a tax block that the attribute is appurtenant to.  | Short Integer | 
| APPURTEN_3 | BBL is a concatenation of Boro-Block-Lot and is stored with every instance of those three fields.  Although the BBL value can always be determined dynamically, this field is maintained in order to simplify indexing, searching and the use of the files by other, as yet undetermined, applications. | String | 
| SUBTERRANE | Lot is a four digit numeric field that identifies a unique lot within a tax block that the attribute is appurtenant to. Subterranean rights lot numbers must be between 8000 and 8999. | Long Integer | 
| CREATED_BY | A field that can be used to identify the operator who created the specific attribute. | String | 
| CREATED_DA | The date the record was created | Date | 
| LAST_MODIF | A field that can be used to identify the operator who last modified the attribute. | String  | 
| LAST_MOD_1 | The date the feature of any attribute value associated with it was changed.  | Date | 
| AV_CHANGE |  | Short Integer | 
| BW_CHANGE |  | Short Integer | 
| EFFECTIVE_ |  | String | 
