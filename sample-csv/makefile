all: techUSA.nt soccer-player.nt

# the order of sparql and csv files is important
techUSA.nt:soccer-player.sparql TechCrunchcontinentalUSA.csv
	tarql --ntriples $^ > $@

# Blazegraph organize info using namespaces
# We assume a test namespace is created already.	
# where the jar file is located
BLAZE_GRAPH_HOME="/home/ubuntu"
#loaddata: techUSA.nt	
#	java -cp $(BLAZE_GRAPH_HOME)/blazegraph.jar com.bigdata.rdf.store.DataLoader -namespace test $<
	
soccer-player.nt:sample-soccer-player.sparql soccer-player.csv
	tarql --ntriples $^ > $@
clean:	
	rm -rf *.nt
