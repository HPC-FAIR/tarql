.PHONY : nts
nts : rodinia_3.1_cuda_bfs_datalevel-lassen-plus-rowId.nt rodinia_3.1_cuda_bfs_kernellevel-lassen-plus-rowId.nt rodinia_3.1_cuda_cfd_datalevel-lassen-plus-rowId.nt rodinia_3.1_cuda_cfd_kernellevel-lassen-plus-rowId.nt rodinia_3.1_cuda_gaussian_datalevel-lassen-plus-rowId.nt rodinia_3.1_cuda_gaussian_kernellevel-lassen-plus-rowId.nt

%.nt: %.csv xplacer.sparql 
	tarql --ntriples $< > $*.nt
# a shortcut
clean:	
	rm -rf *.nt
