# Lot Face Possession Hooks
Geometry Type: SDE Feature Class<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/DTM_Lot_Face_Possession_Hooks.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Lot_Face_Possession_Hooks Feature Class contains point features that define the following possession hook types: - Regular - Underwater and indicate that the owner of the tax lot has "rights" to the area beyond the lot face.
**Description** |The Lot_Face_Possession_Hooks Feature Class contains point features that are used to locate possession hooks on lot face lines. Lot face possession hooks are symbols placed on lot face line features that are used to identify the fact that the line is a lot boundary line and not to be confused with a general boundary lineoutside the lot extents.
**Source(s)** |Tax Map Unit, NYC Department of Finance
**Publication Dates** |**Data**: 2008<br>**Last Update**: Weekly<br>**Metadata**: 12/22/2016<br>**Update Frequency**: Weekly
**Available Formats** |Zipped DTM includes Feature Classes and Tables. Available on the [NYC Open Data Portal](https://data.cityofnewyork.us/Housing-Development/Department-of-Finance-Digital-Tax-Map/smk3-tmxj)
**Use Limitations** |Not specified
**Access Rights** |Public
**Links** |[DOF Digital Tax Map](http://gis.nyc.gov/taxmap/map.htm)
**Tags** |UnderwaterPossession hookRegular
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
| ROTATION | Rotation for placement of posession hooks | Double | 
| CREATED_BY | A field that can be used to identify the operator who created the specific feature. | String | 
| FID | Internal feature number. | Object ID | 
| SHAPE | Feature geometry. | Geometry | 
| LOT_FACE_P | Indicates the type of possession hook, where 0= regular and 1= underwater. | Short Integer | 
| CREATED_DA | The date the record was created. | Date | 
| LAST_MODIF | A field that can be used to identify the operator who last modified the feature. | String | 
| LAST_MOD_1 | The date the feature or any attribute value associated with it was changed. | Date | 
