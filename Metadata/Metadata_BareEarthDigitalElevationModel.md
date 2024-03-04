# Bare Earth Digital Elevation Model
Geometry Type: Raster (TIF)<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/main/Images/BaseBareEarth.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The base bare earth digital elevation model can be used for creating contours and deriving elevation values.
**Description** |The clipped bare earth digital elevation model (DEM) represents the earth's surface with all vegetation and anthropogenic features removed. It is derived from Green and NIR LiDAR data using TIN processing of the ground and bathymetric bottom point returns. Green LiDAR was used within the water's edge breakline for data splicing shape (provided as another deliverable) only and NIR LiDAR was used everywhere outside of this shape. This version of topobathymetric models has been clipped to avoid triangulation and false interpolation over areas identified as voids in the Bathymetric Coverage Polygon (provided as a separate deliverable).
**Source(s)** |City of New York, Quantum Spatial Inc. 
**Publication Dates** |**Data**: 2017<br>**Last Update**: 2018<br>**Metadata**: 09/12/2018<br>**Update Frequency**: As needed. This dataset was created as part of the 2017 LiDAR update
**Available Formats** |Topographic Mosaic<br>Topographic Tiled<br>Bathymetric Mosaic<br>Bathymetric Tiled<br>Topobathymetric Mosaic<br>Topobathymetric Tiled<br>
**Use Limitations** | NA
**Access Rights** |Public
**Links** |Coming Soon
**Tags** |LiDAR, Light Detection and Ranging, elevation data, topography, bare earth, hydro-flattened, breaklines, DEM, digital elevation model, New York City, New York, NYC, Manhattan, Brooklyn, Queens, The Bronx, Staten Island
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Vertical Datum** | NAVD88, Geoid 12B
**Resolution** |1 foot
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |Topographic: 05/03/2017 - 05/17/2017<br>Bathymetric: 07/04/2017 - 07/26/2017
**Capture and Update Notes** |In some areas of heavy vegetation or forest cover, there may be relatively few ground points in the LiDAR data. TINing the points produces large triangles and hence the elevations may be less accurate within such areas. Elevation values for open water surfaces are derived from waters edge breaklines. Triangles were created across water surfaces by interpolating from the nearest breakline elevation points. Due to some very large buildings within the city, there are very large triangles/interpolation throughout. Mosaicking lines and "cross hairs" may be seen in the middle of some interpolation. This is normal and will not affect the quality of the data. Wooden boardwalks and concrete boardwalks which are known to be on pylons and where separation is clearly visible, were removed from the bare earth models. In some areas of the dataset, the DEM goes from being hydroflattened to being bathymetric bottom data. This happens where the "Waters_Edge_for_Data_Splicing" shape cuts through a coastline or long stream/river. For ponds and lakes that cross this boundary, the data has been hydroflattened within the shape while bathymetric data still exists within the LiDAR point cloud.

