# 3-D Building Model
Geometry Type: Multiple<br><br>![image](https://www.nyc.gov/assets/planning/images/content/pages/data-maps/open-data/dcp-nyc3d-model-header.jpg)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |3-D Building Models were developed to supplement the most recent [planimetric](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) update. Some examples of usage include wind or shadow simulations, urban design, and building volume determination.   <br><br> Examples of NYC 3-D Building Model usage include: <br>     [CESIUM (Open Source 3D rendering library)](https://cesiumjs.org/NewYork/index.html?view=-74.01881302800248%2C40.69114333714821%2C753.2406554180401%2C21.27879878293835%2C-21.343905508724625%2C0.0716951918898415)<br>     [NY Times Shadow Study](http://www.nytimes.com/interactive/2016/12/21/upshot/Mapping-the-Shadows-of-New-York-City.html)
**Description** |3-D Building Models representing every NYC building present in the 2014 aerial survey. Models are based on a hybrid of the CItyGML Level of Detail (LOD) 1 (simple/prismatic buildings with flat roof detail) and LOD 2 (includes roof structure details) with approximately 100 iconic buildings modeled to LOD 2.  Highlights of the model include the differentiation of building components including roof, facades, and ground plane. 
**Source(s)** |Office of Technology and Innovation (OTI)
**Publication Dates** |**Data**: 04/18/2016<br>**Last Update**: 04/18/2016<br>**Metadata**: 12/28/2016<br>**Update Frequency**: The 3-D model was a one-time capture. Updates and extensions may be considered in the future. 
**Available Formats** |3-D Model data is available in the following formats: <br>     [CityGML](http://maps.nyc.gov/download/3dmodel/DA_WISE_GML.zip) : 894 MB<br>     [Multipatch (ESRI)](http://maps.nyc.gov/download/3dmodel/DA_WISE_Multipatch.zip) : 251 MB<br>     [DGN (Microstation)](http://maps.nyc.gov/download/3dmodel/DA_Wise_DGN.zip) : 744 MB
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](https://opendata.cityofnewyork.us/overview/#termsofuse)
**Access Rights** |Public
**Links** |https://data.cityofnewyork.us/City-Government/3-D-Building-Model/tnru-abg2
**Tags** |oti, doitt, gis, 3d, buildings, model
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |ASPRS CLASS 1.5 for 1"=100' scale maps
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |Data is based on buildings present in 2014 aerial survey.
**Positional Accuracy** |3-D models are based on the planimetrics building footprint feature class. The horizontal accuracy (XY) of all planimetric feature classes captured is such that 95% of features are within (plus/minus) 1.25 ft of the actual horizontal location. The vertical accuracy (Z) of all planimetric feature classes with elevation values is such that 95% of features captured are within (plus/minus) 1.6 ft of the actual elevation.
**Features Captured** |Permanent structures (e.g. stairwells, towers, etc) with lengths greater than 10' on a side or minimum 100 sq. ft. were captured. Features that are less than 10' but also align with the building planimetric outline are also included. 
**Features Excluded** |For LOD 1.5 buildings, domes and pitched roofs are not rendered.  All roof appendages, such as chimneys, parapets, spindles, and antenna are also not included. <br><br> For buildings with complex or multiple roof structures, a generalized collection method was used. Small permanent structures (e.g. small towers, elevator shaft, stairs) with less than 10' on a side were not captured. 
**Capture and Update Notes** |3-D building models were created by stereo compilation with BAE Systems' SocetSET GXP/Hexagon SSK software. Models are based on 2014 aerial photos and the [building footprints](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md#building-footprint) feature class from the [planimetric](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) database. Using the Open Geospatial Consortium's [CityGML](http://www.opengeospatial.org/standards/citygml) standards as the basis, the model was developed to a hybrid specification combining elements from Level of Detail (LOD) 1 and 2. When possible, the elevation attributes (ground elevation and roof height) from the building footprint feature class were used for building base and top data collection to ensure vertical consistency. Since roof elevations from the building feature class are based on the highest point of the roof, there are some differences in elevation for the 3D roof infrastructure that is modeled.<br><br>Once building roof polygons were created, a [digital elevation model (DEM)](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_DigitalElevationModel.md) was used as a ground lattice in conjunction with building base elevation to create a solid model of the buildings. The model was then populated with projection parameters.  For LOD 1.5 features, multiple roofs less than 8ft difference were considered as one roof outline and elevation points were placed at the highest point within the roof. For LOD 2 all ridges, dbomes and partitions were captured and assigned elevations with microstation tools. <br><br>Approximately 100 iconic buildings were created in LOD 2. <br><br>Building data was then converted from DGN/ESRI multipatch file geodatabase formats to CityGML using Safe Software's Feature Manipulation Engine (FME). <br><br> Examples of LOD 1.5 and LOD 2 buildings can be seen in the images below. <br> ![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/LOD1.5.png)<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/LOD2.png)<br>The model was a one-time capture. If the model is useful, future updates and extensions will be considered. 
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| BIN | Building identification number. Assigned by City Planning | numeric | No
| DOITT_ID | Unique identifier assigned by OTI (formerly DOITT).  | numeric | No
| SOURCE_ID |  | numeric | No
