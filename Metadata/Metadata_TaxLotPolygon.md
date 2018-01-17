# Tax Lot Polygon
Geometry Type: SDE Feature Class<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/DTM_Tax_Lot_Polygon.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Tax_Lot_Polygon Feature Class contains polygon features that define each physical tax lot in the City expressed in real-world coordinates (which reference specific locations on the earth's surface).
**Description** |The Tax_Lot_Polygon Feature Class contains polygon features that define each physical tax lot in the City. This definition results in the representation of tax lots with numbers 1 through 999 except in those cases where lot numbers with a value greater than 999 have been used to represent ordinary tax lots. For condominiums, the lot number being referenced here is the base lot number. There are no air rights lots, subterranean lots, condominium unit lots, or pseudo lots (as defined by City Planning) in this feature class. It is a graphical cadastre only in that it is a schematic representation of the City's lot geometry and not a legal cadastre or a survey accurate map of the City's tax lots.
**Source(s)** |Tax Map Unit, NYC Department of Finance
**Publication Dates** |**Data**: 2008<br>**Last Update**: Weekly<br>**Metadata**: 12/22/2016<br>**Update Frequency**: Weekly
**Available Formats** |Zipped DTM includes Feature Classes and Tables. Available on the [NYC Open Data Portal](https://data.cityofnewyork.us/Housing-Development/Department-of-Finance-Digital-Tax-Map/smk3-tmxj)
**Use Limitations** |Not specified
**Access Rights** |Public
**Links** |[DOF Digital Tax Map](http://gis.nyc.gov/taxmap/map.htm)
**Tags** |Tax Lot Polygon
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
| FID | Internal feature number. | OID | 
| BORO | This is a one digit numeric field that identifies the borough in which the associated feature exists.  Boro values range from one (1) to five (5) and are validated against the D_BORO domain. | Number | 
| BLOCK | Block is a five digit numeric field that identifies the block on which the associated feature exists. | Number | 
| LOT | Lot is a four digit numeric field that identifies a unique lot within a tax block.  Although DOF has a set of defined limits for different types of lots, the fact that there are exceptions to these rules makes it impossible to use a domain for validity checking of the lot numbers. | Number | 
| BBL | BBL is a concatenation of Boro-Block-Lot and is stored with every instance of those three fields.  Although the BBL value can always be determined dynamically, this field is maintained in order to simplify indexing, searching and the use of the files by other, as yet undetermined, applications. | String | 
| CONDO_FLAG | The lot defines a condominium complex | String | 
| COMMUNITY_ |  |  | 
| REGULAR_LO | This field is obtained from the RPAD file and identifies those lots that are rectangular. |  | 
| NUMBER_LOT |  |  | 
| REUC_FLAG | An REUC easement exists on part or all of this lot. | Text | 
| LOT_NOTE |  |  | 
| AIR_RIGHTS | An air rights easement exists on this lot. | text | 
| SUBTERRANE | A subterranean easement exists on part or all of this lot. | String | 
| EASEMENT_F | A land easement exists on part or all of this lot | String | 
| SECTION_NU | NYC Tax Section for the specified lot | Number | 
| VOLUME_NUM | Volume number of the book in which this tax lot can be found. | Number | 
| PAGE_NUMBE | Page number on which this tax lot can be found. | Number | 
| CREATED_BY | A field that can be used to identify the operator who created the specific feature. | String | 
| NYCMAP_BLD | This field is used to identify those lots where a building footprint associated with that lot extends beyond the lot boundary. |  | 
| MISSING_RP | This field is used to identify physical lot polygons found in COGIS that were not matched to a record in the ORE file of RPAD. |  | 
| CONVERSION |  |  | 
| VALUE_REFL | This flag identifies those lots whose assessed value has been transferred to another lot. | Y/N | 
| AV_CHANGE |  |  | 
| CREATED_DA | The date the record was created | String | 
| LAST_MODIF | A field that can be used to identify the operator who last modified the specific feature. | String | 
| LAST_MOD_1 | The date the feature or any attribute value associated with it was changed. | Date | 
| BW_CHANGE |  |  | 
| SHAPE | This field is used to store the geometry or shape of the features |  | 
| EFFECTIVE_ |  |  | 
| BILL_BBL_F | This field is used to identify the source of the Billing BBL Lot Number. | String | 
| SHAPE_Leng | This is the system derived length of the feature (where applicable) | Number | 
| SHAPE_Area | This is the system derived area of the feature (where applicable) | Number | 
