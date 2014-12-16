import csv, simplejson, decimal, codecs

# Convert MASTER Metadata File (downloaded as a CSV)
# to json format for import into mongodb
# Version: 1.0
# Date: 2014/12/16
# Author: Carlos Granier

data = open("MASTER-Metadata-File_Episodes.csv")
reader = csv.DictReader(data, delimiter=",", quotechar='"')

with codecs.open("out.json", "w", encoding="utf-8") as out:
   for r in reader:
      for k, v in r.items():
         # make sure nulls are generated
         if not v:
            r[k] = None
         # parse and generate decimal arrays
         #elif k == "loc":
         #   r[k] = [decimal.Decimal(n) for n in v.strip("[]").split(",")]
         # parse and generate Category array
         elif k == "Category":
            r[k] = [n for n in v.strip("[]").split("|")]
         elif k == "Genre":
            r[k] = [n for n in v.strip("[]").split("|")]
         elif k == "Keywords":
            r[k] = [n for n in v.strip("[]").split("|")]
         elif k == "Cast":
            r[k] = [n for n in v.strip("[]").split("|")]
         elif k == "Director":
            r[k] = [n for n in v.strip("[]").split("|")]
         elif k == "YouTubeAdBreaks":
            r[k] = [n for n in v.strip("[]").split("|")]
         elif k == "HuluAdBreaks":
            r[k] = [n for n in v.strip("[]").split(",")]
         # generate a number
         #elif k == "EpisodeNumber":
         #   r[k] = int(v)
      out.write(simplejson.dumps(r, ensure_ascii=False, use_decimal=True)+"\n")