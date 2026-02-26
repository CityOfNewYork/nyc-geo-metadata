# LiDAR
Geometry Type: Point Cloud (LAZ), Raster (TIFF)<br><br>
<img src="https://github.com/CityOfNewYork/nyc-geo-metadata/blob/main/Images/DEM.PNG" width="400">


### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)

## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Description** |Raster files and point clouds from 2010 and 2017 LiDAR capture covering New York City. The 2010 LiDAR includes one hydro-flattened digital elevation model (DEM). The 2017 LiDAR includes classed and unclassed point clouds in laz format, bare earth DEM, hydroflattened DEM, hydro-enforced DEM (filled and unfilled), highest hit, intensity imagery, 8-class land cover, and tree canopy change (2010-2017). 
**Source(s)** |City of New York, University of Vermont Spatial Analysis Laboratory, Quantum Spatial Inc. 
**Publication Dates** |**Data**: 2017, 2010<br>**Metadata**: 02/28/2019
**Available Formats** |Point Cloud (LAS), Raster (GeoTIFF)
**Access Rights** |Public
**Contact Information** |**Name**: OTI GIS Unit<br>**Email**: gis-mgt@oti.nyc.gov
**Links to Data and Products** |See "Derived Products" links below
**Tags** |lidar, point cloud, dem, digital elevation model, foot, elevation, gis, oti, doitt
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Vertical Datum** |NAVD88 Geoid 12B

 | Year | Resolution | Dates of Capture | Sensor | Derived Products | 
|-- | --| -- | --| -- |
|2010|1 foot|Topographic: 4/14/2010 - 5/1/2010|Topographic: Leica ALS-50|Classified Point Clouds (LAS 1.2)<br>[Hydroflattened DEM](./Metadata_2010_DEM.md)
|2017|1 foot|Topographic: 5/3/2017 - 5/17/2017 (1am - 6am) <br> Bathymetric: 7/4/2017 - 7/26/2017 (1am - 6am)|Topographic: Leica ALS80 <br> Bathymetric: Riegl VQ-880-G|[Topobathymetric Classified Point Cloud (LAS 1.4)](./Metadata_TopobathymetricClassifiedPointCloud.md)<br> [Base Bare Earth DEM](./Metadata_BareEarthDigitalElevationModel.md)<br> [Hydroflattened DEM](./Metadata_HydroflattenedDigitalElevationModel.md)<br> [Hydroenforced (Fill) DEM](./Metadata_HydroEnforcedElevationModelFilled.md)<br>[Hydroenforced (Unfill) DEM](./Metadata_HydroEnforcedElevationModelUnfilled.md)<br>[Highest Hit Model DSM](./Metadata_HighestHitDigitalSurfaceModel.md)<br>[8-Class Land Cover](./Metadata_LandCover.md)<br>[Tree Canopy Change (2010-2017)](./Metadata_TreeCanopyChange.md)<br>[Tidally Coordinated Shoreline](./Metadata_TidalShoreline.md)


