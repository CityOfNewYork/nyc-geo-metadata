# Building Historic
Geometry Type: polygon<br><br>![image](../Images/building-historic.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The New York City Office of Technology and Innovation GIS unit maintains and distributes an accurate 'basemap' for New York City. The basemap provides the foundation for almost all other geospatial data in New York City.
**Description** |Historic Building footprints represent buildings that have been demolished or significantly altered. As with the building footprint features, historic footprints represent the full perimeter outline of each building as viewed from directly above. Additional attribute information maintained for each feature includes: Building Identification Number (BIN); Borough, Block, and Lot information; ground elevation at building base; roof height above ground elevation; construction year; demolition year; and feature type.
**Source(s)** |Annually captured aerial imagery, Research of Department of Buildings records and other NYC records, EagleView Oblique imagery, Cyclomedia panoramic photographs.
**Publication Dates** |**Last Update**: Weekly<br>**Metadata**: 01/13/2025<br>**Update Frequency**: Features are updated daily by OTI staff and regularly published on [NYC Open Data](https://opendata.cityofnewyork.us/) and [NYCMaps](https://nycmaps-nyc.hub.arcgis.com/). 
**Available Formats** |Multiple formats. See links below.
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html)
**Access Rights** |Public
**Links** |[Public](https://nycmaps-nyc.hub.arcgis.com/datasets/nyc::building-historic/about) <br> [REST service](https://services6.arcgis.com/yG5s3afENB5iO9fj/arcgis/rest/services/BUILDING_HISTORIC_view/FeatureServer) <br> [City Employees](https://nyc.maps.arcgis.com/home/item.html?id=780dd00c689f444cb20070185fada44d) <br>
**Tags** |Buildings, Building footprint, BIN, Structure
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot ([epsg:2263](https://spatialreference.org/ref/epsg/2263/)); Vertical Datum NAVD 1988
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Positional Accuracy** |Estimated positional accuracy for photogrammetrically updated features (those with GEOM_SOURCE = Photogrammetric) is +/- 2 feet and meets ASPRS Class 1 horizontal mapping standards and ASPRS vertical Class 2 accuracy specifications.  The mapping standards deal with Root Mean Square (RMS) calculations that states if a random number of clearly identifiable surveyed ground control points throughout the project were compared to the mapped features, the RMS of the points would not exceed 2'. In layman's terms,  95% of the data is accurate to +/- 2'.<br>Features with GEOM_SOURCE = Other (Manual) are captured by heads-up digitizing using the most current orthophotography available. These will be somewhat less accurate than the photogrammetrically updated features. 
**Features Captured** |All buildings >400 sq. feet and taller than 12 feet.  We also include other buildings with Building Identification Numbers (BINs) maintained by city agencies. 
**Features Excluded** |Interior divisions.<br>Temporary trailers or tents.  <br>Movable jet bridges for access to aircraft.<br>Awnings, scaffolds, or sidewalk sheds.<br>Small tool or storage sheds in backyards which have no visible car access. 
**Capture and Update Notes** |We move building footprints to building_historic when they are demolished or significantly altered. See [building footprints](.Metadata/Metadata_BuildingFootprints.md) for original capture and update notes.

## 3. Attribute Information 
---------------------------------------------
| Attribute | Shapefile Attribute | Description | Field Type | Notes | 
|------------ | ------------- | -------- | ----------- | ----------|
| OBJECTID | OBJECTID or FID | Synthetic key populated by internal software | number | This key does not consistently identify a building in published datasets. It will uniquely identify a record in a given dataset. |
| NAME | NAME | Building name. Limited to commonly known names).  | text | This field has not been actively maintained since the original creation of this dataset. |
| BIN | BIN | Building Identification Number. A number assigned by the Department of City Planning and used by the Department of Buildings to reference information pertaining to an individual building. The first digit is a borough code (1 = Manhattan, 2 = The Bronx, 3 = Brooklyn, 4 = Queens, 5 = Staten Island). The remaining 6 digits are intended to be unique for buildings within that borough. In some cases where these 6 digits are all zeros (e.g. 1000000, 2000000, etc.) the BIN is unassigned or unknown. | number | This identifier is not unique. |
| HEIGHT_ROOF | HEIGHTROOF | The height of the roof above the ground elevation, not height above sea level.  | number | Records where this is zero or NULL mean that this information was not available. Sources include (1) Final as-built heights as shown in plan drawings posted on Department of Buildings BIS website (2) EagleView Oblique imagery, direct measurements taken on photogrammetrically controlled aerial imagery (3) Cyclomedia imagery, direct measurements were taken on photogrammetrically controlled terrestrial imagery (for buildings less than 60 feet tall, only). |
| LAST_EDITED_DATE | LSTMODDATE or DATE_LSTMO | Feature last modified date.  | date | This is the date that we added the record to the dataset, not the date that the building was demolished. |
| LAST_STATUS_TYPE | LSTSTATTYPE | Feature last status type (Demolition, Alteration, Geometry, Initialization, Correction, Marked for Construction, Marked For Demolition, Constructed). | text | Recent records should be either demolition or alteration. Older records were not consistently updated. |
| DOITT_ID | DOITT_ID | Consistent unique identifier now assigned by OTI (formerly DOITT).  | number | This column did not exist in earlier versions of the data. Those older records will have doitt_id 0. |
| CONSTRUCTION_YEAR | CNSTRCT_YR | The year construction of the building was completed. | number | Originally this column was populated using the Department of Finance Real Property Assessment Database (RPAD). After 2017 we used imagery and city information systems to populate this value in real time.  For buildings where construction year is zero or NULL this information was not available. |
| DEMOLITION_YEAR | DEMOL_YR | The year the building was demolished or significantly altered. | number | |
| BASE_BBL | BASE_BBL | Borough, block, and lot number for the tax lot that the footprint was physically located within.  | text | Field type is text but only numbers are allowed. <br> Buildings occasionally will be associated with lots that they are not physically located within due to temporary synchronziation issues between city agencies.  Some buildings without property taxes will also fall outside of their identified tax lot. |
| MAPPLUTO_BBL | MPLUTO_BBL | Borough, block, and lot number to be used for joining the building footprints data to DCP's [MapPLUTO](https://www.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page) data, which aggregates data for condominium buildings using DOF's billing BBL. For non-condominium buildings the billing BBL is the same as the BASE_BBL. For condominium buildings the billing BBL may be the same for multiple buildings on different physical tax lots if they are part of the same billing unit for Department of Finance purposes. | text | This column did not exist in earlier versions of the data. Those older records will not have mappluto_bbls. Field type is text but only numbers are allowed. |
| GEOM_SOURCE | GEOM_SOURCE | Indicates the reference source used to add or update the feature. Photogrammetric means the feature was added or updated using photogrammetric stereo-compilation methodology. This is the most accurate update method and should conform to the ASPRS accuracy standards. Other (Manual) means the feature was added or updated by heads-up digitizing from orthophotos or approximated from a plan drawing. These features will be generally be less accurate and may not conform to the ASPRS accuracy standards. | text | |
| FEATURE_CODE | FEAT_CODE | Type of Building. List of values:<br>1000 = Parking<br>1001 = Gas Station Canopy<br>1002 = Storage Tank<br>1003 = Placeholder (triangle for permitted bldg)<br>1004 = Auxiliary Structure (non-addressable, not garage)<br>1005 = Temporary Structure (e.g. construction trailer)<br>1006 = Cantilevered Building<br>2100 = Building<br>2110 = Skybridge<br>5100 = Building Under Construction<br>5110 = Garage<br> | number | |
| GROUND_ELEVATION | GROUNDELEV | Lowest Elevation at the building ground level. Calculated from LiDAR or photogrammetrically. | number | Accuracy varies but when collected photogrammetrically or from modern sources this value is based on the [North American Vertical Datum of 1988](https://www.ngs.noaa.gov/datums/vertical/north-american-vertical-datum-1988.shtml). |
| GLOBALID | GLOBALID | A universally unique identifier ([uuid](https://en.wikipedia.org/wiki/Universally_unique_identifier)). | number | Not published in all datasets. |





