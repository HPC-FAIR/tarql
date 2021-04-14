CSVFILES = \
rodinia_3.1_cuda_bfs_datalevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_bfs_kernellevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_cfd_datalevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_cfd_kernellevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_gaussian_datalevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_gaussian_kernellevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_nw_datalevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_nw_kernellevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_streamcluster_datalevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_streamcluster_kernellevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_lud_datalevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_lud_kernellevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_hotspot_datalevel-lassen-plus-rowId.csv \
rodinia_3.1_cuda_hotspot_kernellevel-lassen-plus-rowId.csv

NTFILES = $(CSVFILES:.csv=.nt)
JSONLDFILES = $(NTFILES:.nt=.jsonld)


GITHUBRAWURL="https://raw.githubusercontent.com/HPC-FAIR/tarql/master/xplacer-csv/"

#%.jsonld: %.nt
#	curl -L "http://rdf-translator.appspot.com/convert/nt/json-ld/html/${GITHUBRAWURL}$<" --output $*.jsonld

#%.nt: %.csv xplacer.sparql 
#	tarql --ntriples xplacer.sparql $< > $*.nt

${NTFILES}:  
	tarql --ntriples xplacer.sparql $(@:%.nt=%.csv) xplacer.sparql > $@


# rdf-translator service has issue taking content using the POST API.
# Use GET API and having github hosting nt files tentatively as a workaround for now.

${JSONLDFILES}:  
	curl -L "http://rdf-translator.appspot.com/convert/nt/json-ld/html/${GITHUBRAWURL}$(@:%.jsonld=%.nt)" --output $@


nt: ${NTFILES}

jsonld: ${JSONLDFILES}


# a shortcut
clean:	
	rm -rf *.nt
