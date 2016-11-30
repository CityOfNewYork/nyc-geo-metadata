# BUILDING FOOTPRINT
building_footprints

![image](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Images/FeatureViews/Build_Foot.png)

Geometry Type: Polygon
### Table of Contents
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Organization**](#data-quality)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#attribute-information)

## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** | The purpose of this document is to define the capture rules for building footprints as part of the planimetric project. 
**Description** | Shapefile of footprint outlines of buildings in New York City. The building footprint shapefile includes the following subtypes:<br> • Building<br> • Sky Bridge<br> • Building Under Construction<br> • Garage
**Source(s)** |	Planimetric data, building footprint database
**Publication  Dates** | **Data**: 2014 (see Capture notes). <br> **Last Update**: 06/02/2016 <br> **Metadata**: 01/01/2016 <br> **Update Frequency**: As needed
**Spatial Coverage** | New York City, NY
**Temporal Coverage** | Database is current as of 2016. Previous downloads of the data are available here:<br> • 2000 Planimetric Delivery, 1996 Imagery (download)<br> • 2004 Planimetric Delivery, 2000/2001 Imagery (download)<br> • 2008 Planimetric Delivery, 2006 Imagery (download)<br> • 2012 Planimetric Delivery, 2010 Imagery (download)<br> • 2016 Planimetric Delivery, 2014 Imagery (download)
**Available Formats** | .shp. Additional data formats are available for download on the OpenData Portal.
**Use Limitations** | NA
**Access Rights** | Public
**Contact Information** | **Name**: Department of Information Technology and Telecommunication (DOITT), GIS <br>**Phone**: ###-###-#### <br> **Email**: gis-group@doitt.nyc.gov
**Links** | The building footprint data layer is available for download on NYC Open Data Portal -- https://data.cityofnewyork.us/Housing-Development/Building-Footprints
**Tags** | planimetrics, building footprint, buildings, sky bridge, garage, building under construction
	
## 2. Data Quality and Organization
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** | New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** | 1”=100’	
**Features Captured** |	All buildings with well-defined walls and roofs that are >400 square feet and taller than 12 feet were captured. Buildings with <12 feet height but with BIN were captured. Buildings with BIN but <400 square feet were also captured.<br><br>**Building**<br>All buildings with well-defined walls and roofs that are >400 square feet and taller than 12 feet were captured.<br>Buildings with <12 feet height but with BIN were captured.<br>Buildings with BIN but <400 square feet were also captured.**Sky Bridge**<br>Elevated walkways that connect buildings were captured as separate building polygons and coded as “Skybridge”.**Building U/C (Building under Construction**<br>Buildings that were under construction in the imagery and had outside walls that clearly indicated the shape of the building were captured. An “million" BIN was assigned to buildings (under construction) not existing in the source database. For more information regarding BIN, see Building Footprint Attributes.**Garage**<br>All garages were captured, regardless of size. To be considered a garage, the structure must have a driveway (paved or unpaved) for road access, and be able to store one or more cars.
**Features Excluded** | The following features were not captured:• temporary trailers, tents, or roofs at gas stations (over pumps).• roofs (overhang) to gas stations, unless connected to building.• movable jet bridge for access to aircraft.• awnings, scaffolds, or sidewalk sheds.
**Positional Accuracy** | Planimetrics are developed to meet American Society for Photogrammetry and Remote Sensing (ASPRS) Class 1 (one) horizontal mapping standards and ASPRS vertical Class 2 (two) accuracy specifications.
**Capture and Update Notes** | **Buildings**<br>Buildings with flat roofs were captured on roof outline, capturing the largest outline (excluding overhangs, awnings, construction features, etc.).Buildings with pitched roofs were captured on the building footprint. <br>Carports, when attached to main building, were included in the outline. Interior divisions within buildings were not captured (used existing building layer and BIN as guide). <br>Parcel data and BIN was used as guidance for collection. Where the parcel data indicated that a building should be two or more geometries AND there was NO physical indication, the building was split using the parcel lines. Where the parcel data indicated that a building should be two or more geometries AND there was a physical indication, the building was split using the physical indications. <br>If an existing building was split into several new buildings, the original BIN was retained in only one of the new buildings (ideally the largest) and the new buildings were assigned an "million" BIN (as a placeholder). BINs can not be duplicated. Building Footprints abutting one another on a single tax lot, but each having a unique BIN, were flagged and verified during review.If a building was demolished (i.e., as evidenced in the imagery), the BIN was also deleted and was not used for any new building geometry.Small triangles denote a permit is out to construct a new building at the location. These small triangles were added by DoITT building editors. These triangles should be removed when new buildings are added. Therefore if a new building was constructed in the new orthos, the building was captured, the attributes from triangle to building were transferred to the new building, and the triangle was deleted. If no new building was visible on the orthos, the triangles were left in the data. An “million" BIN was assigned to buildings not existing in the source database.For more information regarding BIN, see Building Footprint Attributes.


## 3. Attribute Information
-----------------------------------
Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes
------------ | ------------- | -------- | ----------- | ----------
SOURCE_ID | Unique feature Identification Number. | Integer | Y | NA
FEATURE_CODE | Indicates the type of feature. | Integer | Y | NA
SUB_FEATURE_CODE | (where applicable) indicates a subset of features within a given “Feature_Code” set. Subtypes have the following feature codes:<br> • Building = 2100<br> • Sky Bridge = 2110<br> • Building Under Construction = 5100<br> • Garage = 5110 | Integer | Y | NA
STATUS | Unique feature Identification Number. | Integer | Y | NA
HEIGHT_ROOF | Building roof height was calculated as the difference between ground elevation of the building and the roof elevation value. The roof elevation is the highest point of the roof itself (see BUILDING ELEVATION in the ELEVATION Feature Class). See Building Footprint Diagrams below for additional details. | Integer | Y | NA
GROUND_ELEVATION | Represents an interpolated elevation value at the centroid (center point) of the building. The process for capturing this is as follows:1. A bare-earth surface is generated from the 2010 LiDAR by first removing any points that fall within a building polygon. These points are removed to eliminate any data anomalies (e.g., points captured at the roof level). A Digital Terrain Model (DTM) is then generated from the remaining points by interpolating the elevations around the building edges to develop a continuous surface.2. Building centroids (i.e., the center point within each building) are then draped over the DTM generated from step 1. The bare-earth elevation value at that building centroid is then transferred to the ground elevation attribute of the building footprint. The purpose is to determine a single elevation value that is representative of the elevation values surrounding each building. | Integer | Y | NA
NAME | Name of building. | Text | Y | NA
BIN | A Building Identification Number (BIN) is a unique identifier assigned by the Department of City Planning (DCP) for buildings in Geosupport. DoITT inserts assigned BINs into their respective footprints on an ongoing basis through interagency coordination. For cases where a BIN has not been assigned or cannot be determined, a "million” BIN is inserted as follows:• 1000000 for Manhattan,• 2000000 for Bronx,• 3000000 for Brooklyn,• 4000000 for Queens,• 5000000 for Staten Island | Integer | Y | NA
CONSTURCTION_YEAR | Derived from PLUTO. The year construction of the building was completed. See "BuiltCode" field for details on accuracy. | Integer | Y | NA
GEOM_SOURCE | Unique feature Identification Number. | Integer | Y | NA
LAST_MODIFY_BY | Unique feature Identification Number. | Integer | Y | NA
LAST_MODIFY_DATE | Date that a building feature's geometry or attributes was last modified. | Date | Y | NA
LAST_STATUS_TYPE | The status of a building - "Constructed", "Marked for Construction", or "Marked for Demolition". | Text | Y | NA
DOITT_ID | Unique numeric ID assigned by DoITT. | Integer | Y | NA
LAST_STATUS_DATE | Most recent date that a building status was changed. | Date | Y | NA
HEIGHT_ROOF | Building Height is calculated as the difference from the building elevation from the Elevation point feature class and the elevation in the interpolated TIN model. This value then is the height of the roof above the ground elevation, NOT its height above sea level. | Integer | Y | NA
DOB_JOB_NUM | Job number from DOB_JOB table obtained from milestone reports. | Integer | Y | NA
NUM_FLOORS | Derived from PLUTO. Indicates the number of full and partial stories starting from the ground floor. For cases where a lot has more than one building, the number of stories in the primary building on the tax lot is applied to all buildings on the lot. | Integer | Y | NA
BUILT_CODE | Derived from PLUTO. A code indicating whether the year the building was built (CONSTRUCTION_YEAR) is an estimate. E = Estimate; Blank = Year Built is not an Estimate | Integer | Y | NA
