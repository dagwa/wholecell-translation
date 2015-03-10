# Initialization Block



# Model builing Block


 import sys
 from libsbml import *
 
 
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
 
 
 def create_model():
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
   check(model.setExtentUnits("mole"),       'set model units of extent')
   check(model.setSubstanceUnits('mole'),    'set model substance units')
 
   # Create a unit definition we will need later.  Note that SBML Unit
   # objects must have all four attributes 'kind', 'exponent', 'scale'
   # and 'multiplier' defined.
 
   per_second = model.createUnitDefinition()
   check(per_second,                         'create unit definition')
   check(per_second.setId('per_second'),     'set unit definition id')
   unit = per_second.createUnit()
   check(unit,                               'create unit on per_second')
   check(unit.setKind(UNIT_KIND_SECOND),     'set unit kind')
   check(unit.setExponent(-1),               'set unit exponent')
   check(unit.setScale(0),                   'set unit scale')
   check(unit.setMultiplier(1),              'set unit multiplier')
 
   # Create a compartment inside this model, and set the required
   # attributes for an SBML compartment in SBML Level 3.
 
   c1 = model.createCompartment()
   check(c1,                                 'create compartment')
   check(c1.setId('c1'),                     'set compartment id')
   check(c1.setConstant(True),               'set compartment "constant"')
   check(c1.setSize(1),                      'set compartment "size"')
   check(c1.setSpatialDimensions(3),         'set compartment dimensions')
   check(c1.setUnits('litre'),               'set compartment size units')
 
   # Create two species inside this model, set the required attributes
   # for each species in SBML Level 3 (which are the 'id', 'compartment',
   # 'constant', 'hasOnlySubstanceUnits', and 'boundaryCondition'
   # attributes), and initialize the amount of the species along with the
   # units of the amount.
 
   s1 = model.createSpecies()
   check(s1,                                 'create species s1')
   check(s1.setId('s1'),                     'set species s1 id')
   check(s1.setCompartment('c1'),            'set species s1 compartment')
   check(s1.setConstant(False),              'set "constant" attribute on s1')
   check(s1.setInitialAmount(5),             'set initial amount for s1')
   check(s1.setSubstanceUnits('mole'),       'set substance units for s1')
   check(s1.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
   check(s1.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')
 
   s2 = model.createSpecies()
   check(s2,                                 'create species s2')
   check(s2.setId('s2'),                     'set species s2 id')
   check(s2.setCompartment('c1'),            'set species s2 compartment')
   check(s2.setConstant(False),              'set "constant" attribute on s2')
   check(s2.setInitialAmount(0),             'set initial amount for s2')
   check(s2.setSubstanceUnits('mole'),       'set substance units for s2')
   check(s2.setBoundaryCondition(False),     'set "boundaryCondition" on s2')
   check(s2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s2')
 
   # Create a parameter object inside this model, set the required
   # attributes 'id' and 'constant' for a parameter in SBML Level 3, and
   # initialize the parameter with a value along with its units.
 
   k = model.createParameter()
   check(k,                                  'create parameter k')
   check(k.setId('k'),                       'set parameter k id')
   check(k.setConstant(True),                'set parameter k "constant"')
   check(k.setValue(1),                      'set parameter k value')
   check(k.setUnits('per_second'),           'set parameter k units')
 
   # Create a reaction inside this model, set the reactants and products,
   # and set the reaction rate expression (the SBML "kinetic law").  We
   # set the minimum required attributes for all of these objects.  The
   # units of the reaction rate are determined from the 'timeUnits' and
   # 'extentUnits' attributes on the Model object.
 
   r1 = model.createReaction()
   check(r1,                                 'create reaction')
   check(r1.setId('r1'),                     'set reaction id')
   check(r1.setReversible(False),            'set reaction reversibility flag')
   check(r1.setFast(False),                  'set reaction "fast" attribute')
 
   species_ref1 = r1.createReactant()
   check(species_ref1,                       'create reactant')
   check(species_ref1.setSpecies('s1'),      'assign reactant species')
   check(species_ref1.setConstant(True),     'set "constant" on species ref 1')
 
   species_ref2 = r1.createProduct()
   check(species_ref2,                       'create product')
   check(species_ref2.setSpecies('s2'),      'assign product species')
   check(species_ref2.setConstant(True),     'set "constant" on species ref 2')
 
   math_ast = parseL3Formula('k * s1 * c1')
   check(math_ast,                           'create AST for rate expression')
 
   kinetic_law = r1.createKineticLaw()
   check(kinetic_law,                        'create kinetic law')
   check(kinetic_law.setMath(math_ast),      'set math on kinetic law')
 
   # And we're done creating the basic model.
   # Now return a text string containing the model in XML format.
 
   return writeSBMLToString(document)
 
 
 if __name__ == '__main__':
   print(create_model())