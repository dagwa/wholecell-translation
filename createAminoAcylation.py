# misc data to integrate in to the code

# Enzymes/Complexes Composition Gene Name(s)
# Alanyl-tRNA synthetase (4) MG292 alaS
# Arginyl-tRNA synthetase (1) MG378 argS
# Aspartyl-tRNA synthetase (2) MG036 aspS
# Asparaginyl-tRNA synthetase (2) MG113 asnS
# Cysteinyl-tRNA synthetase (1) MG253 cysS
# Glutamyl-tRNA synthetase (1) MG462 gltX
# Glycyl-tRNA synthetase (2) MG251 glyS
# Histidyl-tRNA synthetase (2) MG035 hisS
# Isoleucyl-tRNA synthetase (1) MG345 ileS
# Leucyl-tRNA synthetase (1) MG266 leuS
# Lysyl-tRNA synthetase (2) MG136 lysS
# Methionyl-tRNA synthetase (2) MG021 metG
# Phenylalanyl-tRNA synthetase (2) MG194, (2) MG195 pheS, -
# Prolyl-tRNA synthetase (2) MG283 proS
# Seryl-tRNA synthetase (2) MG005 serS
# Threonyl-tRNA synthetase (2) MG375 thrS
# Tryptophanyl-tRNA synthetase (2) MG126 trpS
# Tyrosyl-tRNA synthetase (2) MG455 tyrS
# Valyl-tRNA synthetase (1) MG334 valS
# Glutamyl-tRNA(Gln) amidotransferase (1) MG098, (1) MG099, (1) MG100 -, -, gatB
# Methionyl-tRNA formyltransferase (1) MG365



