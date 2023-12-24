
# Tire & Wheel Dimension Parser

## Overview
This Python script extracts the permissible tire and wheel dimensions for Swiss vehicles based on their type approval codes. Utilizing sophisticated regular expressions (regex) and parsing logic, it tackles the challenge of extracting dimensions scattered across three different fields in various formats. This tool is invaluable for businesses needing quick access to these specific vehicle details.

## Key Features
* **Advanced Regex & Parsing Logic**: The script's core lies in its ability to handle the diverse formats and fields in which tire and wheel dimensions are presented, decoding them efficiently.
* **User-Friendly**: It offers an easy way for users to access the necessary dimensions to ensure they purchase or mount the correct tires and wheels for a specific vehicle.

## Use Cases
* **Businesses**: Automotive companies can leverage this tool to quickly and accurately determine the permissible tire dimensions for different vehicles.
* **Individual Users**: Even private individuals can use this script to verify that they are selecting the right tires for their vehicle.

## Future Relevance
While the type approval codes in Switzerland are set to be phased out, this tool remains invaluable until then, continuing to provide access to crucial vehicle data via the type approval certificate.

The documentation of the data : [Documentation](https://www.astra.admin.ch/astra/de/home/dokumentation/daten-informationsprodukte/fahrzeugdaten.html)

The url to download the data : [Homologation Data of swiss vehicles](https://ivz-opendata.ch/opendata/2000-Typengenehmigungen_TG_TARGA/2200-Basisdaten_TG_ab_1995/TG-Automobil.txt)

`curl https://ivz-opendata.ch/opendata/2000-Typengenehmigungen_TG_TARGA/2200-Basisdaten_TG_ab_1995/TG-Automobil.txt --output TG-Automobil.txt`
