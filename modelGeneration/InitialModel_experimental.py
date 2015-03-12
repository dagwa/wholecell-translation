
#################################
# Initialization Block
#################################


import sys
import csv

# Get the Protein sequences
prot_names=list()
prot_len=list()
sequence=list()

f = open('ProtSeq.csv', 'rt')

reader = csv.reader(f)
your_list = list(reader)

for i in range(1,len(your_list)): #skip the first one
    prot_names = prot_names+[your_list[i][0]]
    prot_len   = prot_len+[your_list[i][1]]
    sequence   = sequence+[your_list[i][2]]

f.close()

# Get the AA to trna associations
SingleAA = {
  'A':'MG471',
  'N':'MG514',
  'D':'MG489',
  'C':'MG483',
  'E':'MG513',
  'Q':'MG502',
  'H':'MG518',
  'M':'MG485',
  'F':'MG490',
  'P':'MG484',
  'Y':'MG503',
  'V':'MG511',
  'R':['MG492',  'MG495', 'MG497', 'MG523'],
  'G': ['MG493', 'MG499'   ],
  'I': ['MG472', 'MG486'   ],
  'L': ['MG500', 'MG508', 'MG519', 'MG520'],
  'K': ['MG501', 'MG509'   ],
  'S': ['MG475', 'MG487' ,'MG506', 'MG507'],
  'T': ['MG479', 'MG510', 'MG512'] ,
  'W': ['MG496', 'MG504'   ],
  'Fmet': ['MG488']     
}


#  List of ribosome-bound mRNAs
#  Lengths of nascent polypeptides (proteolysis tags)
#  tRNA sequences of protein monomers and proteolysis tags 
#  List of ribosome-bound mRNAs
#  Lengths of nascent polypeptides (proteolysis tags)
#  State of each ribosome: free, actively translating, or stalled
#  Counts of mRNA, aminoacylated tRNA, and aminoacylated tmRNA species



#
# mRNAspecies = ['mRNA1', 'mRNA2']




# Model builing Block



from libsbml import *





