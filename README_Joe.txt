tRNA Aminoacylation model: Script written by Joe Cursons, 11-13/03/2015
Protein translation model: Scripts written by Dan and Denis, 11-13/03/2015

tRNA Aminoacylation SBGN representation: Created by Joe Cursons, 12-13/03/2015
Protein translation SBGN representation: Created by Joe Cursons and Hojjat Naderi, 10-13/03/2015



Continuation: 	Dan, Denis and Joe may be able to contribute a few days (and are relatively keen), 
			but it would be relatively low priority so may not be able to turn things around quickly.

		It probably doesn't make sense to continue with the current implementation of the translation model, because the model 
			file is larger than 1GB, and it would be infeasible to run.



Problems with the current implementation of tRNA aminoacylation:
1) The current tRNA aminoacylation implementation follows Jonathan's original model and describes this as a single reaction step. It would
	probably be more appropriate and realistic to describe this as a two step process where the AMP bound amino acid is first generated
	before ligation to the appropriate tRNA (with ejection of the AMP).



Problems with the current implementation of protein translation:
1) Currently ribosome stalling is not modelled. As a consequence we do not include tmRNA binding (although tmRNA aminoacylation is included
	within that submodel) and subsequent recycling/degradation of incomplete polypeptides. This would create further issues for
	integration, as we would need to create variables for the export of these incomplete polypeptides to the protein submodel.
2) The elongation factors are currently implemented as reactants and products of every reaction step; for a true representation they should
	probably be included as reaction modifiers.
3) EF-P, which catalyses the first synthesis between fMET and the second amino acid is not included within the reactions; it is described
	within the comments of Jonathan's code and the supplementary material
4) The current implementation reads a .csv file containing the protein sequences; ideally this information should be read from a knowledge
	base to allow future model generation as new data are collected
4) The reactions being constructed with python + libSBML should utilise the mRNA sequences (and known codon/anticodon matching) rather 
	than protein sequences to allow for mutations etc to be modelled


Problems with the current implementation of both submodules:
1) Water should probably be removed from the reactions, as execution of the Gillespie algorithm will encounter difficulties due to the
	relatively high abundance of water molecules, and water is currently included in the reaction rate definition.
2) Reaction requirements are currently not being calculated - this will be an issue for integration, as tRNA aminoacylation and protein
	translation together use the majority of cellular ATP.
3) The two submodules should probably be combined into a single submodel - within Jonathan's code, a check is implemented after the
	"process permutation" to ensure that tRNA aminoacylation occurs before (although not necessarily *directly* before) translation.
	This would also make integrations life easier, as aminoacylated tRNAs could be contained within the single model, rather than
	being passed between models of the separate submodules.
