all: techUSA.nt table_2.nt

# the order of sparql and csv files is important
techUSA.nt:sample-2.sparql TechCrunchcontinentalUSA.csv
	tarql --ntriples $^ > $@

# Blazegraph organize info using namespaces
# We assume a test namespace is created already.	
# where the jar file is located
BLAZE_GRAPH_HOME="/home/ubuntu"
#loaddata: techUSA.nt	
#	java -cp $(BLAZE_GRAPH_HOME)/blazegraph.jar com.bigdata.rdf.store.DataLoader -namespace test $<
	
table_2.nt:sample-arsenal-table_2.sparql table_2.csv
	tarql --ntriples $^ > $@
clean:	
	rm -rf *.nt
