import csv

def read_csv(filename, source):
  D = []
  with open(filename, newline='') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        if row[0].startswith('#'):
          continue
        d = {}
        d["term"] = row[0].replace(" ","")
        d["label"] = row[1]
        d["definition"] = row[2]
        d["source"] = source
        D.append(d)

  return D

def read_xml(filename, source):
  # https://gitlab.irap.omp.eu/CDPP/TREPS/blob/master/server/kernel/data/frames.xml
  import xmltodict

  with open(filename) as fd:
    doc = xmltodict.parse(fd.read())

  D = []
  for frame in doc['treps']['frames']['frame']:
    d = {'term': frame['@id'],
         'label': frame['fullname'],
         'definition': frame['description'],
         'source': source
    }
    D.append(d)

  return D

D1 = read_csv('IVOA-2007-STCT.csv', 'https://www.ivoa.net/documents/REC/DM/STC-20071030.html#_Toc181531804')
D2 = read_csv('cdpp-adma-request.csv', 'Request sent to SPASE email list')
D3 = read_csv('spase.csv', 'https://spase-group.org/data/model/spase-2.4.0/spase-2_4_0_xsd.html#CoordinateSystemName')
D4 = read_csv('sunpy.csv', 'https://github.com/sunpy/sunpy/wiki/Coordinate-systems')
D5 = read_csv('laundal-and-richmond-2016.csv', 'https://doi.org/10.1007/s11214-016-0275-y')
D6 = read_xml('frames.xml','https://gitlab.irap.omp.eu/CDPP/TREPS/blob/master/server/kernel/data/frames.xml')
D = [*D1, *D2, *D3, *D4, *D5, *D6]

# https://stackoverflow.com/a/21004113
sorted(D, key=lambda x: x['term'])

import json
with open("combined.json", "w") as outfile: 
    json.dump(D, outfile, indent=2)

with open("../VEP-for-IVOA.head.md","r") as f:
  head = f.read()

with open("../VEP-for-IVOA.md", "w") as outfile: 
  outfile.write(head+"\n")
  for d in D:
    outfile.write(f'**Term**: `#{d["term"]}`\n')
    outfile.write(f'**Label**: {d["label"]}\n')
    outfile.write(f'**Definition**: {d["definition"]}\n')
    outfile.write(f'______________________________________________________________\n\n')


if False:
  # Old code. Used 
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

