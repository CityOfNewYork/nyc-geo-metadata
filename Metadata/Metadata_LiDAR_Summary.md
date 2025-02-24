# LiDAR
Geometry Type: Point Cloud (LAZ), Raster (TIFF)<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/main/Images/DEM.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |
**Description** |Raster files and point clouds from 2010 and 2017 LiDAR capture covering New York City. The 2010 LiDAR includes one hydro-flattened digital elevation model (DEM). The 2017 LiDAR includes classed and unclassed point clouds in laz format, bare earth DEM, hydroflattened DEM, hydro-enforced DEM (filled and unfilled), highest hit, intensity imagery, 8-class land cover, and tree canopy change (2010-2017). 
**Source(s)** |City of New York, University of Vermont Spatial Analysis Laboratory, Quantum Spatial Inc. 
**Publication Dates** |**Data**: 2017<br>**Last Update**: 2018<br>**Metadata**: 01/28/2019<br>**Update Frequency**: As needed
**Available Formats** |Point Cloud (LAS), Raster (GeoTIFF)
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html). Access and use of this data set require the approval of the City of New York Department of Environmental Protection. The City of New York and the University of Vermont make no representations of any kind, including but not limited to the warranties of merchantability or fitness for a particular use, nor are any such warranties to be implied with respect to the data.
**Access Rights** |Public
**Contact Information** |**Name**: OTI GIS Unit<br>**Email**: gis-mgt@oti.nyc.gov
**Links** |Topobathymetric Point Cloud available via [New York State GIS Clearinghouse](https://orthos.dhses.ny.gov/?Extent=-9603624.133747088,4774299.7366908705,-7659066.134172721,5795498.434580554&Layers=07_meter_dem_index_usgs,1_meter_dem_index_fema,1_meter_dem_index_usgs,1_meter_dem_index_tidal_water,1_meter_dem_index_hydro_flattened,1_meter_dem_index_usda_utm18n,1_meter_dem_index_usda_utm17n,1_meter_dem_index_nys,2_meter_dem_index_ne_lidar,2_meter_dem_index_nys,2_meter_dem_index_fema,2_meter_dem_index_monroe_county,2_meter_dem_index_tompkins_county,2_meter_dem_index_erie_county&layerGroups=DEMIndexes,Orthoimagery&rightMenu=0)<br>Digital Elevation and Surface Models available via [New York State GIS Clearinghouse](https://gis.ny.gov/lidar)<br>[Land Cover](https://data.cityofnewyork.us/Environment/Land-Cover-Raster-Data-2017-6in-Resolution/he6d-2qns)<br>[Tree Canopy Change](https://data.cityofnewyork.us/Environment/Tree-Canopy-Change-2010-2017-/by9k-vhck)<br>[Tidally Coordinated Shoreline](https://data.cityofnewyork.us/Environment/Tidally-Coordinated-Shoreline/pawq-tjb4)<br>Intensity Imagery (coming soon)
**Tags** |lidar, point cloud, dem, digital elevation model, foot, elevation, gis, oti, doitt
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Vertical Datum** |NAVD88 Geoid 12B

 | Year | Resolution | Dates of Capture | Sensor | Derived Products | 
|-- | --| -- | --| -- |
|2010.0|1 foot|Topographic: 4/14/2010 - 5/1/2010|Topographic: Leica ALS-50|Classified Point Clouds (LAS 1.2)<br>[Hydroflattened DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_2010_DEM.md)
|2017.0|1 foot|Topographic: 5/3/2017 - 5/17/2017 (1am - 6am) <br> Bathymetric: 7/4/2017 - 7/26/2017 (1am - 6am)|Topographic: Leica ALS80 <br> Bathymetric: Riegl VQ-880-G|[Topobathymetric Classified Point Cloud (LAS 1.4)](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_TopobathymetricClassifiedPointCloud.md)<br> [Base Bare Earth DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_BareEarthDigitalElevationModel.md)<br> [Hydroflattened DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_HydroflattenedDigitalElevationModel.md)<br> [Hydroenforced (Fill) DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_HydroEnforcedElevationModelFilled.md)<br>[Hydroenforced (Unfill) DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_HydroEnforcedElevationModelUnfilled.md)<br>[Highest Hit Model DSM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_HighestHitDigitalSurfaceModel.md)<br>[Intensity Imagery](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_IntensityImagery.md)<br>[8-Class Land Cover](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_LandCover.md)<br>[Tree Canopy Change (2010-2017)](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_TreeCanopyChange.md)<br>[Tidally Coordinated Shoreline](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_TidalShoreline.md)
