import csv, decimal, codecs

# Extract MASTER Metadata File (downloaded as a CSV)
# to CSV format reports for selected titles
# For AdRise
# Version: 1.0
# Date: 2014/12/16
# Author: Carlos Granier

INFILE = "MASTER-Metadata-File_Episodes.csv"
OUTFILE = "calzon-quitao.csv" # generate name from input argv MediaKey

data = open(INFILE)
reader = csv.DictReader(data, delimiter=",", quotechar='"')

with open(OUTFILE, "w") as out:
   # Title:true, EpisodeTitle:true, EpisodeNumber:true, EpisodeSummary:true, Director:true, Cast:true, Genre:true, HuluAdBreaks:true
   fieldnames = ['Title', 'EpisodeTitle', 'EpisodeNumber', 'EpisodeSummary', 'Director', 'Cast', 'Genre', 'HuluAdBreaks']
   writer = csv.DictWriter(out, fieldnames=fieldnames, restval='', extrasaction='ignore')
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
            r[k] = v.replace("|",",")
         elif k == "Genre":
            r[k] = v.replace("|",",")
         elif k == "Keywords":
            r[k] = v.replace("|",",")
         elif k == "Cast":
            r[k] = v.replace("|",",")
         elif k == "Director":
            r[k] = v.replace("|",",")
         elif k == "YouTubeAdBreaks":
            r[k] = v.replace("|",",")
         elif k == "HuluAdBreaks":
            if r[k] != "":
               adbreaks = v.split(",")
               for ad in adbreaks:
                  adhour   = int(ad[0:2]) * 60 * 60
                  adminute = int(ad[3:5]) * 60
                  adsecond = int(ad[6:8])
                  adframe  = int(ad[9:11])
                  adbreakseconds = adhour + adminute + adsecond
                  print r["MediaKey"], " ", r["EpisodeTitle"], " ", adbreakseconds
               r[k] = v.replace("|",",")
         # generate a number
         #elif k == "EpisodeNumber":
         #   r[k] = int(v)
      writer.writerow(r)
