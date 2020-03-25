# Boundary
Geometry Type: SDE Feature Class<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/DTM_Boundary.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Boundary Feature Class contains polyline features that define the following boundary line types: Bulkhead, Easement, Pierhead, Pierhead and Bulkhead, REUC, Riparian, Unclassified (default), Street Widening, High Water Line, Low Water Line, Pier, Slope Line, Deeded Rights, Special Access Rights
**Description** |The Boundary Feature Class contains a variety of line types not directly related to lots.
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
| OBJECTID | Internal feature number. | OID | 
| BOUNDARY_T | Integer value that indicates the subtype of boundary line. Default = 6. Legend: <br>3 - Pierhead and Bulkhead<br>8 - High Water Line<br>4 - REUC<br>5 - Riparian<br>6 - Unclassified<br>7 - Street Widening<br>2 - Pierhead<br>9 - Low Water Line<br>0 - Bulkhead<br>1 - Easement<br>11 - Pier<br>12 - Slope Line<br>13 - Deeded Rights | Short Integer | 
| TYPE | This field is used to store the domain values associated with the sub-types.  Currently only the subtype of "Easement" has a domain associated with it. | Short Integer | 
| ID_NUMBER | Various ID numbers, including REUC Idents. | String | 
| DESCRIPTIO | Verbal description of BOUNDARY_TYPE field. | String |
| LENGTH | Feature length | Double | 
| MODIFIER | Domain: D_BOOLEAN_SYMBOL_VALUE | Short Integer | 
| CREATED_BY | A field that can be used to identify the operator that created the feature. | String | 
| CREATED_DA | The date the feature was created. | Date | 
| LAST_MODIF | This field can be used to indicate the operator who last modified the feature | String | 
| LAST_MOD00 | The date the feature was last modified | Date | 
| EFFECTIVE_ | Effective Tax Year | String | 
| GLOBALID |  | String | 
| SHAPE | Feature geometry. | Geometry | 
| SHAPE_Leng | Esri Automated shape length field | Double | 
