# Wi-Fi Hotspot Locations
Geometry Type: point<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/WiFiHotspots.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The purpose of this dataset is to help users identify Wi-Fi Hotspot locations throughout New York City. 
**Description** |Public Wi-Fi Hotspot locations throughout the 5 boroughs including LinkNYC-Citybridge.
**Source(s)** |Wi-Fi providers include At&T, LinkNYC-Citybridge (BETA), BPL, Cablevision, Chelsea, City Tech, Downtown Brooklyn, Harlem, Manhattan Down Alliance, NYCHA, NYPL, QPL, Time Warner Cable, Transit Wireless, and various partners.
**Publication Dates** |**Data**: 09/12/2014<br>**Last Update**: 09/22/2016<br>**Metadata**: 12/22/2016<br>**Update Frequency**: As needed
**Available Formats** |Shapefile. Additional data formats are available for download on the [NYC Open Data Portal](https://data.cityofnewyork.us/Social-Services/NYC-Wi-Fi-Hotspot-Locations/a9we-mtpn).
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html)
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/Social-Services/NYC-Wi-Fi-Hotspot-Locations/a9we-mtpn
**Tags** |wi-fi, parks, wifi, nyc wi-fi hotspot locations, internet, mifi, connectivity, optics, doitt, mobile, web, www, world wide web, websites
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |Data is current as of last update date.
**Positional Accuracy** |Locations of Wi-Fi Hotspots are provided by service providers. 
**Features Captured** |See description
**Features Excluded** |This dataset does not include all LinkNYC - CityBridge, LLC (Free) internet kiosks. For LinkNYC locations, see [Open Data Portal - LinkNYC](https://data.cityofnewyork.us/Social-Services/LinkNYC-Map/tgrn-h24f)
**Capture and Update Notes** |
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| BORO | Two-letter code for borough:<br>BK = Brooklyn <br>BX = Bronx <br>MN = Manhattan<br>QN = Queens<br>QU=Queens<br>SI=Staten Island | text | No
| TYPE | Type of wifi:<br>Free<br>Limited Free<br>Partner Site | text | No
| PROVIDER | Wi-Fi provider. Wi-Fi providers include: <br>At&T<br>LinkNYC-Citybridge (BETA)<br>BPL<br>Cablevision<br>Chelsea<br>City Tech<br>Downtown Brooklyn<br>Harlem<br>Manhattan Down Alliance<br>NYCHA<br>NYPL<br>QPL<br>Time Warner Cable<br>Transit Wireless<br>Partners | text | No
| NAME | Name of Wi-Fi | text | No
| LOCATION | Location of Wi-Fi | text | No
| LOCATION_TYPE | Type of Location<br>Indoor<br>Library<br>Outdoor<br>Outdoor Kiosk<br>Outdoor TWC Aerial<br>Subway Station | text | No
| REMARKS | Miscellaneous notes on location (ex. station number) or status | text | No
| CITY | City of Wi-Fi location | text | No
| SSID | Network name | text | No
| SOURCEID | ID of feature from provider source | text | No
