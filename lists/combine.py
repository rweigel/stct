import csv

def read_csv(filename, sourceLabel, source):
  D = []
  print("Reading", filename)
  with open(filename, newline='') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        if row[0].startswith('#'):
          continue

        d = {"term": "", "label": "", "definition": "", "sourceLabel": sourceLabel, "source": source}

        d["term"] = row[0].replace(" ","")
        if len(row) > 1:
          d["label"] = row[1]
        if len(row) > 2:
          d["definition"] = row[2]

        D.append(d)

  return D

def read_xml(filename, sourceLabel, source):
  import xmltodict

  print("Reading", filename)
  with open(filename) as fd:
    doc = xmltodict.parse(fd.read())

  D = []
  for frame in doc['treps']['frames']['frame']:
    d = {'term': frame['@id'],
         'label': frame['fullname'],
         'definition': frame['description'],
         'sourceLabel': sourceLabel,
         'source': source
    }
    D.append(d)

  return D

def read_md():
  # Old code. Not used anymore.
  with open('VEP-for-IVOA.md') as mdfile:
    line = None
    d = {}
    while line != '':
      line = mdfile.readline()
      if line.startswith('**Term**: '):
        d["term"] = line.replace("**Term**: ","").rstrip().replace('#','').replace('`','').rstrip()
      if line.startswith('**Label**: '):
        d["label"] = line.replace("**Label**: ","").replace('#','').replace('`','').rstrip()

      if line.startswith('**Definition**:'):
        d["source"] = "https://gitlab.irap.omp.eu/CDPP/TREPS/blob/master/server/kernel/data/frames.xml"
        d["definition"] = ""
        while True:
          line = mdfile.readline()
          if line.startswith('____'):
            D.append(d)
            break
          d["definition"] += line


D1 = read_csv('IVOA-2007-STCT.csv', 'IVOA', 'https://www.ivoa.net/documents/REC/DM/STC-20071030.html#_Toc181531804')
D2 = read_csv('cdpp-adma-request.csv', 'CDPP/AMDA', 'Request sent to SPASE email list')
D3 = read_csv('spase.csv', 'SPASE', 'https://spase-group.org/data/model/spase-2.4.0/spase-2_4_0_xsd.html#CoordinateSystemName')
D4 = read_csv('sunpy.csv', 'SunPy', 'https://github.com/sunpy/sunpy/wiki/Coordinate-systems')
D5 = read_csv('laundal-and-richmond-2016.csv', 'Laundal', 'https://doi.org/10.1007/s11214-016-0275-y')
D6 = read_xml('frames.xml','TREPS', 'https://gitlab.irap.omp.eu/CDPP/TREPS/blob/master/server/kernel/data/frames.xml')
D7 = read_csv('spice-built-in-pck-body-fixed.csv', 'NAIF', 'https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/frames.html#Appendix.%20%60%60Built%20in''%20Inertial%20Reference%20Frames')

D = [*D1, *D2, *D3, *D4, *D5, *D6, *D7]

# https://stackoverflow.com/a/21004113
D = sorted(D, key=lambda x: x['term'])

import json
filename = "combined.json"
with open(filename, "w") as outfile:
  print("Writing", filename)
  json.dump(D, outfile, indent=2)

filename = "combined.csv"
with open(filename, "w") as outfile:
  print("Writing", filename)
  outfile.write("term,label,definition,sourceLabel,source\n")
  for d in D:
    outfile.write(f'{d["term"]},"{d["label"]}","{d["definition"]}",{d["sourceLabel"]},"{d["source"]}"\n')

filename = "../VEP-for-IVOA.head.md"
with open(filename,"r") as f:
  print("Reading", filename)
  head = f.read()

filename = "../VEP-for-IVOA.md"
with open(filename, "w") as outfile: 
  print("Writing", filename)
  outfile.write(head+"\n")
  for d in D:
    outfile.write(f'**Term**: `#{d["term"]}`\n')
    outfile.write(f'**Label**: {d["label"]}\n')
    outfile.write(f'**Definition**: \n{d["definition"]}\n')
    outfile.write(f'______________________________________________________________\n\n')