def create_species(model, var_name):
  s1 = model.createSpecies()
  check(s1,                                 'create species s1')
  check(s1.setName(var_name),                     'set species s1 name')
  check(s1.setId(var_name),                     'set species s1 id')
  check(s1.setCompartment('c'),            'set species s1 compartment')
  check(s1.setConstant(False),              'set "constant" attribute on s1')
  check(s1.setInitialAmount(0),             'set initial amount for s1')
  check(s1.setSubstanceUnits('item'),       'set substance units for s1')
  check(s1.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
  check(s1.setHasOnlySubstanceUnits(True), 'set "hasOnlySubstanceUnits" on s1')

def riboPos_Elongation(model,startingPos,AAadded,tRNA_needed,iterator):
  # Create a reaction inside this model, set the reactants and products,
  # and set the reaction rate expression (the SBML "kinetic law").  We
  # set the minimum required attributes for all of these objects.  The
  # units of the reaction rate are determined from the 'timeUnits' and
  # 'extentUnits' attributes on the Model object.


  r1 = model.createReaction()
  check(r1,                                 'create reaction')
  check(r1.setName(startingPos+'_plus_'+AAadded+str(iterator)),                     'set reaction name')
  check(r1.setId(startingPos+'_plus_'+AAadded+str(iterator)),                     'set reaction id')
  check(r1.setReversible(False),            'set reaction reversibility flag')
  check(r1.setFast(False),                  'set reaction "fast" attribute')
 

  
    #STUFF THAT ACTUALLY CHANGES FROM REACTION TO REACTION 


  #Add the current Ribosome position
  species_ref1 = r1.createReactant()
  check(species_ref1,                       'create reactant')
  check(species_ref1.setSpecies(startingPos),      'assign reactant species')
  check(species_ref1.setConstant(True),     'set "constant" on species ref 1')
  #Produce the Next Position
  species_ref6 = r1.createProduct()
  check(species_ref6,                       'create product')
  check(species_ref6.setSpecies(startingPos[:-1]+str(int(startingPos[-1])+1)),      'assign product species')
  check(species_ref6.setConstant(True),     'set "constant" on species ref 2')


  #Add the amino-acylated tRNA
  species_ref2 = r1.createReactant()
  check(species_ref2,                       'create product')
  check(species_ref2.setSpecies('aminoacylated_'+ tRNA_needed),      'assign product species')
  check(species_ref2.setConstant(True),     'set "constant" on species ref 2')
  #Produce the Unloaded tRNA
  wtf = r1.createProduct()
  check(wtf,                       'create product')
  check(wtf.setSpecies(tRNA_needed),      'assign product species')
  check(wtf.setConstant(True),     'set "constant" on species ref 2') 



  #STUFF THAT IS THE SAME FOR ALL REACTIONS
  #Add the GTP
  species_ref2 = r1.createReactant()
  check(species_ref2,                       'create product')
  check(species_ref2.setSpecies('GTP'),      'assign product species')
  check(species_ref2.setConstant(True),     'set "constant" on species ref 2')
  #Add the EFG
  species_ref3 = r1.createReactant()
  check(species_ref3,                       'create product')
  check(species_ref3.setSpecies('MG_089_MONOMER'),      'assign product species')
  check(species_ref3.setConstant(True),     'set "constant" on species ref 2')
  #Add the EFTU
  species_ref4 = r1.createReactant()
  check(species_ref4,                       'create product')
  check(species_ref4.setSpecies('MG_451_MONOMER'),      'assign product species')
  check(species_ref4.setConstant(True),     'set "constant" on species ref 2')
  #Add the H2O
  species_ref5 = r1.createReactant()
  check(species_ref5,                       'create product')
  check(species_ref5.setSpecies('H2O'),      'assign product species')
  check(species_ref5.setConstant(True),     'set "constant" on species ref 2')
  
  
  #Produce the GDP
  species_ref8 = r1.createProduct()
  check(species_ref8,                       'create product')
  check(species_ref8.setSpecies('GDP'),      'assign product species')
  check(species_ref8.setConstant(True),     'set "constant" on species ref 2')
  #Produce the Pi
  species_ref9 = r1.createProduct()
  check(species_ref9,                       'create product')
  check(species_ref9.setSpecies('PI'),      'assign product species')
  check(species_ref9.setConstant(True),     'set "constant" on species ref 2')
  #Produce the EFG
  species_ref10 = r1.createProduct()
  check(species_ref10,                       'create product')
  check(species_ref10.setSpecies('MG_089_MONOMER'),      'assign product species')
  check(species_ref10.setConstant(True),     'set "constant" on species ref 2')
  #Produce the EFTU
  species_ref11 = r1.createProduct()
  check(species_ref11,                       'create product')
  check(species_ref11.setSpecies('MG_451_MONOMER'),      'assign product species')
  check(species_ref11.setConstant(True),     'set "constant" on species ref 2')
  
  math_ast = parseL3Formula('k * GTP * GTP * MG_089_MONOMER * MG_451_MONOMER * H2O')
  check(math_ast,                           'create AST for rate expression')
 
  kinetic_law = r1.createKineticLaw()
  check(kinetic_law,                        'create kinetic law')
  check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

def check(value, message):
  """If 'value' is None, prints an error message constructed using
  'message' and then exits with status code 1.  If 'value' is an integer,
  it assumes it is a libSBML return status code.  If the code value is
  LIBSBML_OPERATION_SUCCESS, returns without further action; if it is not,
  prints an error message constructed using 'message' along with text from
  libSBML explaining the meaning of the code, and exits with status code 1.
  """
  if value == None:
    raise SystemExit('LibSBML returned a null value trying to ' + message + '.')
  elif type(value) is int:
    if value == LIBSBML_OPERATION_SUCCESS:
      return
    else:
      err_msg = 'Error encountered trying to ' + message + '.' \
                + 'LibSBML returned error code ' + str(value) + ': "' \
                + OperationReturnValue_toString(value).strip() + '"'
      raise SystemExit(err_msg)
  else:
    return


def create_model(names,lengthsofseq,sequenceAAs):
  """Returns a simple but complete SBML Level 3 model for illustration."""

  # Create an empty SBMLDocument object.  It's a good idea to check for
  # possible errors.  Even when the parameter values are hardwired like
  # this, it is still possible for a failure to occur (e.g., if the
  # operating system runs out of memory).

  try:
    document = SBMLDocument(3, 1)
  except ValueError:
    raise SystemExit('Could not create SBMLDocumention object')

  # Create the basic Model object inside the SBMLDocument object.  To
  # produce a model with complete units for the reaction rates, we need
  # to set the 'timeUnits' and 'extentUnits' attributes on Model.  We
  # set 'substanceUnits' too, for good measure, though it's not strictly
  # necessary here because we also set the units for invididual species
  # in their definitions.

  model = document.createModel()
  check(model,                              'create model')
  check(model.setTimeUnits("second"),       'set model-wide time units')
  check(model.setExtentUnits("item"),       'set model units of extent')
  check(model.setSubstanceUnits('item'),    'set model substance units')

  # Create a unit definition we will need later.  Note that SBML Unit
  # objects must have all four attributes 'kind', 'exponent', 'scale'
  # and 'multiplier' defined.

  # per_second = model.createUnitDefinition()
  # check(per_second,                         'create unit definition')
  # check(per_second.setId('per_second'),     'set unit definition id')
  # unit = per_second.createUnit()
  # check(unit,                               'create unit on per_second')
  # check(unit.setKind(UNIT_KIND_SECOND),     'set unit kind')
  # check(unit.setExponent(-1),               'set unit exponent')
  # check(unit.setScale(0),                   'set unit scale')
  # check(unit.setMultiplier(1),              'set unit multiplier')

  # Create a compartment inside this model, and set the required
  # attributes for an SBML compartment in SBML Level 3.

  c1 = model.createCompartment()
  check(c1,                                 'create compartment')
  check(c1.setId('c'),                     'set compartment id')
  check(c1.setConstant(True),               'set compartment "constant"')
  check(c1.setSize(1),                      'set compartment "size"')
  check(c1.setSpatialDimensions(3),         'set compartment dimensions')
  check(c1.setUnits('litre'),               'set compartment size units')

  #############################################
  # Create ribosome position species (one for each position plus a final one)
  #############################################

  for n in range(len(names)): 

    #create the #AA positions
    for p in range(int(lengthsofseq[n])):
      create_species(model, names[n] + '_p' + str(p))

    #create the final position
    create_species(model, names[n] + '_pF')


  

  # Create a parameter object inside this model, set the required
  # attributes 'id' and 'constant' for a parameter in SBML Level 3, and
  # initialize the parameter with a value along with its units.

  k = model.createParameter()
  check(k,                                  'create parameter k')
  check(k.setId('k'),                       'set parameter k id')
  check(k.setConstant(True),                'set parameter k "constant"')
  check(k.setValue(1),                      'set parameter k value')
  check(k.setUnits('per_second'),           'set parameter k units')


  #############################################
  # Create ribosome position reactions 
  #############################################
  # Initiation 

  # Elongation
  for n in range(len(names)): 

    #create the #AA positions
    for p in range(int(lengthsofseq[n])):

      if isinstance(SingleAA[sequence[n][p]],basestring):
          riboPos_Elongation(model ,names[n] + '_p' + str(p),sequence[n][p],SingleAA[sequence[n][p]],1)
      else:
          i=1
          for id in SingleAA[sequence[n][p]]:
          #riboPos_Elongation(model,startingPos             ,AAadded       ,tRNA_needed,iterator):
            riboPos_Elongation(model ,names[n] + '_p' + str(p),sequence[n][p],id         ,i)
            i=i+1


  # Termination
 
  # And we're done creating the basic model.
  # Now return a text string containing the model in XML format.
 
  return writeSBMLToFile(document,'model1.xml')
 
 
if __name__ == '__main__':
  print(create_model(prot_names[0:2], ['3','1'], sequence[0:2])) # prot_len[0:2]
