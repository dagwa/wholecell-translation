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

# MG_0004_Aminoacylation

# Initialization Block
import sys
# import libsbml
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


# Model building Block
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

    # FIX FROM HERE
    mg471aminoacylprod3 = mg471aminoacyl.createProduct()
    check(mg471aminoacylprod3,                       'create product')
    check(mg471aminoacylprod3.setSpecies('aminoacylated_MG471'),      'assign product species')
    check(mg471aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg471aminoacyl.createKineticLaw()
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

    # FIX FROM HERE
    mg472aminoacylprod3 = mg472aminoacyl.createProduct()
    check(mg472aminoacylprod3,                       'create product')
    check(mg472aminoacylprod3.setSpecies('aminoacylated_MG472'),      'assign product species')
    check(mg472aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg472aminoacyl.createKineticLaw()
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

    # FIX FROM HERE
    mg475aminoacylprod3 = mg475aminoacyl.createProduct()
    check(mg475aminoacylprod3,                       'create product')
    check(mg475aminoacylprod3.setSpecies('aminoacylated_MG475'),      'assign product species')
    check(mg475aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg475aminoacyl.createKineticLaw()
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

    # FIX FROM HERE
    mg479aminoacylprod3 = mg479aminoacyl.createProduct()
    check(mg479aminoacylprod3,                       'create product')
    check(mg479aminoacylprod3.setSpecies('aminoacylated_MG479'),      'assign product species')
    check(mg479aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg479aminoacyl.createKineticLaw()
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

    # FIX FROM HERE
    mg483aminoacylprod3 = mg483aminoacyl.createProduct()
    check(mg483aminoacylprod3,                       'create product')
    check(mg483aminoacylprod3.setSpecies('aminoacylated_MG483'),      'assign product species')
    check(mg483aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg483aminoacyl.createKineticLaw()
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

    # FIX FROM HERE
    mg484aminoacylprod3 = mg484aminoacyl.createProduct()
    check(mg484aminoacylprod3,                       'create product')
    check(mg484aminoacylprod3.setSpecies('aminoacylated_MG484'),      'assign product species')
    check(mg484aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg484aminoacyl.createKineticLaw()
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

    # FIX FROM HERE
    mg485aminoacylprod3 = mg485aminoacyl.createProduct()
    check(mg485aminoacylprod3,                       'create product')
    check(mg485aminoacylprod3.setSpecies('aminoacylated_MG485'),      'assign product species')
    check(mg485aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg485aminoacyl.createKineticLaw()
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

    # FIX FROM HERE
    mg486aminoacylprod3 = mg486aminoacyl.createProduct()
    check(mg486aminoacylprod3,                       'create product')
    check(mg486aminoacylprod3.setSpecies('aminoacylated_MG486'),      'assign product species')
    check(mg486aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg486aminoacyl.createKineticLaw()
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

    # FIX FROM HERE
    mg487aminoacylprod3 = mg487aminoacyl.createProduct()
    check(mg487aminoacylprod3,                       'create product')
    check(mg487aminoacylprod3.setSpecies('aminoacylated_MG487'),      'assign product species')
    check(mg487aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg487aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG488 tRNA aminoacylation (formyl-Methionine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # A methionylformyltransferase is used to add the formyl group on to the methionine on tRNA MG488

    # first, model the methionine aminoacylation of MG488
    mg488aminoacyl = model.createReaction()
    check(mg488aminoacyl,                                 'create reaction')
    check(mg488aminoacyl.setId('MG488_Aminoacylation'),                     'set reaction id')
    check(mg488aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg488aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg488aminoacylreact1 = mg488aminoacyl.createReactant()
    check(mg488aminoacylreact1,                       'create reactant')
    check(mg488aminoacylreact1.setSpecies('MET'),      'assign reactant species')
    check(mg488aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg488aminoacylreact2 = mg488aminoacyl.createReactant()
    check(mg488aminoacylreact2,                       'create reactant')
    check(mg488aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg488aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg488aminoacylreact3 = mg488aminoacyl.createReactant()
    check(mg488aminoacylreact3,                       'create reactant')
    check(mg488aminoacylreact3.setSpecies('MG488'),      'assign reactant species')
    check(mg488aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg488aminoacylprod1 = mg488aminoacyl.createProduct()
    check(mg488aminoacylprod1,                       'create product')
    check(mg488aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg488aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg488aminoacylprod2 = mg488aminoacyl.createProduct()
    check(mg488aminoacylprod2,                       'create product')
    check(mg488aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg488aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg488aminoacylprod3 = mg488aminoacyl.createProduct()
    check(mg488aminoacylprod3,                       'create product')
    check(mg488aminoacylprod3.setSpecies('met_aminoacylated_MG488'),      'assign product species')
    check(mg488aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg488aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    # next, model the methionylformyltransferase catalysed reaction
    mg488methtrans = model.createReaction()
    check(mg488methtrans,                                 'create reaction')
    check(mg488methtrans.setId('MG488_Formyltransferase'),                     'set reaction id')
    check(mg488methtrans.setReversible(False),            'set reaction reversibility flag')
    check(mg488methtrans.setFast(False),                  'set reaction "fast" attribute')

    mg488methtransreact1 = mg488methtrans.createReactant()
    check(mg488methtransreact1,                       'create reactant')
    check(mg488methtransreact1.setSpecies('met_aminoacylated_MG488'),      'assign reactant species')
    check(mg488methtransreact1.setConstant(False),     'set "constant" on species ref 1')

    mg488methtransreact2 = mg488methtrans.createReactant()
    check(mg488methtransreact2,                       'create reactant')
    check(mg488methtransreact2.setSpecies('FTHF10'),      'assign reactant species')
    check(mg488methtransreact2.setConstant(False),     'set "constant" on species ref 1')

    mg488methtransreact3 = mg488methtrans.createReactant()
    check(mg488methtransreact3,                       'create reactant')
    check(mg488methtransreact3.setSpecies('H2O'),      'assign reactant species')
    check(mg488methtransreact3.setConstant(False),     'set "constant" on species ref 1')

    mg488methtransprod1 = mg488methtrans.createProduct()
    check(mg488methtransprod1,                       'create product')
    check(mg488methtransprod1.setSpecies('THF'),      'assign product species')
    check(mg488methtransprod1.setConstant(False),     'set "constant" on species ref 2')

    # FIX: why is there no proton flying off here?

    # FIX FROM HERE
    mg488methtransprod2 = mg488methtrans.createProduct()
    check(mg488methtransprod2,                       'create product')
    check(mg488methtransprod2.setSpecies('aminoacylated_MG488'),      'assign product species')
    check(mg488methtransprod2.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg488methtrans.createKineticLaw()
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

    # FIX FROM HERE
    mg489aminoacylprod3 = mg489aminoacyl.createProduct()
    check(mg489aminoacylprod3,                       'create product')
    check(mg489aminoacylprod3.setSpecies('aminoacylated_MG489'),      'assign product species')
    check(mg489aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg489aminoacyl.createKineticLaw()
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

    # FIX FROM HERE
    mg490aminoacylprod3 = mg490aminoacyl.createProduct()
    check(mg490aminoacylprod3,                       'create product')
    check(mg490aminoacylprod3.setSpecies('aminoacylated_MG490'),      'assign product species')
    check(mg490aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg490aminoacyl.createKineticLaw()
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

    # FIX FROM HERE
    mg492aminoacylprod3 = mg492aminoacyl.createProduct()
    check(mg492aminoacylprod3,                       'create product')
    check(mg492aminoacylprod3.setSpecies('aminoacylated_MG492'),      'assign product species')
    check(mg492aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg492aminoacyl.createKineticLaw()
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

    # FIX FROM HERE
    mg493aminoacylprod3 = mg493aminoacyl.createProduct()
    check(mg493aminoacylprod3,                       'create product')
    check(mg493aminoacylprod3.setSpecies('aminoacylated_MG493'),      'assign product species')
    check(mg493aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg493aminoacyl.createKineticLaw()
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

    # FIX FROM HERE
    mg495aminoacylprod3 = mg495aminoacyl.createProduct()
    check(mg495aminoacylprod3,                       'create product')
    check(mg495aminoacylprod3.setSpecies('aminoacylated_MG495'),      'assign product species')
    check(mg495aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg495aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG496 tRNA aminoacylation (Tryptophan)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg496aminoacyl = model.createReaction()
    check(mg496aminoacyl,                                 'create reaction')
    check(mg496aminoacyl.setId('MG496_Aminoacylation'),                     'set reaction id')
    check(mg496aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg496aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg496aminoacylreact1 = mg496aminoacyl.createReactant()
    check(mg496aminoacylreact1,                       'create reactant')
    check(mg496aminoacylreact1.setSpecies('TRP'),      'assign reactant species')
    check(mg496aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg496aminoacylreact2 = mg496aminoacyl.createReactant()
    check(mg496aminoacylreact2,                       'create reactant')
    check(mg496aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg496aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg496aminoacylreact3 = mg496aminoacyl.createReactant()
    check(mg496aminoacylreact3,                       'create reactant')
    check(mg496aminoacylreact3.setSpecies('MG496'),      'assign reactant species')
    check(mg496aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg496aminoacylprod1 = mg496aminoacyl.createProduct()
    check(mg496aminoacylprod1,                       'create product')
    check(mg496aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg496aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg496aminoacylprod2 = mg496aminoacyl.createProduct()
    check(mg496aminoacylprod2,                       'create product')
    check(mg496aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg496aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg496aminoacylprod3 = mg496aminoacyl.createProduct()
    check(mg496aminoacylprod3,                       'create product')
    check(mg496aminoacylprod3.setSpecies('aminoacylated_MG496'),      'assign product species')
    check(mg496aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg496aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG497 tRNA aminoacylation (Arginine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg497aminoacyl = model.createReaction()
    check(mg497aminoacyl,                                 'create reaction')
    check(mg497aminoacyl.setId('MG497_Aminoacylation'),                     'set reaction id')
    check(mg497aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg497aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg497aminoacylreact1 = mg497aminoacyl.createReactant()
    check(mg497aminoacylreact1,                       'create reactant')
    check(mg497aminoacylreact1.setSpecies('ARG'),      'assign reactant species')
    check(mg497aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg497aminoacylreact2 = mg497aminoacyl.createReactant()
    check(mg497aminoacylreact2,                       'create reactant')
    check(mg497aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg497aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg497aminoacylreact3 = mg497aminoacyl.createReactant()
    check(mg497aminoacylreact3,                       'create reactant')
    check(mg497aminoacylreact3.setSpecies('MG497'),      'assign reactant species')
    check(mg497aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg497aminoacylprod1 = mg497aminoacyl.createProduct()
    check(mg497aminoacylprod1,                       'create product')
    check(mg497aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg497aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg497aminoacylprod2 = mg497aminoacyl.createProduct()
    check(mg497aminoacylprod2,                       'create product')
    check(mg497aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg497aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg497aminoacylprod3 = mg497aminoacyl.createProduct()
    check(mg497aminoacylprod3,                       'create product')
    check(mg497aminoacylprod3.setSpecies('aminoacylated_MG497'),      'assign product species')
    check(mg497aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg497aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG499 tRNA aminoacylation (Glycine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg499aminoacyl = model.createReaction()
    check(mg499aminoacyl,                                 'create reaction')
    check(mg499aminoacyl.setId('MG499_Aminoacylation'),                     'set reaction id')
    check(mg499aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg499aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg499aminoacylreact1 = mg499aminoacyl.createReactant()
    check(mg499aminoacylreact1,                       'create reactant')
    check(mg499aminoacylreact1.setSpecies('GLY'),      'assign reactant species')
    check(mg499aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg499aminoacylreact2 = mg499aminoacyl.createReactant()
    check(mg499aminoacylreact2,                       'create reactant')
    check(mg499aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg499aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg499aminoacylreact3 = mg499aminoacyl.createReactant()
    check(mg499aminoacylreact3,                       'create reactant')
    check(mg499aminoacylreact3.setSpecies('MG499'),      'assign reactant species')
    check(mg499aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg499aminoacylprod1 = mg499aminoacyl.createProduct()
    check(mg499aminoacylprod1,                       'create product')
    check(mg499aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg499aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg499aminoacylprod2 = mg499aminoacyl.createProduct()
    check(mg499aminoacylprod2,                       'create product')
    check(mg499aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg499aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg499aminoacylprod3 = mg499aminoacyl.createProduct()
    check(mg499aminoacylprod3,                       'create product')
    check(mg499aminoacylprod3.setSpecies('aminoacylated_MG499'),      'assign product species')
    check(mg499aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg499aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG500 tRNA aminoacylation (Leucine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg500aminoacyl = model.createReaction()
    check(mg500aminoacyl,                                 'create reaction')
    check(mg500aminoacyl.setId('MG500_Aminoacylation'),                     'set reaction id')
    check(mg500aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg500aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg500aminoacylreact1 = mg500aminoacyl.createReactant()
    check(mg500aminoacylreact1,                       'create reactant')
    check(mg500aminoacylreact1.setSpecies('LEU'),      'assign reactant species')
    check(mg500aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg500aminoacylreact2 = mg500aminoacyl.createReactant()
    check(mg500aminoacylreact2,                       'create reactant')
    check(mg500aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg500aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg500aminoacylreact3 = mg500aminoacyl.createReactant()
    check(mg500aminoacylreact3,                       'create reactant')
    check(mg500aminoacylreact3.setSpecies('MG500'),      'assign reactant species')
    check(mg500aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg500aminoacylprod1 = mg500aminoacyl.createProduct()
    check(mg500aminoacylprod1,                       'create product')
    check(mg500aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg500aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg500aminoacylprod2 = mg500aminoacyl.createProduct()
    check(mg500aminoacylprod2,                       'create product')
    check(mg500aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg500aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg500aminoacylprod3 = mg500aminoacyl.createProduct()
    check(mg500aminoacylprod3,                       'create product')
    check(mg500aminoacylprod3.setSpecies('aminoacylated_MG500'),      'assign product species')
    check(mg500aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg500aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG501 tRNA aminoacylation (Lysine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg501aminoacyl = model.createReaction()
    check(mg501aminoacyl,                                 'create reaction')
    check(mg501aminoacyl.setId('MG501_Aminoacylation'),                     'set reaction id')
    check(mg501aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg501aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg501aminoacylreact1 = mg501aminoacyl.createReactant()
    check(mg501aminoacylreact1,                       'create reactant')
    check(mg501aminoacylreact1.setSpecies('LYS'),      'assign reactant species')
    check(mg501aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg501aminoacylreact2 = mg501aminoacyl.createReactant()
    check(mg501aminoacylreact2,                       'create reactant')
    check(mg501aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg501aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg501aminoacylreact3 = mg501aminoacyl.createReactant()
    check(mg501aminoacylreact3,                       'create reactant')
    check(mg501aminoacylreact3.setSpecies('MG501'),      'assign reactant species')
    check(mg501aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg501aminoacylprod1 = mg501aminoacyl.createProduct()
    check(mg501aminoacylprod1,                       'create product')
    check(mg501aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg501aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg501aminoacylprod2 = mg501aminoacyl.createProduct()
    check(mg501aminoacylprod2,                       'create product')
    check(mg501aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg501aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg501aminoacylprod3 = mg501aminoacyl.createProduct()
    check(mg501aminoacylprod3,                       'create product')
    check(mg501aminoacylprod3.setSpecies('aminoacylated_MG501'),      'assign product species')
    check(mg501aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg501aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG502 tRNA aminoacylation (Glutamine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # from SuppInfo1.pdf, pp. 105: "Since there is no glutaminyl-tRNA synthase (to add a glutamine to a tRNA),
    #    glutamyl-tRNA synthase first adds a glutamate to tRNA MG502 and then Glu-tRNA amidotransferase converts
    #    the glutamate into a glutamine.
    # first, model the glutamyl tRNA synthase reaction
    mg502aminoacyl = model.createReaction()
    check(mg502aminoacyl,                                 'create reaction')
    check(mg502aminoacyl.setId('MG502_Aminoacylation'),                     'set reaction id')
    check(mg502aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg502aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg502aminoacylreact1 = mg502aminoacyl.createReactant()
    check(mg502aminoacylreact1,                       'create reactant')
    check(mg502aminoacylreact1.setSpecies('GLU'),      'assign reactant species')
    check(mg502aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg502aminoacylreact2 = mg502aminoacyl.createReactant()
    check(mg502aminoacylreact2,                       'create reactant')
    check(mg502aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg502aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg502aminoacylreact3 = mg502aminoacyl.createReactant()
    check(mg502aminoacylreact3,                       'create reactant')
    check(mg502aminoacylreact3.setSpecies('MG502'),      'assign reactant species')
    check(mg502aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg502aminoacylprod1 = mg502aminoacyl.createProduct()
    check(mg502aminoacylprod1,                       'create product')
    check(mg502aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg502aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg502aminoacylprod2 = mg502aminoacyl.createProduct()
    check(mg502aminoacylprod2,                       'create product')
    check(mg502aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg502aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg502aminoacylprod3 = mg502aminoacyl.createProduct()
    check(mg502aminoacylprod3,                       'create product')
    check(mg502aminoacylprod3.setSpecies('GLU_aminoacylated_MG502'),      'assign product species')
    check(mg502aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg502aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    # next, model the Glu-tRNA amidotransferase reaction
    mg502amidotrans = model.createReaction()
    check(mg502amidotrans,                                 'create reaction')
    check(mg502amidotrans.setId('MG502_Amidotransferase'),                     'set reaction id')
    check(mg502amidotrans.setReversible(False),            'set reaction reversibility flag')
    check(mg502amidotrans.setFast(False),                  'set reaction "fast" attribute')

    mg502amidotransreact1 = mg502amidotrans.createReactant()
    check(mg502amidotransreact1,                       'create reactant')
    check(mg502amidotransreact1.setSpecies('GLU_aminoacylated_MG502'),      'assign reactant species')
    check(mg502amidotransreact1.setConstant(False),     'set "constant" on species ref 1')

    mg502amidotransreact2 = mg502amidotrans.createReactant()
    check(mg502amidotransreact2,                       'create reactant')
    check(mg502amidotransreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg502amidotransreact2.setConstant(False),     'set "constant" on species ref 1')

    mg502amidotransreact3 = mg502amidotrans.createReactant()
    check(mg502amidotransreact3,                       'create reactant')
    check(mg502amidotransreact3.setSpecies('GLN'),      'assign reactant species')
    check(mg502amidotransreact3.setConstant(False),     'set "constant" on species ref 1')

    mg502amidotransprod1 = mg502amidotrans.createProduct()
    check(mg502amidotransprod1,                       'create product')
    check(mg502amidotransprod1.setSpecies('ADP'),      'assign product species')
    check(mg502amidotransprod1.setConstant(False),     'set "constant" on species ref 2')

    mg502amidotransprod2 = mg502amidotrans.createProduct()
    check(mg502amidotransprod2,                       'create product')
    check(mg502amidotransprod2.setSpecies('PI'),      'assign product species')
    check(mg502amidotransprod2.setConstant(False),     'set "constant" on species ref 2')

    mg502amidotransprod3 = mg502amidotrans.createProduct()
    check(mg502amidotransprod3,                       'create product')
    check(mg502amidotransprod3.setSpecies('GLU'),      'assign product species')
    check(mg502amidotransprod3.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg502amidotransprod4 = mg502amidotrans.createProduct()
    check(mg502amidotransprod4,                       'create product')
    check(mg502amidotransprod4.setSpecies('aminoacylated_MG502'),      'assign product species')
    check(mg502amidotransprod4.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg502amidotrans.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG503 tRNA aminoacylation (Tyrosine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg503aminoacyl = model.createReaction()
    check(mg503aminoacyl,                                 'create reaction')
    check(mg503aminoacyl.setId('MG503_Aminoacylation'),                     'set reaction id')
    check(mg503aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg503aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg503aminoacylreact1 = mg503aminoacyl.createReactant()
    check(mg503aminoacylreact1,                       'create reactant')
    check(mg503aminoacylreact1.setSpecies('TYR'),      'assign reactant species')
    check(mg503aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg503aminoacylreact2 = mg503aminoacyl.createReactant()
    check(mg503aminoacylreact2,                       'create reactant')
    check(mg503aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg503aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg503aminoacylreact3 = mg503aminoacyl.createReactant()
    check(mg503aminoacylreact3,                       'create reactant')
    check(mg503aminoacylreact3.setSpecies('MG503'),      'assign reactant species')
    check(mg503aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg503aminoacylprod1 = mg503aminoacyl.createProduct()
    check(mg503aminoacylprod1,                       'create product')
    check(mg503aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg503aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg503aminoacylprod2 = mg503aminoacyl.createProduct()
    check(mg503aminoacylprod2,                       'create product')
    check(mg503aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg503aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg503aminoacylprod3 = mg503aminoacyl.createProduct()
    check(mg503aminoacylprod3,                       'create product')
    check(mg503aminoacylprod3.setSpecies('aminoacylated_MG503'),      'assign product species')
    check(mg503aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg503aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG504 tRNA aminoacylation (Tryptophan)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg504aminoacyl = model.createReaction()
    check(mg504aminoacyl,                                 'create reaction')
    check(mg504aminoacyl.setId('MG504_Aminoacylation'),                     'set reaction id')
    check(mg504aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg504aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg504aminoacylreact1 = mg504aminoacyl.createReactant()
    check(mg504aminoacylreact1,                       'create reactant')
    check(mg504aminoacylreact1.setSpecies('TRP'),      'assign reactant species')
    check(mg504aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg504aminoacylreact2 = mg504aminoacyl.createReactant()
    check(mg504aminoacylreact2,                       'create reactant')
    check(mg504aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg504aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg504aminoacylreact3 = mg504aminoacyl.createReactant()
    check(mg504aminoacylreact3,                       'create reactant')
    check(mg504aminoacylreact3.setSpecies('MG504'),      'assign reactant species')
    check(mg504aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg504aminoacylprod1 = mg504aminoacyl.createProduct()
    check(mg504aminoacylprod1,                       'create product')
    check(mg504aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg504aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg504aminoacylprod2 = mg504aminoacyl.createProduct()
    check(mg504aminoacylprod2,                       'create product')
    check(mg504aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg504aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg504aminoacylprod3 = mg504aminoacyl.createProduct()
    check(mg504aminoacylprod3,                       'create product')
    check(mg504aminoacylprod3.setSpecies('aminoacylated_MG504'),      'assign product species')
    check(mg504aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg504aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG506 tRNA aminoacylation (Serine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg506aminoacyl = model.createReaction()
    check(mg506aminoacyl,                                 'create reaction')
    check(mg506aminoacyl.setId('MG506_Aminoacylation'),                     'set reaction id')
    check(mg506aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg506aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg506aminoacylreact1 = mg506aminoacyl.createReactant()
    check(mg506aminoacylreact1,                       'create reactant')
    check(mg506aminoacylreact1.setSpecies('SER'),      'assign reactant species')
    check(mg506aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg506aminoacylreact2 = mg506aminoacyl.createReactant()
    check(mg506aminoacylreact2,                       'create reactant')
    check(mg506aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg506aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg506aminoacylreact3 = mg506aminoacyl.createReactant()
    check(mg506aminoacylreact3,                       'create reactant')
    check(mg506aminoacylreact3.setSpecies('MG506'),      'assign reactant species')
    check(mg506aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg506aminoacylprod1 = mg506aminoacyl.createProduct()
    check(mg506aminoacylprod1,                       'create product')
    check(mg506aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg506aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg506aminoacylprod2 = mg506aminoacyl.createProduct()
    check(mg506aminoacylprod2,                       'create product')
    check(mg506aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg506aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg506aminoacylprod3 = mg506aminoacyl.createProduct()
    check(mg506aminoacylprod3,                       'create product')
    check(mg506aminoacylprod3.setSpecies('aminoacylated_MG506'),      'assign product species')
    check(mg506aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg506aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG507 tRNA aminoacylation (Serine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg507aminoacyl = model.createReaction()
    check(mg507aminoacyl,                                 'create reaction')
    check(mg507aminoacyl.setId('MG507_Aminoacylation'),                     'set reaction id')
    check(mg507aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg507aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg507aminoacylreact1 = mg507aminoacyl.createReactant()
    check(mg507aminoacylreact1,                       'create reactant')
    check(mg507aminoacylreact1.setSpecies('SER'),      'assign reactant species')
    check(mg507aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg507aminoacylreact2 = mg507aminoacyl.createReactant()
    check(mg507aminoacylreact2,                       'create reactant')
    check(mg507aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg507aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg507aminoacylreact3 = mg507aminoacyl.createReactant()
    check(mg507aminoacylreact3,                       'create reactant')
    check(mg507aminoacylreact3.setSpecies('MG507'),      'assign reactant species')
    check(mg507aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg507aminoacylprod1 = mg507aminoacyl.createProduct()
    check(mg507aminoacylprod1,                       'create product')
    check(mg507aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg507aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg507aminoacylprod2 = mg507aminoacyl.createProduct()
    check(mg507aminoacylprod2,                       'create product')
    check(mg507aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg507aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg507aminoacylprod3 = mg507aminoacyl.createProduct()
    check(mg507aminoacylprod3,                       'create product')
    check(mg507aminoacylprod3.setSpecies('aminoacylated_MG507'),      'assign product species')
    check(mg507aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg507aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG508 tRNA aminoacylation (Leucine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg508aminoacyl = model.createReaction()
    check(mg508aminoacyl,                                 'create reaction')
    check(mg508aminoacyl.setId('MG508_Aminoacylation'),                     'set reaction id')
    check(mg508aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg508aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg508aminoacylreact1 = mg508aminoacyl.createReactant()
    check(mg508aminoacylreact1,                       'create reactant')
    check(mg508aminoacylreact1.setSpecies('LEU'),      'assign reactant species')
    check(mg508aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg508aminoacylreact2 = mg508aminoacyl.createReactant()
    check(mg508aminoacylreact2,                       'create reactant')
    check(mg508aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg508aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg508aminoacylreact3 = mg508aminoacyl.createReactant()
    check(mg508aminoacylreact3,                       'create reactant')
    check(mg508aminoacylreact3.setSpecies('MG508'),      'assign reactant species')
    check(mg508aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg508aminoacylprod1 = mg508aminoacyl.createProduct()
    check(mg508aminoacylprod1,                       'create product')
    check(mg508aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg508aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg508aminoacylprod2 = mg508aminoacyl.createProduct()
    check(mg508aminoacylprod2,                       'create product')
    check(mg508aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg508aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg508aminoacylprod3 = mg508aminoacyl.createProduct()
    check(mg508aminoacylprod3,                       'create product')
    check(mg508aminoacylprod3.setSpecies('aminoacylated_MG508'),      'assign product species')
    check(mg508aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg508aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG509 tRNA aminoacylation (Lysine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg509aminoacyl = model.createReaction()
    check(mg509aminoacyl,                                 'create reaction')
    check(mg509aminoacyl.setId('MG509_Aminoacylation'),                     'set reaction id')
    check(mg509aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg509aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg509aminoacylreact1 = mg509aminoacyl.createReactant()
    check(mg509aminoacylreact1,                       'create reactant')
    check(mg509aminoacylreact1.setSpecies('LYS'),      'assign reactant species')
    check(mg509aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg509aminoacylreact2 = mg509aminoacyl.createReactant()
    check(mg509aminoacylreact2,                       'create reactant')
    check(mg509aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg509aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg509aminoacylreact3 = mg509aminoacyl.createReactant()
    check(mg509aminoacylreact3,                       'create reactant')
    check(mg509aminoacylreact3.setSpecies('MG509'),      'assign reactant species')
    check(mg509aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg509aminoacylprod1 = mg509aminoacyl.createProduct()
    check(mg509aminoacylprod1,                       'create product')
    check(mg509aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg509aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg509aminoacylprod2 = mg509aminoacyl.createProduct()
    check(mg509aminoacylprod2,                       'create product')
    check(mg509aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg509aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg509aminoacylprod3 = mg509aminoacyl.createProduct()
    check(mg509aminoacylprod3,                       'create product')
    check(mg509aminoacylprod3.setSpecies('aminoacylated_MG509'),      'assign product species')
    check(mg509aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg509aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG510 tRNA aminoacylation (Threonine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg510aminoacyl = model.createReaction()
    check(mg510aminoacyl,                                 'create reaction')
    check(mg510aminoacyl.setId('MG510_Aminoacylation'),                     'set reaction id')
    check(mg510aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg510aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg510aminoacylreact1 = mg510aminoacyl.createReactant()
    check(mg510aminoacylreact1,                       'create reactant')
    check(mg510aminoacylreact1.setSpecies('THR'),      'assign reactant species')
    check(mg510aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg510aminoacylreact2 = mg510aminoacyl.createReactant()
    check(mg510aminoacylreact2,                       'create reactant')
    check(mg510aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg510aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg510aminoacylreact3 = mg510aminoacyl.createReactant()
    check(mg510aminoacylreact3,                       'create reactant')
    check(mg510aminoacylreact3.setSpecies('MG510'),      'assign reactant species')
    check(mg510aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg510aminoacylprod1 = mg510aminoacyl.createProduct()
    check(mg510aminoacylprod1,                       'create product')
    check(mg510aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg510aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg510aminoacylprod2 = mg510aminoacyl.createProduct()
    check(mg510aminoacylprod2,                       'create product')
    check(mg510aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg510aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg510aminoacylprod3 = mg510aminoacyl.createProduct()
    check(mg510aminoacylprod3,                       'create product')
    check(mg510aminoacylprod3.setSpecies('aminoacylated_MG510'),      'assign product species')
    check(mg510aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg510aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG511 tRNA aminoacylation (Valine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg511aminoacyl = model.createReaction()
    check(mg511aminoacyl,                                 'create reaction')
    check(mg511aminoacyl.setId('MG511_Aminoacylation'),                     'set reaction id')
    check(mg511aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg511aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg511aminoacylreact1 = mg511aminoacyl.createReactant()
    check(mg511aminoacylreact1,                       'create reactant')
    check(mg511aminoacylreact1.setSpecies('VAL'),      'assign reactant species')
    check(mg511aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg511aminoacylreact2 = mg511aminoacyl.createReactant()
    check(mg511aminoacylreact2,                       'create reactant')
    check(mg511aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg511aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg511aminoacylreact3 = mg511aminoacyl.createReactant()
    check(mg511aminoacylreact3,                       'create reactant')
    check(mg511aminoacylreact3.setSpecies('MG511'),      'assign reactant species')
    check(mg511aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg511aminoacylprod1 = mg511aminoacyl.createProduct()
    check(mg511aminoacylprod1,                       'create product')
    check(mg511aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg511aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg511aminoacylprod2 = mg511aminoacyl.createProduct()
    check(mg511aminoacylprod2,                       'create product')
    check(mg511aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg511aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg511aminoacylprod3 = mg511aminoacyl.createProduct()
    check(mg511aminoacylprod3,                       'create product')
    check(mg511aminoacylprod3.setSpecies('aminoacylated_MG511'),      'assign product species')
    check(mg511aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg511aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG512 tRNA aminoacylation (Threonine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg512aminoacyl = model.createReaction()
    check(mg512aminoacyl,                                 'create reaction')
    check(mg512aminoacyl.setId('MG512_Aminoacylation'),                     'set reaction id')
    check(mg512aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg512aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg512aminoacylreact1 = mg512aminoacyl.createReactant()
    check(mg512aminoacylreact1,                       'create reactant')
    check(mg512aminoacylreact1.setSpecies('THR'),      'assign reactant species')
    check(mg512aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg512aminoacylreact2 = mg512aminoacyl.createReactant()
    check(mg512aminoacylreact2,                       'create reactant')
    check(mg512aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg512aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg512aminoacylreact3 = mg512aminoacyl.createReactant()
    check(mg512aminoacylreact3,                       'create reactant')
    check(mg512aminoacylreact3.setSpecies('MG512'),      'assign reactant species')
    check(mg512aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg512aminoacylprod1 = mg512aminoacyl.createProduct()
    check(mg512aminoacylprod1,                       'create product')
    check(mg512aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg512aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg512aminoacylprod2 = mg512aminoacyl.createProduct()
    check(mg512aminoacylprod2,                       'create product')
    check(mg512aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg512aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg512aminoacylprod3 = mg512aminoacyl.createProduct()
    check(mg512aminoacylprod3,                       'create product')
    check(mg512aminoacylprod3.setSpecies('aminoacylated_MG512'),      'assign product species')
    check(mg512aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg512aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG513 tRNA aminoacylation (Glutamate)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg513aminoacyl = model.createReaction()
    check(mg513aminoacyl,                                 'create reaction')
    check(mg513aminoacyl.setId('MG513_Aminoacylation'),                     'set reaction id')
    check(mg513aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg513aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg513aminoacylreact1 = mg513aminoacyl.createReactant()
    check(mg513aminoacylreact1,                       'create reactant')
    check(mg513aminoacylreact1.setSpecies('GLU'),      'assign reactant species')
    check(mg513aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg513aminoacylreact2 = mg513aminoacyl.createReactant()
    check(mg513aminoacylreact2,                       'create reactant')
    check(mg513aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg513aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg513aminoacylreact3 = mg513aminoacyl.createReactant()
    check(mg513aminoacylreact3,                       'create reactant')
    check(mg513aminoacylreact3.setSpecies('MG513'),      'assign reactant species')
    check(mg513aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg513aminoacylprod1 = mg513aminoacyl.createProduct()
    check(mg513aminoacylprod1,                       'create product')
    check(mg513aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg513aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg513aminoacylprod2 = mg513aminoacyl.createProduct()
    check(mg513aminoacylprod2,                       'create product')
    check(mg513aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg513aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg513aminoacylprod3 = mg513aminoacyl.createProduct()
    check(mg513aminoacylprod3,                       'create product')
    check(mg513aminoacylprod3.setSpecies('aminoacylated_MG513'),      'assign product species')
    check(mg513aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg513aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG514 tRNA aminoacylation (Asparagine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg514aminoacyl = model.createReaction()
    check(mg514aminoacyl,                                 'create reaction')
    check(mg514aminoacyl.setId('MG514_Aminoacylation'),                     'set reaction id')
    check(mg514aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg514aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg514aminoacylreact1 = mg514aminoacyl.createReactant()
    check(mg514aminoacylreact1,                       'create reactant')
    check(mg514aminoacylreact1.setSpecies('ASN'),      'assign reactant species')
    check(mg514aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg514aminoacylreact2 = mg514aminoacyl.createReactant()
    check(mg514aminoacylreact2,                       'create reactant')
    check(mg514aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg514aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg514aminoacylreact3 = mg514aminoacyl.createReactant()
    check(mg514aminoacylreact3,                       'create reactant')
    check(mg514aminoacylreact3.setSpecies('MG514'),      'assign reactant species')
    check(mg514aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg514aminoacylprod1 = mg514aminoacyl.createProduct()
    check(mg514aminoacylprod1,                       'create product')
    check(mg514aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg514aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg514aminoacylprod2 = mg514aminoacyl.createProduct()
    check(mg514aminoacylprod2,                       'create product')
    check(mg514aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg514aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg514aminoacylprod3 = mg514aminoacyl.createProduct()
    check(mg514aminoacylprod3,                       'create product')
    check(mg514aminoacylprod3.setSpecies('aminoacylated_MG514'),      'assign product species')
    check(mg514aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg514aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG518 tRNA aminoacylation (Histidine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg518aminoacyl = model.createReaction()
    check(mg518aminoacyl,                                 'create reaction')
    check(mg518aminoacyl.setId('MG518_Aminoacylation'),                     'set reaction id')
    check(mg518aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg518aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg518aminoacylreact1 = mg518aminoacyl.createReactant()
    check(mg518aminoacylreact1,                       'create reactant')
    check(mg518aminoacylreact1.setSpecies('HIS'),      'assign reactant species')
    check(mg518aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg518aminoacylreact2 = mg518aminoacyl.createReactant()
    check(mg518aminoacylreact2,                       'create reactant')
    check(mg518aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg518aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg518aminoacylreact3 = mg518aminoacyl.createReactant()
    check(mg518aminoacylreact3,                       'create reactant')
    check(mg518aminoacylreact3.setSpecies('MG518'),      'assign reactant species')
    check(mg518aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg518aminoacylprod1 = mg518aminoacyl.createProduct()
    check(mg518aminoacylprod1,                       'create product')
    check(mg518aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg518aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg518aminoacylprod2 = mg518aminoacyl.createProduct()
    check(mg518aminoacylprod2,                       'create product')
    check(mg518aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg518aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg518aminoacylprod3 = mg518aminoacyl.createProduct()
    check(mg518aminoacylprod3,                       'create product')
    check(mg518aminoacylprod3.setSpecies('aminoacylated_MG518'),      'assign product species')
    check(mg518aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg518aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG519 tRNA aminoacylation (Leucine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg519aminoacyl = model.createReaction()
    check(mg519aminoacyl,                                 'create reaction')
    check(mg519aminoacyl.setId('MG519_Aminoacylation'),                     'set reaction id')
    check(mg519aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg519aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg519aminoacylreact1 = mg519aminoacyl.createReactant()
    check(mg519aminoacylreact1,                       'create reactant')
    check(mg519aminoacylreact1.setSpecies('LEU'),      'assign reactant species')
    check(mg519aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg519aminoacylreact2 = mg519aminoacyl.createReactant()
    check(mg519aminoacylreact2,                       'create reactant')
    check(mg519aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg519aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg519aminoacylreact3 = mg519aminoacyl.createReactant()
    check(mg519aminoacylreact3,                       'create reactant')
    check(mg519aminoacylreact3.setSpecies('MG519'),      'assign reactant species')
    check(mg519aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg519aminoacylprod1 = mg519aminoacyl.createProduct()
    check(mg519aminoacylprod1,                       'create product')
    check(mg519aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg519aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg519aminoacylprod2 = mg519aminoacyl.createProduct()
    check(mg519aminoacylprod2,                       'create product')
    check(mg519aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg519aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg519aminoacylprod3 = mg519aminoacyl.createProduct()
    check(mg519aminoacylprod3,                       'create product')
    check(mg519aminoacylprod3.setSpecies('aminoacylated_MG519'),      'assign product species')
    check(mg519aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg519aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG520 tRNA aminoacylation (Leucine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg520aminoacyl = model.createReaction()
    check(mg520aminoacyl,                                 'create reaction')
    check(mg520aminoacyl.setId('MG520_Aminoacylation'),                     'set reaction id')
    check(mg520aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg520aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg520aminoacylreact1 = mg520aminoacyl.createReactant()
    check(mg520aminoacylreact1,                       'create reactant')
    check(mg520aminoacylreact1.setSpecies('LEU'),      'assign reactant species')
    check(mg520aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg520aminoacylreact2 = mg520aminoacyl.createReactant()
    check(mg520aminoacylreact2,                       'create reactant')
    check(mg520aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg520aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg520aminoacylreact3 = mg520aminoacyl.createReactant()
    check(mg520aminoacylreact3,                       'create reactant')
    check(mg520aminoacylreact3.setSpecies('MG520'),      'assign reactant species')
    check(mg520aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg520aminoacylprod1 = mg520aminoacyl.createProduct()
    check(mg520aminoacylprod1,                       'create product')
    check(mg520aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg520aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg520aminoacylprod2 = mg520aminoacyl.createProduct()
    check(mg520aminoacylprod2,                       'create product')
    check(mg520aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg520aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg520aminoacylprod3 = mg520aminoacyl.createProduct()
    check(mg520aminoacylprod3,                       'create product')
    check(mg520aminoacylprod3.setSpecies('aminoacylated_MG520'),      'assign product species')
    check(mg520aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg520aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # MG523 tRNA aminoacylation (Arginine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg523aminoacyl = model.createReaction()
    check(mg523aminoacyl,                                 'create reaction')
    check(mg523aminoacyl.setId('MG523_Aminoacylation'),                     'set reaction id')
    check(mg523aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg523aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg523aminoacylreact1 = mg523aminoacyl.createReactant()
    check(mg523aminoacylreact1,                       'create reactant')
    check(mg523aminoacylreact1.setSpecies('ARG'),      'assign reactant species')
    check(mg523aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg523aminoacylreact2 = mg523aminoacyl.createReactant()
    check(mg523aminoacylreact2,                       'create reactant')
    check(mg523aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg523aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg523aminoacylreact3 = mg523aminoacyl.createReactant()
    check(mg523aminoacylreact3,                       'create reactant')
    check(mg523aminoacylreact3.setSpecies('MG523'),      'assign reactant species')
    check(mg523aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg523aminoacylprod1 = mg523aminoacyl.createProduct()
    check(mg523aminoacylprod1,                       'create product')
    check(mg523aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg523aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg523aminoacylprod2 = mg523aminoacyl.createProduct()
    check(mg523aminoacylprod2,                       'create product')
    check(mg523aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg523aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg523aminoacylprod3 = mg523aminoacyl.createProduct()
    check(mg523aminoacylprod3,                       'create product')
    check(mg523aminoacylprod3.setSpecies('aminoacylated_MG523'),      'assign product species')
    check(mg523aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg523aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')



    # Now return a text string containing the model in XML format.

    return writeSBMLToString(document)

 
if __name__ == '__main__':
    print(create_model())
