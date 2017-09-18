# Tax Lot Face
Geometry Type: SDE Feature Class<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/DTM_Tax_Lot_Face.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Tax_Lot_Face Feature Class contains a polyline feature for each face of each physical tax lot in the City. The tax lot face lines are generated from the Tax_Lot_Polygon features.
**Description** |The Tax_Lot_Face Feature Class contains a polyline feature for each face of each physical tax lot in the City that is represented by a polygon within the Tax_Lot_Polygon feature class. It is a graphical cadastre only in that it is a schematic representation of the City's block geometry and not a legal cadastre or a survey accurate map of the City's tax blocks.
**Source(s)** |Tax Map Unit, NYC Department of Finance
**Publication Dates** |**Data**: 2008<br>**Last Update**: Weekly<br>**Metadata**: 12/22/2016<br>**Update Frequency**: Weekly
**Available Formats** |Zipped DTM includes Feature Classes and Tables. Available on the [NYC Open Data Portal](https://data.cityofnewyork.us/Housing-Development/Department-of-Finance-Digital-Tax-Map/smk3-tmxj)
**Use Limitations** |Not specified
**Access Rights** |Public
**Links** |[DOF Digital Tax Map](http://gis.nyc.gov/taxmap/map.htm)
**Tags** |UnderwaterTax Lot FaceRegular
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
| BORO | This is a one digit numeric field that identifies the borough in which the associated feature exists.  Boro values range from one (1) to five (5) and are validated against the D_BORO domain. | String | 
| BLOCK | Block is a five digit numeric field that identifies the block on which the associated feature exists. | Long Integer | 
| FID | Internal feature number. | Numeric | 
| LOT | Lot is a four digit numeric field that identifies a unique lot within a tax block.  Although DOF has a set of defined limits for different types of lots, the fact that there are exceptions to these rules makes it impossible to use a domain for validity checking of the lot numbers. | Short Integer | 
| TAX_LOT_FA | This field identifies the type of each lot face line.  Lot faces are either "underwater" which as the name implies, are under water or they are "regular" meaning that they are standard lot faces existing on the land surface. | Short Integer | 
| BBL | BBL is a concatenation of Boro-Block-Lot and is stored with every instance of those three fields.  Although the BBL value can always be determined dynamically, this field is maintained in order to simplify indexing, searching and the use of the files by other, as yet undetermined, applications. | String | 
| SOURCE | The Source field is populated during the conversion process and indicates where the value of "Lot_Face_Length" was obtained.  The codes used are obtained from the "D_LOT_FACE_LENGTH_SOURCE" domain | Short Integer | 
| CREATED_BY | A field that can be used to identify the operator who created the specific feature. | String | 
| AV_CHANGE |  |  | 
| LOT_FACE_L | Length of the lot face as obtained from the original COGIS file and subsequently updated. | Double | 
| BW_CHANGE |  |  | 
| BLOCK_FACE | This field is obtained from the original COGIS file and identifies those lot face segments that also form part of the block face polygon. | Short Integer | 
| LOT_FACE_1 | This field is set during the pre-conversion and/or the conversion process to identify lot face segments that do not conform to the required conversion rules. | Short Integer | 
| SHAPE | Feature geometry. | Geometry | 
| CREATED_DA | The date the record was created | string | 
| LAST_MODIF | A field that can be used to identify the operator who last modified the specific feature. | String | 
| LAST_MOD_1 | The date the feature or any attribute value associated with it was changed. | String | 
| APPROX_LEN | Boolean field that indicates if the length is approximate (+/-) | Short Integer | 
| SHAPE_Leng |  | Double | 
