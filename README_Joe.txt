tRNA Aminoacylation model: Script written by Joe Cursons, 11-13/03/2015
Protein translation model: Scripts written by Dan (translation elongation and termination) and Denis (translation initiation), 11-13/03/2015

tRNA Aminoacylation SBGN representation: Created by Joe Cursons, 12-13/03/2015
Protein translation SBGN representation: Created by Joe Cursons and Hojjat Naderi, 10-13/03/2015



Continuation: 	Dan, Denis and Joe may be able to contribute a few days (and are relatively keen), 
			but it would be relatively low priority so may not be able to turn things around quickly.

		It probably doesn't make sense to continue with the current implementation of the translation model, because the model 
			file is larger than 1GB, and it would be infeasible to run.


Resource allocation for tRNA aminoacylation (to be implemented):
Sum over all tRNAs/amino acids; min{tRNA & corresponding amino acid} :: one ATP each (but forms an AMP) & corresponding amino acids/tRNAs
	+ min{Met_MG488, FTHF10, H2O}
	+ min{Gln, ATP, H2O} for Glu amidotransferase reaction

	



Notes on the current implementation of protein translation:
1) To avoid the definition of events/conditional statements, we have constructed reactions describing the per-amino acid elongation of 
	polypeptides. For every protein of length L, there are L+2 species (position 0 -> position L, and a position 'F' [for final] which
	is passed to translation termination). There are also reactions specifying the progression between species, corresponding to the
	addition of individual amino acids.
	- The species are labelled according to the mRNA sequence name (e.g. MGxyz), together with the position (A) --> e.g. MGxyz_pA
2) As a consequence of this model formulation, it can (theoretically) be run using a Gillespie algorithm to model stochasticity 
	associated with the allocation of GTP and elongation factors to active ribosomes.


Alternatives for the implementation of protein translation:
1) **Requires the capability to dynamically define variables** - rather than having a huge state space and tracking progression of a
	relatively small number of paths/transitions through the state space, it would be a much more compact representation to have
	variables which track the position of a ribosome upon a specific mRNA. Unfortunately, it is difficult/impossible to know in 
	advance how many ribosomes are currently active, thus it would require functionality within SBML to dynamically define variables
	(or dynamically expand/contract a vector which lists this information).


Problems with the current implementation of tRNA aminoacylation:
1) The current tRNA aminoacylation implementation follows Jonathan's original model and describes this as a single reaction step. It would
	probably be more appropriate and realistic to describe this as a two step process where the AMP bound amino acid is first generated
	before ligation to the appropriate tRNA (with ejection of the AMP).


Problems with the current implementation of protein translation:
1) As noted above, the current model is very large (the SBML file is greater than 1GB) and it is infeasible to load this into a simulator
	such as COPASI, let alone run the simulation.
2) Currently ribosome stalling is not modelled. As a consequence we do not include tmRNA binding (although tmRNA aminoacylation is included
	within that submodel) and subsequent recycling/degradation of incomplete polypeptides. This would create further issues for
	integration, as we would need to create variables for the export of these incomplete polypeptides to the protein submodel.
3) The elongation factors are currently implemented as reactants and products of every reaction step; for a true representation they should
	probably be included as reaction modifiers.
4) EF-P, which catalyses the first synthesis between fMET and the second amino acid is not included within the reactions; it is described
	within the comments of Jonathan's code and the supplementary material
5) The current implementation reads a .csv file containing the protein sequences; ideally this information should be read from a knowledge
	base to allow future model generation as new data are collected
6) The reactions being constructed with python + libSBML should utilise the mRNA sequences (and known codon/anticodon matching) rather 
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


Problems with the SBGN representation of the protein translation model:
1) Because the protein translation model is defined with a separate reaction for every elongation step, the resulting SBGN diagram would
	be incomprehensible due to its size and number of nodes. A more efficient representation would be to create a SBGN submap for the
	addition of specific amino acids, and then for each protein, connect these submaps corresponding to the sequence/elongation order.