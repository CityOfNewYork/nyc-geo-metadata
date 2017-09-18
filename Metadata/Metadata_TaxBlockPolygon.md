# Tax Block Polygon
Geometry Type: SDE Feature Class<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/DTM_Tax_Block_Polygon.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Tax_Block_Polygon Feature Class contains polygon features that define each physical tax block in the City expressed in real-world coordinates which reference specific locations on the earth's surface.  It is a graphical cadastre only in that it is a schematic representation of the City's block geometry and not a legal cadastre or a survey accurate map of the City's tax blocks.
**Description** |The Tax_Block_Polygon Feature Class contains polygon features that define each physical tax block in the City. It is a graphical cadstre only in that it is a schematic representation of the City's block geometry and not a legal cadstre or a survey accurate map of the City's tax blocks.
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
**Spatial Coverage** |
**Temporal Coverage** |
**Positional Accuracy** |
**Features Captured** |
**Features Excluded** |
**Capture and Update Notes** |
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| FID | Internal feature number. | OID | 
| BORO | This is a one digit numeric filed that identifies the borough in which the associated feature exists. Boro values range from one (1) to five (5) and are validated against the D_BORO domain. | String | 
| BLOCK | Block is a five digit numeric field that identifies the blokc on which the asociated feature exists.  | Long Integer | 
| CREATED_BY | A field that can be used to identify the operator who created the specific feature. | String | 
| EOP_OVERLA | Based on the block configuration and the priorities of the conversion rules, this tax block could not fit within the NYCMap polygon that defines the edge of pavement. | Short Integer | 
| JAGGED_ST_ | Based on the block configuration and the priorities of the conversion rules, this tax block could not be aligned within the NYCMap polygon that defines the edge of pavement in such a way as to produce a straight row of tax blocks on the street. | Short Integer | 
| SHAPE | Feature geometry. | Shape | 
| CREATED_DA | The date the record was created | Date | 
| LAST_MODIF | A field that can be used to identify the operatior who last modified the specific feature | String | 
| LAST_MOD_1 | The date the feature of any attribute value associated with it was changed | Date | 
| SECTION_NU | NYC Tax Section for the specified block | Short Integer | 
| VOLUME_NUM | Volume number of the book in which this tax lot can be found. | Short Integer | 
| SHAPE_Area | Area of feature in internal units squared. |  | 
| Shape_Len | This is the system derived length of the feature (where applicable) | Double | 
