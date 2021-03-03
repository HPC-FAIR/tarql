all: techUSA.nt soccer-player.nt rodinia_3.1_cuda_nw_labelledData-lassen-plus-rowId.nt

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

# the source of the csv
# https://docs.google.com/spreadsheets/d/1fbQ-mRpkCmZBGqhIiuN0f4Lfq8HdJac8FyZPbMBJv9M/edit?usp=sharing
# changes from the raw data from gitlab: 
# https://gitlab.com/DATA-PLACEMENT-LDRD/optimization_unified_memory/-/blob/master/rodinia_3.1/cuda/nw/labelledData.csv
# 1. add No as ID
# 2. remove spaces in column names: SPARQL cannot handle them
rodinia_3.1_cuda_nw_labelledData-lassen-plus-rowId.nt:xplacer.sparql rodinia_3.1_cuda_nw_labelledData-lassen-plus-rowId.csv 
	tarql --ntriples $^ > $@
# a shortcut
xplacer:rodinia_3.1_cuda_nw_labelledData-lassen-plus-rowId.nt	
clean:	
	rm -rf *.nt
