# the order of sparql and csv files is important
techUSA.nt:sample-2.sparql TechCrunchcontinentalUSA.csv
	tarql --ntriples $^ > $@

# Blazegraph organize info using namespaces
# We assume a test namespace is created already.	
# where the jar file is located
BLAZE_GRAPH_HOME="/home/ubuntu"
loaddata: techUSA.nt	
	java -cp $(BLAZE_GRAPH_HOME)/blazegraph.jar com.bigdata.rdf.store.DataLoader -namespace test $<
clean:	
	rm -rf techUSA.nt
