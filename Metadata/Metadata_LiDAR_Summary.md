# LiDAR
Geometry Type: Point Cloud (LAZ), Raster (TIFF)<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/main/Images/DEM.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Description** |Raster files and point clouds from 2010 and 2017 LiDAR capture covering New York City. The 2010 LiDAR includes one hydro-flattened digital elevation model (DEM). The 2017 LiDAR includes classed and unclassed point clouds in laz format, bare earth DEM, hydroflattened DEM, hydro-enforced DEM (filled and unfilled), highest hit, intensity imagery, 8-class land cover, and tree canopy change (2010-2017). 
**Source(s)** |City of New York, University of Vermont Spatial Analysis Laboratory, Quantum Spatial Inc. 
**Publication Dates** |**Data**: 2017<br>**Last Update**: 2018<br>**Metadata**: 01/28/2019<br>**Update Frequency**: As needed
**Available Formats** |Point Cloud (LAS), Raster (GeoTIFF)
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html). Access and use of this data set require the approval of the City of New York Department of Environmental Protection. The City of New York and the University of Vermont make no representations of any kind, including but not limited to the warranties of merchantability or fitness for a particular use, nor are any such warranties to be implied with respect to the data.
**Access Rights** |Public
**Contact Information** |**Name**: OTI GIS Unit<br>**Email**: gis-mgt@oti.nyc.gov
**Links** |[Topobathymetric Point Cloud](https://data.cityofnewyork.us/City-Government/Topobathymetric-LiDAR-Data-2017-/7sc8-jtbz/about_data)<br>[Digital Elevation and Surface Models](https://data.cityofnewyork.us/City-Government/Topobathymetric-LiDAR-Data-2017-/7sc8-jtbz/about_data)<br>[Land Cover](https://data.cityofnewyork.us/Environment/Land-Cover-Raster-Data-2017-6in-Resolution/he6d-2qns)<br>[Tree Canopy Change](https://data.cityofnewyork.us/Environment/Tree-Canopy-Change-2010-2017-/by9k-vhck)<br>[Tidally Coordinated Shoreline](https://data.cityofnewyork.us/Environment/Tidally-Coordinated-Shoreline/pawq-tjb4)
**Tags** |lidar, point cloud, dem, digital elevation model, foot, elevation, gis, oti, doitt
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Vertical Datum** |NAVD88 Geoid 12B

 | Year | Resolution | Dates of Capture | Sensor | Derived Products | 
|-- | --| -- | --| -- |
|2010.0|1 foot|Topographic: 4/14/2010 - 5/1/2010|Topographic: Leica ALS-50|Classified Point Clouds (LAS 1.2)<br>[Hydroflattened DEM](./Metadata_2010_DEM.md)
|2017.0|1 foot|Topographic: 5/3/2017 - 5/17/2017 (1am - 6am) <br> Bathymetric: 7/4/2017 - 7/26/2017 (1am - 6am)|Topographic: Leica ALS80 <br> Bathymetric: Riegl VQ-880-G|[Topobathymetric Classified Point Cloud (LAS 1.4)](./Metadata_TopobathymetricClassifiedPointCloud.md)<br> [Base Bare Earth DEM](./Metadata_BareEarthDigitalElevationModel.md)<br> [Hydroflattened DEM](./Metadata_HydroflattenedDigitalElevationModel.md)<br> [Hydroenforced (Fill) DEM](./Metadata_HydroEnforcedElevationModelFilled.md)<br>[Hydroenforced (Unfill) DEM](./Metadata_HydroEnforcedElevationModelUnfilled.md)<br>[Highest Hit Model DSM](./Metadata_HighestHitDigitalSurfaceModel.md)<br>[8-Class Land Cover](./Metadata_LandCover.md)<br>[Tree Canopy Change (2010-2017)](./Metadata_TreeCanopyChange.md)<br>[Tidally Coordinated Shoreline](./Metadata_TidalShoreline.md)
