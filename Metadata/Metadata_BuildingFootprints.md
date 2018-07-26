# Building Footprints
Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Images/FeatureViews/Build_Foot.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |Building footprints represent the perimeter outline of each building. Divisions between adjoining buildings are determined by tax lot divisions. 
**Source(s)** |Current Imagery
**Publication Dates** |**Data**: 05/03/16<br>**Last Update**: 03/15/2017<br>**Metadata**: 12/22/2016<br>**Update Frequency**: Agency data is updated daily by Centerline Management Group (CMG). Public releases of this data are made monthly. 
**Available Formats** |Shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/Housing-Development/Building-Footprints/nqwf-w8eh)
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html)
**Access Rights** |Public
**Links** |https://data.cityofnewyork.us/Housing-Development/Building-Footprints/nqwf-w8eh
**Tags** |Buildings, Building footprint, BIN, Structure
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |Estimated positional accuracy: 95% of the data is accurate to +/- 2 feet. All the NYCMap data was aero triangulated and stereo-compiled to meet ASPRS Class 1 horizontal mapping standards and ASPRS vertical Class 2 accuracy specifications.  The mapping standards deal with Root Mean Square (RMS) calculations that states if a random number of clearly identifiable surveyed ground control points throughout the project were compared to the mapped features, the RMS of the points would not exceed 2'. In layman's terms,  95% of the data is accurate to +/- 2'.
**Features Captured** |Collect all buildings >400 sq. feet and taller than 12 feet.  Buildings with <12 feet height but with BIN should be captured.<br>Buildings with BIN but <400 sq. feet will be captured.<br>Buildings with flat roofs will be captured on roof outline, capturing the largest outline (excluding overhangs, awnings, construction features, etc.).<br>Buildings with pitched roofs will be captured on the building footprint.<br>Carports, when attached to main building, will be included in the outline.
**Features Excluded** |Do not collect interior divisions (use existing building layer and BIN as guide).<br>Do not collect temporary trailers, tents, or roofs at gas stations (over pumps). Do NOT collect roofs (overhang) to gas stations, unless connected to building.<br>Do NOT collect movable jet bridge for access to aircraft.<br>Do NOT collect awnings, scaffolds, or sidewalk sheds.<br>Do NOT collect small tool or storage sheds in backyards which have no visible car access.  In cases where there is no BIN for the garage, a dummy BIN (1000000, 2000000, etc. for each of the Boroughs, see LION manuals pdf) will be populated.
**Capture and Update Notes** |Use parcel data and BIN as guidance for collection.  Where the parcel data indicates that a building should be two or more geometries AND there is NO physical indication, split the building using the parcel lines.   Where the parcel data indicates that a building should be two or more geometries AND there is a physical indication, split the building using the physical indications.  In cases where geometry previously existed in the legacy data, populate all resulting geometries with the original BIN (BINs will be duplicated in these cases).<br>Use Parcel layer to place garages within parcel or at parcel boundary  check for special cases where parcel boundary clearly crosses garage.  In these cases, either split the garage using physical features, or use the property line where there is no distinguishing physical feature. <br><br> For more information on capture and update of the Building Footprints dataset, see (Capture Rules.) [https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md]
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| BBL | Borough block and lot number | text | No
| BIN | Building identification number. Assigned by City Planning | double | No
| NAME | Building name (limited to commonly known names) | text | No
| LSTMODDATE | Feature last modified date | date | No
| LSTSTATTYPE | Feature last status type (Demolition, Alteration, Geometry, Initialization, Correction, Marked for Construction, Marked For Demolition, Constructed) | text | No
| CNSTRCT_YR | The year construction of the building was completed. If the year of construction is an estimate, it is indicated in the "BuiltCode" field with an E code.<br>Source: Department of Finance  = Real Property Assessment Database (RPAD). | double | No
| DOITT_ID | Unique identifier assigned by DOITT.  | double | No
| HEIGHTROOF | Building Height is calculated as the difference from the building elevation from the Elevation point feature class and the elevation in the interpolated TIN model. This value then is the height of the roof above the ground elevation, NOT its height above sea level. | double | No
| FEAT_CODE | Type of Building. List of values:<br>2100 = Building<br>5100 = Building Under Construction<br>5110 = Garage<br>2110 = Skybridge | long | No
| GROUNDELEV | Lowest Elevation at the building ground level. Calculated from LiDAR or photogrammetrically. | double | No
