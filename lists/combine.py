import os
import csv
import glob
import json

def read_csv(filename, sourceLabel):
  D = []
  print("Reading", filename)
  with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    source_url = header[0].split("#")[1].strip()
    source_file = filename
    for row in reader:
      d = {"term": "", "label": "", "definition": "", "sourceLabel": sourceLabel, "sourceURL": source_url, "sourceFile": source_file}
      d["term"] = row[0].replace(" ","")
      if len(row) > 1:
        d["label"] = row[1]
      if len(row) > 2:
        d["definition"] = row[2]

      D.append(d)

  return D

def read_xml(filename, source_label, source_url):
  import xmltodict

  print("Reading", filename)
  with open(filename) as fd:
    doc = xmltodict.parse(fd.read())

  D = []
  for frame in doc['treps']['frames']['frame']:
    definition = frame['description']
    if definition is not None:
      definition = definition.replace('"', '""')
    d = {'term': frame['@id'],
         'label': frame['fullname'],
         'definition': definition,
         'sourceLabel': source_label,
         'sourceURL': source_url,
         'sourceFile': filename
    }
    D.append(d)

  return D

data = []
files = glob.glob('**/*.csv') + glob.glob('**/*.xml')
for file in files:
  file_name = file.split('/')[1]
  file_id = file_name.split('-')[0]
  file_ext = os.path.splitext(file_name)[1]
  if file_ext == '.csv':
    source_data = read_csv(file, file_id)
  else:
    if file_id.startswith('SPICE'):
      source_url = "https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/frames.html#Complete%20List%20of%20%60%60Built%20in''%20Inertial%20Reference%20Frames"
    if file_id.startswith('TREPS'):
      source_url = "https://gitlab.irap.omp.eu/CDPP/TREPS/blob/master/server/kernel/data/frames.xml"
    source_data = read_xml(file, file_id, source_url)
  data = [*data, *source_data]


# https://stackoverflow.com/a/21004113
data = sorted(data, key=lambda x: x['term'])

filename = "combined.json"
with open(filename, "w") as outfile:
  print("Writing", filename)
  json.dump(data, outfile, indent=2)

filename = "combined.csv"
with open(filename, "w") as outfile:
  print("Writing", filename)
  outfile.write("term,sourceLabel,label,definition,sourceURL,sourceFile\n")
  for d in data:
    outfile.write(f'{d["term"]},{d["sourceLabel"]},"{d["label"]}","{d["definition"]}","{d["sourceURL"]}","{d["sourceFile"]}"\n')

