# LiDAR and Derived Products
Geometry Type: Point Cloud (LAZ), Raster (TIFF)<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/DEM.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Description** |Raster files and point clouds from 2010 and 2017 LiDAR capture covering New York City. The 2010 LiDAR includes one hydro-flattened digital elevation model (DEM). The 2017 LiDAR includes classed and unclassed point clouds in laz format, bare earth DEM, hydroflattened DEM, hydro-enforced DEM (filled and unfilled), highest hit, intensity imagery, 8-class land cover, and tree canopy change (2010-2017). For more information on specific derived products, see the Data Quality and Specifications section below. 
**Source(s)** |City of New York, University of Vermont Spatial Analysis Laboratory, Quantum Spatial Inc. 
**Publication Dates** |**Data**: 2017<br>**Last Update**: 2018<br>**Metadata**: 09/12/2018<br>**Update Frequency**: As needed
**Available Formats** |Point Cloud (LAS), Digital Elevation/Surface Models (GeoTIFF), Land Cover (GeoTIFF), Tree Canopy Change (Shapefile)
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html). 
**Access Rights** |Public
**Contact Information** |**Name**: DoITT GIS Unit<br>**Email**: gis-mgt@doitt.nyc.gov
**Links** |Direct download will be available via NYS (Available soon)<br>DoITT GIS Story Map
**Tags** |lidar, point cloud, dem, digital elevation model, foot, elevation, gis, doitt
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Vertical Datum** |NAVD88 Geoid 12B

| Year | Resolution | Dates of Capture | Sensor | Derived Products | 
|-- | --| -- | --| -- |
|2010|1 foot|Topographic: 4/14/2010 - 5/1/2010|Topographic: Leica ALS-50|Classified Point Clouds (LAS 1.2)<br>[Hydroflattened DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_2010_DEM.md)
|2017|1 foot|Topographic: 5/3/2017 - 5/17/2017 (1am - 6am) <br> Bathymetric: 7/4/2017 - 7/26/2017 (1am - 6am)|Topographic: Leica ALS80 <br> Bathymetric: Riegl VQ-880-G|[Topobathymetric Classified Point Cloud (LAS 1.4)](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_TopobathymetricClassifiedPointCloud.md)<br> [Base Bare Earth DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_BareEarthDigitalElevationModel.md)<br> [Hydroflattened DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_HydroflattenedDigitalElevationModel.md)<br> [Hydroenforced (Fill) DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_HydroEnforcedElevationModelFilled.md)<br>[Hydroenforced (Unfill) DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_HydroEnforcedElevationModelUnfilled.md)<br>[Highest Hit Model DSM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_HighestHitDigitalSurfaceModel.md)<br>[Intensity Imagery](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_IntensityImagery.md)<br>[8-Class Land Cover](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_LandCover.md)<br>[Tree Canopy Change (2010-2017)](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_TreeCanopyChange.md)<br>[Tidally Coordinated Shoreline](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_TidalShoreline.md)
