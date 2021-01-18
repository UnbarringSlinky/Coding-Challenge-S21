#https://biopython-tutorial.readthedocs.io/en/latest/notebooks/17%20-%20Graphics%20including%20GenomeDiagram.html

from Bio import SeqIO
from IPython.core.display import Image
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
record = SeqIO.read("Genome.gb", "genbank")
gd_diagram = GenomeDiagram.Diagram("Tomato curly stunt virus")

gd_track_for_features = gd_diagram.new_track(1, name="Features") 
gd_feature_set = gd_track_for_features.new_set()

for feature in record.features: #Iterates Through all features in the Genome.gb file
    if feature.type != "gene":
        continue
    if len(gd_feature_set)%2==0:
        color = colors.blue
    else:
        color = colors.red
    gd_feature_set.add_feature(feature, color=color, label=True, label_size= 16) #populates our diagram with our feature from Genome.gb
gd_diagram.draw(format="circular", circular=True, pagesize=("A4"),
                fragments= 4, start=0, end=len(record), circle_core=.6,tracklines=0) #Draws the diagram in a circular fashion with it terminating at the length of our records
gd_diagram.write("TomatoCurlyStuntVirus.png", "PNG") #Writes information to a file called TomatoCurlyStunt.png, in the format of a PNG
Image("TomatoCurlyStuntVirus.png")