# MG472_Aminoacylation
# MG475_Aminoacylation
# MG479_Aminoacylation
# MG483_Aminoacylation
# MG484_Aminoacylation
# MG485_Aminoacylation
# MG487_Aminoacylation
# MG487_Aminoacylation
# MG488_Aminoacylation
# MG488_Formyltransferase
# MG489_Aminoacylation
# MG490_Aminoacylation
# MG492_Aminoacylation
# MG493_Aminoacylation
# MG495_Aminoacylation
# MG496_Aminoacylation
# MG497_Aminoacylation
# MG499_Aminoacylation
# MG500_Aminoacylation
# MG501_Aminoacylation
# MG502_Amidotransferase
# MG502_Aminoacylation
# MG503_Aminoacylation
# MG504_Aminoacylation
# MG506_Aminoacylation
# MG507_Aminoacylation
# MG508_Aminoacylation
# MG509_Aminoacylation
# MG510_Aminoacylation
# MG511_Aminoacylation
# MG512_Aminoacylation
# MG513_Aminoacylation
# MG514_Aminoacylation
# MG518_Aminoacylation
# MG519_Aminoacylation
# MG520_Aminoacylation
# MG523_Aminoacylation
# MG_0004_Aminoacylation

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
    check(model.setExtentUnits("item"),       'set model units of extent')
    check(model.setSubstanceUnits('item'),    'set model substance units')

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
    check(c1.setSize(0.01),                   'set compartment "size"')
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


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG471 tRNA aminoacylation (Alanine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg471aminoacyl = model.createReaction()
    check(mg471aminoacyl,                                 'create reaction')
    check(mg471aminoacyl.setId('MG471_Aminoacylation'),                     'set reaction id')
    check(mg471aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg471aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg471aminoacylreact1 = mg471aminoacyl.createReactant()
    check(mg471aminoacylreact1,                       'create reactant')
    check(mg471aminoacylreact1.setSpecies('ALA'),      'assign reactant species')
    check(mg471aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg471aminoacylreact2 = mg471aminoacyl.createReactant()
    check(mg471aminoacylreact2,                       'create reactant')
    check(mg471aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg471aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg471aminoacylreact3 = mg471aminoacyl.createReactant()
    check(mg471aminoacylreact3,                       'create reactant')
    check(mg471aminoacylreact3.setSpecies('MG471'),      'assign reactant species')
    check(mg471aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg471aminoacylprod1 = mg471aminoacyl.createProduct()
    check(mg471aminoacylprod1,                       'create product')
    check(mg471aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg471aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg471aminoacylprod2 = mg471aminoacyl.createProduct()
    check(mg471aminoacylprod2,                       'create product')
    check(mg471aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg471aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg471aminoacylprod3 = mg471aminoacyl.createProduct()
    check(mg471aminoacylprod3,                       'create product')
    check(mg471aminoacylprod3.setSpecies('aminoacylated_MG471'),      'assign product species')
    check(mg471aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG472 tRNA aminoacylation (Isoleucine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg472aminoacyl = model.createReaction()
    check(mg472aminoacyl,                                 'create reaction')
    check(mg472aminoacyl.setId('MG472_Aminoacylation'),                     'set reaction id')
    check(mg472aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg472aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg472aminoacylreact1 = mg472aminoacyl.createReactant()
    check(mg472aminoacylreact1,                       'create reactant')
    check(mg472aminoacylreact1.setSpecies('ILE'),      'assign reactant species')
    check(mg472aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg472aminoacylreact2 = mg472aminoacyl.createReactant()
    check(mg472aminoacylreact2,                       'create reactant')
    check(mg472aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg472aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg472aminoacylreact3 = mg472aminoacyl.createReactant()
    check(mg472aminoacylreact3,                       'create reactant')
    check(mg472aminoacylreact3.setSpecies('MG472'),      'assign reactant species')
    check(mg472aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg472aminoacylprod1 = mg472aminoacyl.createProduct()
    check(mg472aminoacylprod1,                       'create product')
    check(mg472aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg472aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg472aminoacylprod2 = mg472aminoacyl.createProduct()
    check(mg472aminoacylprod2,                       'create product')
    check(mg472aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg472aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg472aminoacylprod3 = mg472aminoacyl.createProduct()
    check(mg472aminoacylprod3,                       'create product')
    check(mg472aminoacylprod3.setSpecies('aminoacylated_MG472'),      'assign product species')
    check(mg472aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG475 tRNA aminoacylation (Serine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg475aminoacyl = model.createReaction()
    check(mg475aminoacyl,                                 'create reaction')
    check(mg475aminoacyl.setId('MG475_Aminoacylation'),                     'set reaction id')
    check(mg475aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg475aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg475aminoacylreact1 = mg475aminoacyl.createReactant()
    check(mg475aminoacylreact1,                       'create reactant')
    check(mg475aminoacylreact1.setSpecies('SER'),      'assign reactant species')
    check(mg475aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg475aminoacylreact2 = mg475aminoacyl.createReactant()
    check(mg475aminoacylreact2,                       'create reactant')
    check(mg475aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg475aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg475aminoacylreact3 = mg475aminoacyl.createReactant()
    check(mg475aminoacylreact3,                       'create reactant')
    check(mg475aminoacylreact3.setSpecies('MG475'),      'assign reactant species')
    check(mg475aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg475aminoacylprod1 = mg475aminoacyl.createProduct()
    check(mg475aminoacylprod1,                       'create product')
    check(mg475aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg475aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg475aminoacylprod2 = mg475aminoacyl.createProduct()
    check(mg475aminoacylprod2,                       'create product')
    check(mg475aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg475aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg475aminoacylprod3 = mg475aminoacyl.createProduct()
    check(mg475aminoacylprod3,                       'create product')
    check(mg475aminoacylprod3.setSpecies('aminoacylated_MG475'),      'assign product species')
    check(mg475aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG479 tRNA aminoacylation (Threonine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg479aminoacyl = model.createReaction()
    check(mg479aminoacyl,                                 'create reaction')
    check(mg479aminoacyl.setId('MG479_Aminoacylation'),                     'set reaction id')
    check(mg479aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg479aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg479aminoacylreact1 = mg479aminoacyl.createReactant()
    check(mg479aminoacylreact1,                       'create reactant')
    check(mg479aminoacylreact1.setSpecies('SER'),      'assign reactant species')
    check(mg479aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg479aminoacylreact2 = mg479aminoacyl.createReactant()
    check(mg479aminoacylreact2,                       'create reactant')
    check(mg479aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg479aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg479aminoacylreact3 = mg479aminoacyl.createReactant()
    check(mg479aminoacylreact3,                       'create reactant')
    check(mg479aminoacylreact3.setSpecies('MG479'),      'assign reactant species')
    check(mg479aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg479aminoacylprod1 = mg479aminoacyl.createProduct()
    check(mg479aminoacylprod1,                       'create product')
    check(mg479aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg479aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg479aminoacylprod2 = mg479aminoacyl.createProduct()
    check(mg479aminoacylprod2,                       'create product')
    check(mg479aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg479aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg479aminoacylprod3 = mg479aminoacyl.createProduct()
    check(mg479aminoacylprod3,                       'create product')
    check(mg479aminoacylprod3.setSpecies('aminoacylated_MG479'),      'assign product species')
    check(mg479aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG483 tRNA aminoacylation (Cysteine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg483aminoacyl = model.createReaction()
    check(mg483aminoacyl,                                 'create reaction')
    check(mg483aminoacyl.setId('MG483_Aminoacylation'),                     'set reaction id')
    check(mg483aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg483aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg483aminoacylreact1 = mg483aminoacyl.createReactant()
    check(mg483aminoacylreact1,                       'create reactant')
    check(mg483aminoacylreact1.setSpecies('CYS'),      'assign reactant species')
    check(mg483aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg483aminoacylreact2 = mg483aminoacyl.createReactant()
    check(mg483aminoacylreact2,                       'create reactant')
    check(mg483aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg483aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg483aminoacylreact3 = mg483aminoacyl.createReactant()
    check(mg483aminoacylreact3,                       'create reactant')
    check(mg483aminoacylreact3.setSpecies('MG483'),      'assign reactant species')
    check(mg483aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg483aminoacylprod1 = mg483aminoacyl.createProduct()
    check(mg483aminoacylprod1,                       'create product')
    check(mg483aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg483aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg483aminoacylprod2 = mg483aminoacyl.createProduct()
    check(mg483aminoacylprod2,                       'create product')
    check(mg483aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg483aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg483aminoacylprod3 = mg483aminoacyl.createProduct()
    check(mg483aminoacylprod3,                       'create product')
    check(mg483aminoacylprod3.setSpecies('aminoacylated_MG483'),      'assign product species')
    check(mg483aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')



    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG484 tRNA aminoacylation (Proline)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg484aminoacyl = model.createReaction()
    check(mg484aminoacyl,                                 'create reaction')
    check(mg484aminoacyl.setId('MG484_Aminoacylation'),                     'set reaction id')
    check(mg484aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg484aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg484aminoacylreact1 = mg484aminoacyl.createReactant()
    check(mg484aminoacylreact1,                       'create reactant')
    check(mg484aminoacylreact1.setSpecies('PRO'),      'assign reactant species')
    check(mg484aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg484aminoacylreact2 = mg484aminoacyl.createReactant()
    check(mg484aminoacylreact2,                       'create reactant')
    check(mg484aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg484aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg484aminoacylreact3 = mg484aminoacyl.createReactant()
    check(mg484aminoacylreact3,                       'create reactant')
    check(mg484aminoacylreact3.setSpecies('MG484'),      'assign reactant species')
    check(mg484aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg484aminoacylprod1 = mg484aminoacyl.createProduct()
    check(mg484aminoacylprod1,                       'create product')
    check(mg484aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg484aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg484aminoacylprod2 = mg484aminoacyl.createProduct()
    check(mg484aminoacylprod2,                       'create product')
    check(mg484aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg484aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg484aminoacylprod3 = mg484aminoacyl.createProduct()
    check(mg484aminoacylprod3,                       'create product')
    check(mg484aminoacylprod3.setSpecies('aminoacylated_MG484'),      'assign product species')
    check(mg484aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG485 tRNA aminoacylation (Methionine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg485aminoacyl = model.createReaction()
    check(mg485aminoacyl,                                 'create reaction')
    check(mg485aminoacyl.setId('MG485_Aminoacylation'),                     'set reaction id')
    check(mg485aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg485aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg485aminoacylreact1 = mg485aminoacyl.createReactant()
    check(mg485aminoacylreact1,                       'create reactant')
    check(mg485aminoacylreact1.setSpecies('MET'),      'assign reactant species')
    check(mg485aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg485aminoacylreact2 = mg485aminoacyl.createReactant()
    check(mg485aminoacylreact2,                       'create reactant')
    check(mg485aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg485aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg485aminoacylreact3 = mg485aminoacyl.createReactant()
    check(mg485aminoacylreact3,                       'create reactant')
    check(mg485aminoacylreact3.setSpecies('MG485'),      'assign reactant species')
    check(mg485aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg485aminoacylprod1 = mg485aminoacyl.createProduct()
    check(mg485aminoacylprod1,                       'create product')
    check(mg485aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg485aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg485aminoacylprod2 = mg485aminoacyl.createProduct()
    check(mg485aminoacylprod2,                       'create product')
    check(mg485aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg485aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg485aminoacylprod3 = mg485aminoacyl.createProduct()
    check(mg485aminoacylprod3,                       'create product')
    check(mg485aminoacylprod3.setSpecies('aminoacylated_MG485'),      'assign product species')
    check(mg485aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG486 tRNA aminoacylation (Isoleucine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg486aminoacyl = model.createReaction()
    check(mg486aminoacyl,                                 'create reaction')
    check(mg486aminoacyl.setId('MG486_Aminoacylation'),                     'set reaction id')
    check(mg486aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg486aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg486aminoacylreact1 = mg486aminoacyl.createReactant()
    check(mg486aminoacylreact1,                       'create reactant')
    check(mg486aminoacylreact1.setSpecies('ILE'),      'assign reactant species')
    check(mg486aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg486aminoacylreact2 = mg486aminoacyl.createReactant()
    check(mg486aminoacylreact2,                       'create reactant')
    check(mg486aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg486aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg486aminoacylreact3 = mg486aminoacyl.createReactant()
    check(mg486aminoacylreact3,                       'create reactant')
    check(mg486aminoacylreact3.setSpecies('MG486'),      'assign reactant species')
    check(mg486aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg486aminoacylprod1 = mg486aminoacyl.createProduct()
    check(mg486aminoacylprod1,                       'create product')
    check(mg486aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg486aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg486aminoacylprod2 = mg486aminoacyl.createProduct()
    check(mg486aminoacylprod2,                       'create product')
    check(mg486aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg486aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg486aminoacylprod3 = mg486aminoacyl.createProduct()
    check(mg486aminoacylprod3,                       'create product')
    check(mg486aminoacylprod3.setSpecies('aminoacylated_MG486'),      'assign product species')
    check(mg486aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG487 tRNA aminoacylation (Serine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg487aminoacyl = model.createReaction()
    check(mg487aminoacyl,                                 'create reaction')
    check(mg487aminoacyl.setId('MG487_Aminoacylation'),                     'set reaction id')
    check(mg487aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg487aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg487aminoacylreact1 = mg487aminoacyl.createReactant()
    check(mg487aminoacylreact1,                       'create reactant')
    check(mg487aminoacylreact1.setSpecies('SER'),      'assign reactant species')
    check(mg487aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg487aminoacylreact2 = mg487aminoacyl.createReactant()
    check(mg487aminoacylreact2,                       'create reactant')
    check(mg487aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg487aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg487aminoacylreact3 = mg487aminoacyl.createReactant()
    check(mg487aminoacylreact3,                       'create reactant')
    check(mg487aminoacylreact3.setSpecies('MG487'),      'assign reactant species')
    check(mg487aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg487aminoacylprod1 = mg487aminoacyl.createProduct()
    check(mg487aminoacylprod1,                       'create product')
    check(mg487aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg487aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg487aminoacylprod2 = mg487aminoacyl.createProduct()
    check(mg487aminoacylprod2,                       'create product')
    check(mg487aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg487aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg487aminoacylprod3 = mg487aminoacyl.createProduct()
    check(mg487aminoacylprod3,                       'create product')
    check(mg487aminoacylprod3.setSpecies('aminoacylated_MG487'),      'assign product species')
    check(mg487aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG488 tRNA aminoacylation (formyl-Methionine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg488aminoacyl = model.createReaction()
    check(mg488aminoacyl,                                 'create reaction')
    check(mg488aminoacyl.setId('MG488_Aminoacylation'),                     'set reaction id')
    check(mg488aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg488aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg488aminoacylreact1 = mg488aminoacyl.createReactant()
    check(mg488aminoacylreact1,                       'create reactant')
    check(mg488aminoacylreact1.setSpecies('aminoacylated_MG485'),      'assign reactant species')
    check(mg488aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg488aminoacylreact2 = mg488aminoacyl.createReactant()
    check(mg488aminoacylreact2,                       'create reactant')
    check(mg488aminoacylreact2.setSpecies('FTHF10'),      'assign reactant species')
    check(mg488aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg488aminoacylreact3 = mg488aminoacyl.createReactant()
    check(mg488aminoacylreact3,                       'create reactant')
    check(mg488aminoacylreact3.setSpecies('H2O'),      'assign reactant species')
    check(mg488aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg488aminoacylprod1 = mg488aminoacyl.createProduct()
    check(mg488aminoacylprod1,                       'create product')
    check(mg488aminoacylprod1.setSpecies('THF'),      'assign product species')
    check(mg488aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    #To check: why is there no proton flying off here?

    #FIX FROM HERE
    mg488aminoacylprod2 = mg488aminoacyl.createProduct()
    check(mg488aminoacylprod2,                       'create product')
    check(mg488aminoacylprod2.setSpecies('aminoacylated_MG488'),      'assign product species')
    check(mg488aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG489 tRNA aminoacylation (Aspartic acid)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg489aminoacyl = model.createReaction()
    check(mg489aminoacyl,                                 'create reaction')
    check(mg489aminoacyl.setId('MG489_Aminoacylation'),                     'set reaction id')
    check(mg489aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg489aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg489aminoacylreact1 = mg489aminoacyl.createReactant()
    check(mg489aminoacylreact1,                       'create reactant')
    check(mg489aminoacylreact1.setSpecies('ASP'),      'assign reactant species')
    check(mg489aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg489aminoacylreact2 = mg489aminoacyl.createReactant()
    check(mg489aminoacylreact2,                       'create reactant')
    check(mg489aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg489aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg489aminoacylreact3 = mg489aminoacyl.createReactant()
    check(mg489aminoacylreact3,                       'create reactant')
    check(mg489aminoacylreact3.setSpecies('MG489'),      'assign reactant species')
    check(mg489aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg489aminoacylprod1 = mg489aminoacyl.createProduct()
    check(mg489aminoacylprod1,                       'create product')
    check(mg489aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg489aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg489aminoacylprod2 = mg489aminoacyl.createProduct()
    check(mg489aminoacylprod2,                       'create product')
    check(mg489aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg489aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg489aminoacylprod3 = mg489aminoacyl.createProduct()
    check(mg489aminoacylprod3,                       'create product')
    check(mg489aminoacylprod3.setSpecies('aminoacylated_MG489'),      'assign product species')
    check(mg489aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG490 tRNA aminoacylation (Phenylalanine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg490aminoacyl = model.createReaction()
    check(mg490aminoacyl,                                 'create reaction')
    check(mg490aminoacyl.setId('MG490_Aminoacylation'),                     'set reaction id')
    check(mg490aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg490aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg490aminoacylreact1 = mg490aminoacyl.createReactant()
    check(mg490aminoacylreact1,                       'create reactant')
    check(mg490aminoacylreact1.setSpecies('PHE'),      'assign reactant species')
    check(mg490aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg490aminoacylreact2 = mg490aminoacyl.createReactant()
    check(mg490aminoacylreact2,                       'create reactant')
    check(mg490aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg490aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg490aminoacylreact3 = mg490aminoacyl.createReactant()
    check(mg490aminoacylreact3,                       'create reactant')
    check(mg490aminoacylreact3.setSpecies('MG490'),      'assign reactant species')
    check(mg490aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg490aminoacylprod1 = mg490aminoacyl.createProduct()
    check(mg490aminoacylprod1,                       'create product')
    check(mg490aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg490aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg490aminoacylprod2 = mg490aminoacyl.createProduct()
    check(mg490aminoacylprod2,                       'create product')
    check(mg490aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg490aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg490aminoacylprod3 = mg490aminoacyl.createProduct()
    check(mg490aminoacylprod3,                       'create product')
    check(mg490aminoacylprod3.setSpecies('aminoacylated_MG490'),      'assign product species')
    check(mg490aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG492 tRNA aminoacylation (Arginine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg492aminoacyl = model.createReaction()
    check(mg492aminoacyl,                                 'create reaction')
    check(mg492aminoacyl.setId('MG492_Aminoacylation'),                     'set reaction id')
    check(mg492aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg492aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg492aminoacylreact1 = mg492aminoacyl.createReactant()
    check(mg492aminoacylreact1,                       'create reactant')
    check(mg492aminoacylreact1.setSpecies('ARG'),      'assign reactant species')
    check(mg492aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg492aminoacylreact2 = mg492aminoacyl.createReactant()
    check(mg492aminoacylreact2,                       'create reactant')
    check(mg492aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg492aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg492aminoacylreact3 = mg492aminoacyl.createReactant()
    check(mg492aminoacylreact3,                       'create reactant')
    check(mg492aminoacylreact3.setSpecies('MG492'),      'assign reactant species')
    check(mg492aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg492aminoacylprod1 = mg492aminoacyl.createProduct()
    check(mg492aminoacylprod1,                       'create product')
    check(mg492aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg492aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg492aminoacylprod2 = mg492aminoacyl.createProduct()
    check(mg492aminoacylprod2,                       'create product')
    check(mg492aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg492aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg492aminoacylprod3 = mg492aminoacyl.createProduct()
    check(mg492aminoacylprod3,                       'create product')
    check(mg492aminoacylprod3.setSpecies('aminoacylated_MG492'),      'assign product species')
    check(mg492aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG493 tRNA aminoacylation (Glycine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg493aminoacyl = model.createReaction()
    check(mg493aminoacyl,                                 'create reaction')
    check(mg493aminoacyl.setId('MG493_Aminoacylation'),                     'set reaction id')
    check(mg493aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg493aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg493aminoacylreact1 = mg493aminoacyl.createReactant()
    check(mg493aminoacylreact1,                       'create reactant')
    check(mg493aminoacylreact1.setSpecies('GLY'),      'assign reactant species')
    check(mg493aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg493aminoacylreact2 = mg493aminoacyl.createReactant()
    check(mg493aminoacylreact2,                       'create reactant')
    check(mg493aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg493aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg493aminoacylreact3 = mg493aminoacyl.createReactant()
    check(mg493aminoacylreact3,                       'create reactant')
    check(mg493aminoacylreact3.setSpecies('MG493'),      'assign reactant species')
    check(mg493aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg493aminoacylprod1 = mg493aminoacyl.createProduct()
    check(mg493aminoacylprod1,                       'create product')
    check(mg493aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg493aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg493aminoacylprod2 = mg493aminoacyl.createProduct()
    check(mg493aminoacylprod2,                       'create product')
    check(mg493aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg493aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg493aminoacylprod3 = mg493aminoacyl.createProduct()
    check(mg493aminoacylprod3,                       'create product')
    check(mg493aminoacylprod3.setSpecies('aminoacylated_MG493'),      'assign product species')
    check(mg493aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')


    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG495 tRNA aminoacylation (Arginine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg495aminoacyl = model.createReaction()
    check(mg495aminoacyl,                                 'create reaction')
    check(mg495aminoacyl.setId('MG495_Aminoacylation'),                     'set reaction id')
    check(mg495aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg495aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg495aminoacylreact1 = mg495aminoacyl.createReactant()
    check(mg495aminoacylreact1,                       'create reactant')
    check(mg495aminoacylreact1.setSpecies('ARG'),      'assign reactant species')
    check(mg495aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg495aminoacylreact2 = mg495aminoacyl.createReactant()
    check(mg495aminoacylreact2,                       'create reactant')
    check(mg495aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg495aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg495aminoacylreact3 = mg495aminoacyl.createReactant()
    check(mg495aminoacylreact3,                       'create reactant')
    check(mg495aminoacylreact3.setSpecies('MG495'),      'assign reactant species')
    check(mg495aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg495aminoacylprod1 = mg495aminoacyl.createProduct()
    check(mg495aminoacylprod1,                       'create product')
    check(mg495aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg495aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg495aminoacylprod2 = mg495aminoacyl.createProduct()
    check(mg495aminoacylprod2,                       'create product')
    check(mg495aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg495aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    #FIX FROM HERE
    mg495aminoacylprod3 = mg495aminoacyl.createProduct()
    check(mg495aminoacylprod3,                       'create product')
    check(mg495aminoacylprod3.setSpecies('aminoacylated_MG495'),      'assign product species')
    check(mg495aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = r1.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')



    # Now return a text string containing the model in XML format.

    return writeSBMLToString(document)

 
if __name__ == '__main__':
  print(create_model())
