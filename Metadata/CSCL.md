# CSCL


Geometry Type: point, line, polygon<br><br>![image](../Images/CSCL.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |CSCL (Citywide Street Centerline) is a Geodatabase managed by the Department of City Planning (DCP) and the Office of Technology and Innovation (OTI). The CSCL database was developed subsequent to 9/11 to ensure that all the NYC public safety agencies were working with GIS data from a common source. CSCL data feeds the NYPD 911 call-takers maps as well as each of the unique dispatch systems used by NYPD, FDNY, and FDNY EMS. It also supplies city agencies and the public with an authoritative source for a variety of other GIS data. CSCL is used to produce the Dept. of City Planning’s Geosupport software, a geocoding system widely used by city agencies and the public.
**Description** |CSCL is governed by 7 city agencies: DCP, OTI, NYPD, FDNY, OEM, DOT, and DEP. CSCL centrally maintains database of street, address, common place, and additional location data to support public safety dispatching, serving as the authoritative source for New York City’s geographic data. The data is edited on a daily basis and updates are synchronized nightly to NYPD, FDNY, DOT, DSNY, OEM and OTI-PSGIS. The CSCL database contains 72 feature classes, 38 tables and 46 relationships that are described below.
**Publication Dates** |**Last Update**: Weekly<br>**Metadata**: 12/11/2024<br>**Update Frequency**: Features are updated daily by OTI staff and released publicly on [NYCMaps](https://nycmaps-nyc.hub.arcgis.com/). 
**Available Formats** | (zipped) ESRI File Geodatabase 
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html)
**Access Rights** |Public
**Links** |https://nyc.maps.arcgis.com/home/item.html?id=113249f31f994dde836f3617c9bca1e3
**Tags** |CSCL
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot ([epsg:2263](https://spatialreference.org/ref/epsg/2263/)); Vertical Datum NAVD 1988
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Positional Accuracy** |Estimated positional accuracy for photogrammetrically updated features (those with GEOM_SOURCE = Photogrammetric) is +/- 2 feet and meets ASPRS Class 1 horizontal mapping standards and ASPRS vertical Class 2 accuracy specifications.  The mapping standards deal with Root Mean Square (RMS) calculations that states if a random number of clearly identifiable surveyed ground control points throughout the project were compared to the mapped features, the RMS of the points would not exceed 2'. In layman's terms,  95% of the data is accurate to +/- 2'.<br>Features with GEOM_SOURCE = Other (Manual) are captured by heads-up digitizing using the most current orthophotography available. These will be somewhat less accurate than the photogrammetrically updated features. 
**Features Captured** |All buildings >400 sq. feet and taller than 12 feet.  We also add other buildings with Building Identification Numbers (BINs) maintained by city agencies. <br>In rare cases where we have no visual or plan information to digitize a footprint we use a small triangle as a placeholder. These features are flagged as FEATURE_CODE = Placeholder. In cases where there is no BIN for a feature we will use a dummy BIN (1000000, 2000000, etc. for each of the boroughs) until we can determine an actual BIN for the structure.
**Features Excluded** |Interior divisions.<br>Temporary trailers or tents.  <br>Movable jet bridges for access to aircraft.<br>Awnings, scaffolds, or sidewalk sheds.<br>Small tool or storage sheds in backyards which have no visible car access. 
**Capture and Update Notes** |Guidelines for Photogrammetric Update: Use parcel data and BIN as guidance for collection.  Where the parcel data indicates that a building should be two or more geometries AND there is NO physical indication, split the building using the parcel lines.   Where the parcel data indicates that a building should be two or more geometries AND there is a physical indication, split the building using the physical indications.  In cases where geometry previously existed in the legacy data, populate all resulting geometries with the original BIN (BINs will be duplicated in these cases).<br>Use Parcel layer to place garages within parcel or at parcel boundary  check for special cases where parcel boundary clearly crosses garage.  In these cases, either split the garage using physical features, or use the property line where there is no distinguishing physical feature. <br><br> For more information on capture and update of the Building Footprints dataset, see [Capture Rules](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) <br><br> Guidelines for Manual Update: Features captured by manual update are digitized from the most recent imagery available. In cases where no imagery is available, features are digitized using plan diagrams available from the Department of Buildings. In cases where there is no imagery or plan source available, add a small placeholder triangle and set feature code to Placeholder. Use Eagleview or Cyclomedia for ground elevation. Take roof heights from Department of Buildings plan diagrams if available or measure from controlled terrestrial image sources like Cyclomedia. In the past when no source was available, roof height was left zero or NULL. 
## 3. Attribute Information 
---------------------------------------------
| Attribute | Shapefile Attribute | Description | Field Type | Notes | 
|------------ | ------------- | -------- | ----------- | ----------|
| OBJECTID | OBJECTID | Synthetic key populated by internal software | number | Use DOITT_ID instead for a consistent key identifying a building. |
| BASE_BBL | BASE_BBL | Borough, block, and lot number for the tax lot that the footprint is physically located within.  | text | Field type is text but only numbers are allowed. <br> Buildings occasionally will be associated with lots that they are not physically located within due to temporary synchronziation issues between city agencies.  Some buildings without property taxes will also fall outside of their identified tax lot |
| BIN | BIN | Building Identification Number. A number assigned by City Planning and used by Dept. of Buildings to reference information pertaining to an individual building. The first digit is a borough code (1 = Manhattan, 2 = The Bronx, 3 = Brooklyn, 4 = Queens, 5 = Staten Island). The remaining 6 digits are unique for buildings within that borough. In some cases where these 6 digits are all zeros (e.g. 1000000, 2000000, etc.) the BIN is unassigned or unknown. | number | Due to "million BINs" this identifier is not unique |
| CONSTRUCTION_YEAR | CNSTRCT_YR | The year construction of the building was completed. | number | Originally this column was populated using the Department of Finance Real Property Assessment Database (RPAD). After 2017 we used imagery and city information systems to populate this value in real time.  Buildings where construction year is zero or NULL this information was not available. |
| DOITT_ID | DOITT_ID | Consistent unique identifier assigned by OTI (formerly DOITT).  | number | |
| FEATURE_CODE | FEAT_CODE | Type of Building. List of values:<br>1000 = Parking<br>1001 = Gas Station Canopy<br>1002 = Storage Tank<br>1003 = Placeholder (triangle for permitted bldg)<br>1004 = Auxiliary Structure (non-addressable, not garage)<br>1005 = Temporary Structure (e.g. construction trailer)<br>1006 = Cantilevered Building<br>2100 = Building<br>2110 = Skybridge<br>5100 = Building Under Construction<br>5110 = Garage<br> | number | |
| GEOM_SOURCE | GEOM_SOURCE | Indicates the reference source used to add or update the feature. Photogrammetric means the feature was added or updated using photogrammetric stereo-compilation methodology. This is the most accurate update method and should conform to the ASPRS accuracy standards. Other (Manual) means the feature was added or updated by heads-up digitizing from orthophotos or approximated from a plan drawing. These features will be generally be less accurate and may not conform to the ASPRS accuracy standards. | text | |
| GLOBALID | GLOBALID | A universally unique identifier ([uuid](https://en.wikipedia.org/wiki/Universally_unique_identifier)) | number | not published in all datasets |
| GROUND_ELEVATION | GROUNDELEV | Lowest Elevation at the building ground level. Calculated from LiDAR or photogrammetrically. | number | Accuracy varies but when collected photogrammetrically or from modern sources this value is based on the [North American Vertical Datumm of 1988](https://www.ngs.noaa.gov/datums/vertical/north-american-vertical-datum-1988.shtml) |
| HEIGHT_ROOF | HEIGHTROOF | The height of the roof above the ground elevation, not height above sea level.  | number | Records where this is zero or NULL mean that this information was not available. Sources include (1) Final as-built heights as shown in plan drawings posted on Department of Buildings BIS website (2) EagleView Oblique imagery, direct measurements taken on photogrammetrically controlled aerial imagery (3) Cyclomedia imagery, direct measurements were taken on photogrammetrically controlled terrestrial imagery (for buildings less than 60 feet tall, only) |
| LAST_EDITED_DATE | LSTMODDATE | Feature last modified date | date | |
| LAST_STATUS_TYPE | LSTSTATTYPE | Feature last status type (Demolition, Alteration, Geometry, Initialization, Correction, Marked for Construction, Marked For Demolition, Constructed) | text | |
| MAPPLUTO_BBL | MPLUTO_BBL | Borough, block, and lot number to be used for joining the building footprints data to DCP's MapPLUTO data, which aggregates data for condominium buildings using DOF's billing BBL. For non-condominium buildings the billing BBL is the same as the BASE_BBL. For condominium buildings the billing BBL may be the same for multiple buildings on different physical tax lots if they are part of the same billing unit for Department of Finance purposes. | text | Field type is text but only numbers are allowed |
| NAME | NAME | Building name (limited to commonly known names). This field has not been actively maintained since the original creation of this dataset. | text | |








