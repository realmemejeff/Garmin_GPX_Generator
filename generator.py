files_lines = ['<?xml version="1.0" encoding="UTF-8" standalone="no"?>', '<gpx', '  xmlns="http://www.topografix.com/GPX/1/1"', '  xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3"', '  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"', '  xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd', '  http://www.garmin.com/xmlschemas/GpxExtensions/v3', '  http://www8.garmin.com/xmlschemas/GpxExtensions/v3/GpxExtensionsv3.xsd"', '  version="1.1"', '  creator="gpx-poi.com">']

location = input('Google coordinate copied text: ')
place = input('Place name lowercase: ')
location0 = location.replace(' ', '')
location1 = location0.split(',')
loc1 = str(location1[0])
loc2 = str(location1[1])
size0 = len(loc1)
size1 = len(loc2)
loc4 = loc1[:size0 - 8]
loc5 = loc2[:size1 - 8]
loc6 = '  <wpt lat="' + loc4 + '" lon="' + loc5 + '">'
files_lines.append(loc6)
loc8 = place.upper()
loc7 = '    <name>' + loc8 + '</name><cmt>崸Х諟㹰</cmt><extensions>'
files_lines.append(loc7)
files_lines.append('    </extensions>')
files_lines.append('  </wpt>')
files_lines.append('</gpx>')
outfile = place + '.gpx'
with open(outfile, 'w') as filee:
  for x in files_lines:
    filee.write("%s\n" % x)
