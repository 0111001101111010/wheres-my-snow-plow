#!/usr/bin/python
# -*- coding: utf-8 -*-
from geocodio import GeocodioClient
client = GeocodioClient("")
geocoded_location = client.geocode("Main St. Norfolk to Tidewater Dr VA")

print geocoded_location