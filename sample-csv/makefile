all: techUSA.nt table_2.nt

# the order of sparql and csv files is important
techUSA.nt:sample-2.sparql TechCrunchcontinentalUSA.csv
	tarql --ntriples $^ > $@
table_2.nt:sample-2.sparql table_2.csv
	tarql --ntriples $^ > $@
clean:	
	rm -rf *.nt
