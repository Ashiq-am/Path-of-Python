# Import libraries
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

rec1 = SeqRecord(Seq("MMYQQGCFAGGTVLRLAKDLAENNRGARVLVVCSEITAVTFRGPSETHLDSMVGQALFGD"
					+ "GAGAVIVGSDPDLSVERPLYELVWTGATLLPDSEGAIDGHLREVGLTFHLLKDVPGLISK"
					+ "NIEKSLKEAFTPLGISDWNSTFWIAHPGGPAILDQVEAKLGLKEEKMRATREVLSEYGNM"),
				id="gi|14150838|gb|AAK54648.1|AF376133_1",
				description="chalcone synthase [Cucumis sativus]")

rec2 = SeqRecord(Seq("MVTVEEFRRAQCAEGPATVMAIGTATPSNCVDQSTYPDYYFRITNSEHKVELKEKFKRMC"
					+ "EKSMIKKRYMHLTEEILKENPNICAYMAPSLDARQDIVVVEVPKLGKEAAQKAIKEWGQP"
					+ "KSKITHLVFCTTSGVDMPGCDYQLTKLLGLRPSVKRFMMYQQGCFAGGTVLRMAKDLAEN"
					+ "NKGARVLVVCSEITAVTFRGPNDTHLDSLVGQALFGDGAAAVIIGSDPIPEVERPLFELV"
					+ "SAAQTLLPDSEGAIDGHLREVGLTFHLLKDVPGLISKNIEKSLVEAFQPLGISDWNSLFW"
					+ "IAHPGGPAILDQVELKLGLKQEKLKATRKVLSNYGNMSSACVLFILDEMRKASAKEGLGT"
					+ "TGEGLEWGVLFGFGPGLTVETVVLHSVAT"),
				id="gi|13925890|gb|AAK49457.1|",
				description="chalcone synthase [Nicotiana tabacum]")
sequences = [rec1, rec2]

# Writing to file
with open("example.fasta", "w") as output_handle:
	SeqIO.write(sequences, output_handle, "fasta")

for record in SeqIO.parse("example.fasta", "fasta"):
	print("ID %s" % record.id)
	print("Sequence length %i" % len(record))
