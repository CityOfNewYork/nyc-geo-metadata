# LiDAR
Geometry Type: Point Cloud (LAZ), Raster (TIFF)<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/LiDAR.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
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

 | Year | Resolution | Coverage | Dates of Capture | Product Details | Color Infrared | 
| -- | -- | -- | -- | -- | -- |
|1924|Unknown|New York City|Unknown|Acquired from the Department of City Planning. Manually georeferenced using visible locations between the 1951 images and current orthophotography.|No
|1951|Unknown|New York City|Unknown|Acquired from the Department of Records Municipal Archives. Manually georeferenced using visible locations between the 1951 images and current orthophotography.|No
|1996|1'|New York City|April: 1" = 800', entire city <br> June: 1"=1000', Manhattan||No
|2001|6''|Partial (Manhattan, Staten Island)|April 14: 1”=800’ – used for plan/topo update in Manhattan and Staten Island<br>July 3, & July 21:  1”=1000'– used for Manhattan orthos||No
|2002|6''|Partial (Bronx, Brooklyn, Queens)|April 4: 1"=800'  – used for plan/topo update for Bronx/Brooklyn/Queens||No
|2004|6''|New York City|April 19-20: Staten Island<br>April 29: Manhattan (2/3)<br>April 30: Manhattan (1/3)<br>April 24: Bronx, Brooklyn, Queens (2/3)<br>April 25: Bronx, Brooklyn, Queens (2/3)<br>May 4: Bronx, Brooklyn, Queens – re-flight of rejected flight strips|Selective true orthoimagery. Manhattan full true orthoimagery;  Bronx, Brooklyn, Queens, Staten Island true orthos for buildings greater than six stories.|No
|2006|6''|New York City|April: Bronx, Brooklyn, Queens, Staten Island <br> June: Manhattan|Selective true orthoimagery. Manhattan full true orthoimagery;  Bronx, Brooklyn, Queens, Staten Island true orthos for buildings greater than six stories.|No
|2008|6''|New York City|March 10 - May 14: Bronx, Brooklyn, Queens, Staten Island <br>June: Manhattan|Selective true orthoimagery. Manhattan full true orthoimagery;  Bronx, Brooklyn, Queens, Staten Island true orthos for buildings greater than five stories.|Yes
|2010|6''|New York City|April 1 - April 10: Bronx, Brooklyn, Queens, Staten Island <br>June 15: Manhattan|Selective true orthoimagery. Manhattan full true orthoimagery;  Bronx, Brooklyn, Queens, Staten Island true orthos for buildings greater than five stories.|Yes
|2012|6''|New York City|March 30 - April 6: Bronx, Brooklyn, Queens, Staten Island <br>June 15 -16 and June 20: Manhattan|Selective true orthoimagery. Manhattan full true orthoimagery;  Bronx, Brooklyn, Queens, Staten Island true orthos for buildings greater than five stories.|Yes
|2014|6''|New York City|April 1 - April 3: Bronx, Brooklyn, Queens, Staten Island <br>April 25: Water <br>June 1: Manhattan|Full true orthoimagery|Yes
|2016|6''|New York City|March 26 - April 5: Bronx, Brookyln, Manhattan, Queens, Staten Island|Full true orthoimagery|Yes
