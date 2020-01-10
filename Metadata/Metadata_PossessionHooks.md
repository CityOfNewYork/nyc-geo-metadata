# Possession Hooks
Geometry Type: SDE Feature Class<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/DTM_Possession_Hooks.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Possession Hooks Feature Class contains point features that are used to locate possession hooks on the various lines within the Cadastral feature dataset.
**Description** |The Possession Hooks Feature Class contains point features that are used to locate possession hooks on the various lines within the Cadastral feature dataset. Possession hooks are symbols placed on various line features that are used to identify the fact that the line is not a lot boundary line.
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
| HOOK_TYPE | Short integer defining hook types | Short Integer | 
| ROTATION | ESRI generated field denoting the display angle of the posession hook. | Double | 
| CREATED_BY | A field that can be used to identify the operatior who created the specific feature. | String | 
| CREATED_DA | The date the feature was created | Date | 
| LAST_MODIF | A field that can be used to identify the operator who last modified the feature | String | 
| LAST_MOD00 | The date the feature or any attribute value associated with it was changed. | Date | 
| GLOBALID | | String |
| SHAPE | Feature geometry. | Shapefile |  
