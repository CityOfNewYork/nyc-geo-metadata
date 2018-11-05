# LiDAR
Geometry Type: Point Cloud (LAZ), Raster (TIFF)<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/DEM.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |
**Description** |Raster files and point clouds from 2010 and 2017 LiDAR capture covering New York City. The 2010 LiDAR includes one hydro-flattened digital elevation model (DEM). The 2017 LiDAR includes classed and unclassed point clouds in laz format, bare earth DEM, hydroflattened DEM, hydro-enforced DEM (filled and unfilled), highest hit, intensity imagery, 8-class land cover, and tree canopy change (2010-2017). 
**Source(s)** |City of New York, University of Vermont Spatial Analysis Laboratory, Quantum Spatial Inc. 
**Publication Dates** |**Data**: 2017<br>**Last Update**: 2018<br>**Metadata**: 09/12/2018<br>**Update Frequency**: As needed
**Available Formats** |Point Cloud (LAS), Raster (GeoTIFF)
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html). Access and use of this data set require the approval of the City of New York Department of Environmental Protection. The City of New York and the University of Vermont make no representations of any kind, including but not limited to the warranties of merchantability or fitness for a particular use, nor are any such warranties to be implied with respect to the data.
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
| Year | Resolution | Sensor | Derived Products | Details | Accuracy Summary | More Information | 
|------------ | ------------- | -------- | ----------- | ---------- | ----------- | ----------|
2010|1 foot	|Topographic: 4/14/2010 - 5/1/2010|	Topographic: Leica ALS-50	|Classified Point Clouds (LAS 1.2)<br>Hydroflattened DEM <br> 7 - Class Land Cover	|The 2010 LiDAR  includes topographic LiDAR capture for New York City. |	The average vertical accuracy (RMSE) for this dataset was 0.245 ft (0.0748). Non-vegetated Vertical Accuracy (NVA) for this dataset is 0.312 ft (0.095 m).	|[Hydroflattened DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_2010_DEM.md)
2017|	1 foot	|Topographic: 5/3/2017 - 5/17/2017 (1am - 6am) <br> Bathymetric: 7/4/2017 - 7/26/2017 (1am - 6am)|	Topographic: Leica ALS80 <br> Bathymetric: Riegl VQ-880-G	|Classified Point Cloud (LAS 1.4)<br>Base Bare Earth DEM<br> Hydroflattened DEM<br> Hydroenforced (Fill) DEM<br>Hydroenforced (Unfill) DEM<br>Highest Hit Model DSM<br>Intensity Imagery<br>8-Class Land Cover<br>Tree Canopy Change (2010-2017)<br>Shoreline	|The 2017 LiDAR  includes topographic and bathymetric LiDAR capture for New York City. 	|The Non-vegetated Vertical Accuracy (NVA) of this dataset, tested at 95% confidence level is 0.242 ft (0.074 m). <br>
The Vegetated Vertical Accuracy (VVA) of this dataset, evaluated at the 95th percentile is 0.517 ft (0.158 m). <br>
Vegetated Vertical Accuracy was assessed using 18 VVA check points. These check points were not used in the calibration or post processing of the LiDAR point cloud data.
Vertical accuracy was also assessed using ground control points that were used in the calibration and post processing of the LiDAR point cloud as they still serve as a good indication of the overall accuracy of the LiDAR dataset. The Root Mean Square Error (RMSE) of the vertical accuracy of the LiDAR dataset as compared to ground control points is 0.128 ft (0.039 m). Please see the LiDAR data report for a discussion of the statistics related to this dataset. |[Base Bare Earth DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_BaseBareEarthDigitalElevationModel.md)<br> [Hydroflattened DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_HydroflattenedDigitalElevationModel.md)<br> [Hydroenforced (Fill) DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_HydroEnforcedElevationModelFilled.md)<br>[Hydroenforced (Unfill) DEM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_HydroEnforcedElevationModelUnfilled.md)<br>[Highest Hit Model DSM](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_HighestHitDigitalSurfaceModel.md)<br>[Intensity Imagery](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_IntensityImagery.md)<br>[8-Class Land Cover](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_LandCover.md)<br>[Tree Canopy Change (2010-2017)](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_TreeCanopyChange.md)