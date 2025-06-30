# Hydroflattened Digital Elevation Model
Geometry Type: Raster (TIF)<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/main/Images/Hydroflattened.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The hydroflattened digital elevation model can be used for creating contours and deriving elevation values. Water surface elevations are more accurate than in the Base bare earth. This model is also better than base bare earth for cartographic purposes.
**Description** |The bare earth digital elevation model (DEM) represents the earth's surface with all vegetation and anthropogenic features removed. It is derived from Green and NIR LiDAR data using TIN processing of the ground and bathymetric bottom point returns. Green LiDAR was used within the water's edge breakline for data splicing shape (provided as another deliverable) only and NIR LiDAR was used everywhere outside of this shape. Within the NIR-only portion of the AOI all rivers greater than 20 feet in width and lakes at least 0.25 acres in size have been flattened to consistent elevations. Some smaller streams and ponds were also flattened when deemed appropriate. Water boundary polygons were developed manually and by using automatic algorithms. Elevation values were then assigned to the water's edge from the LiDAR data creating 3D breaklines enforced during model creation to flatten water bodies. Some elevation values inside the NIR-only AOI have been interpolated across areas in the ground model where there is no elevation data (e.g. under dense vegetation). Within the green-only portion of the AOI (inside the low tide breaklines shape), the data has been clipped to avoid triangulation and false interpolation over areas identified as voids in the Bathymetric Coverage Polygon (provided as a separate deliverable).The horizontal datum for this dataset is NAD83, the vertical datum is NAVD88, Geoid 12B, and the data is projected in New York State Plane - Long Island. Units are in US Survey Feet. Quantum Spatial collected the New York City LiDAR data for The City of New York between 05/03/17 and 07/26/17.
**Source(s)** |City of New York, Quantum Spatial Inc. 
**Publication Dates** |**Data**: 2017<br>**Last Update**: 2018<br>**Metadata**: 09/12/2018<br>**Update Frequency**: As needed. This dataset was created as part of the 2017 LiDAR update
**Available Formats** |Topographic Mosaic<br>Topographic Tiled<br>Bathymetric Mosaic<br>Bathymetric Tiled<br>Topobathymetric Mosaic<br>Topobathymetric Tiled
**Use Limitations** |
**Access Rights** |Public
**Links** |[Digital Elevation and Surface Models](https://data.cityofnewyork.us/City-Government/Topobathymetric-LiDAR-Data-2017-/7sc8-jtbz/about_data)
**Tags** |LiDAR, Light Detection and Ranging, elevation data, topography, bare earth, hydro-flattened, breaklines, DEM, digital elevation model, New York City, New York, NYC, Manhattan, Brooklyn, Queens, The Bronx, Staten Island
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |1 foot
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |Topographic: 05/03/2017 - 05/17/2017<br>Bathymetric: 07/04/2017 - 07/26/2017
**Capture and Update Notes** |In some areas of heavy vegetation or forest cover, there may be relatively few ground points in the LiDAR data. TINing the points produces large triangles and hence the elevations may be less accurate within such areas. Elevation values for open water surfaces are derived from waters edge breaklines. Triangles were created across water surfaces by interpolating from the nearest breakline elevation points. Due to some very large buildings within the city, there are very large triangles/interpolation throughout. Mosaicking lines and "cross hairs" may be seen in the middle of some interpolation. This is normal and will not affect the quality of the data. Wooden boardwalks and concrete boardwalks which are known to be on pylons and where separation is clearly visible, were removed from the bare earth models. In some areas of the dataset, the DEM goes from being hydroflattened to being bathymetric bottom data. This happens where the "Waters_Edge_for_Data_Splicing" shape cuts through a coastline or long stream/river. For ponds and lakes that cross this boundary, the data has been hydroflattened within the shape while bathymetric data still exists within the LiDAR point cloud.
