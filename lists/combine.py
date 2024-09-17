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
      d = {"term": "", "label": "", "definition": "", "sourceLabel": sourceLabel, "source_url": source_url, "source_file": source_file}
      d["term"] = row[0].replace(" ","")
      if len(row) > 1:
        d["label"] = row[1]
      if len(row) > 2:
        d["definition"] = row[2]

      D.append(d)

  return D

def read_xml(filename, sourceLabel, source_url):
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
         'source_url': source_url,
         'source_file': filename
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
    source = "https://gitlab.irap.omp.eu/CDPP/TREPS/blob/master/server/kernel/data/frames.xml"
    source_data = read_xml(file, file_id, source)
  data = [*data, *source_data]
  # https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/frames.html#Complete%20List%20of%20%60%60Built%20in''%20Inertial%20Reference%20Frames

# https://stackoverflow.com/a/21004113
data = sorted(data, key=lambda x: x['term'])

filename = "combined.json"
with open(filename, "w") as outfile:
  print("Writing", filename)
  json.dump(data, outfile, indent=2)

filename = "combined.csv"
with open(filename, "w") as outfile:
  print("Writing", filename)
  outfile.write("term,label,definition,sourceLabel,source_url,source_file\n")
  for d in data:
    outfile.write(f'{d["term"]},"{d["label"]}","{d["definition"]}",{d["sourceLabel"]},"{d["source_url"]}","{d["source_file"]}"\n')


if False:
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
