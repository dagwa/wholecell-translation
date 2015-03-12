# misc data to integrate in to the code

# MG_0004_Aminoacylation

# Initialization Block
import os
import libsbml as sbml


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
        if value == sbml.LIBSBML_OPERATION_SUCCESS:
            return
        else:
            err_msg = 'Error encountered trying to ' + message + '.' \
                      + 'LibSBML returned error code ' + str(value) + ': "' \
                      + sbml.OperationReturnValue_toString(value).strip() + '"'
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
        document = sbml.SBMLDocument(3, 1)
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
    check(unit.setKind(sbml.UNIT_KIND_SECOND),     'set unit kind')
    check(unit.setExponent(-1),               'set unit exponent')
    check(unit.setScale(0),                   'set unit scale')
    check(unit.setMultiplier(1),              'set unit multiplier')

    per_minute = model.createUnitDefinition()
    check(per_minute,                         'create unit definition')
    check(per_minute.setId('per_minute'),     'set unit definition id')
    unit = per_minute.createUnit()
    check(unit,                               'create unit on per_minute')
    check(unit.setKind(sbml.UNIT_KIND_SECOND),     'set unit kind')
    check(unit.setExponent(-1),               'set unit exponent')
    check(unit.setScale(0),                   'set unit scale')
    check(unit.setMultiplier(60),              'set unit multiplier')

    # Create a compartment inside this model, and set the required
    # attributes for an SBML compartment in SBML Level 3.

    cytocompartment = model.createCompartment()
    check(cytocompartment,                                 'create compartment')
    check(cytocompartment.setId('c'),                     'set compartment id')
    check(cytocompartment.setConstant(True),               'set compartment "constant"')
    check(cytocompartment.setSize(0.01),                   'set compartment "size"')
    check(cytocompartment.setSpatialDimensions(3),         'set compartment dimensions')
    check(cytocompartment.setUnits('litre'),               'set compartment size units')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create species and set the required attributes - Metabolites
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

    adp = model.createSpecies()
    check(adp,                                 'create species s1')
    check(adp.setId('ADP'),                     'set species s1 id')
    check(adp.setCompartment('c'),            'set species s1 compartment')
    check(adp.setConstant(False),              'set "constant" attribute on s1')
    check(adp.setInitialAmount(10),             'set initial amount for s1')
    check(adp.setSubstanceUnits('item'),       'set substance units for s1')
    check(adp.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(adp.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    amp = model.createSpecies()
    check(amp,                                 'create species s1')
    check(amp.setId('AMP'),                     'set species s1 id')
    check(amp.setCompartment('c'),            'set species s1 compartment')
    check(amp.setConstant(False),              'set "constant" attribute on s1')
    check(amp.setInitialAmount(10),             'set initial amount for s1')
    check(amp.setSubstanceUnits('item'),       'set substance units for s1')
    check(amp.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(amp.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    atp = model.createSpecies()
    check(atp,                                 'create species s1')
    check(atp.setId('ATP'),                    'set species s1 id')
    check(atp.setCompartment('c'),             'set species s1 compartment')
    check(atp.setConstant(False),              'set "constant" attribute on s1')
    check(atp.setInitialAmount(1000),             'set initial amount for s1')
    check(atp.setSubstanceUnits('item'),       'set substance units for s1')
    check(atp.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(atp.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    fthf10 = model.createSpecies()
    check(fthf10,                                 'create species s1')
    check(fthf10.setId('FTHF10'),                 'set species s1 id')
    check(fthf10.setCompartment('c'),             'set species s1 compartment')
    check(fthf10.setConstant(False),              'set "constant" attribute on s1')
    check(fthf10.setInitialAmount(10),             'set initial amount for s1')
    check(fthf10.setSubstanceUnits('item'),       'set substance units for s1')
    check(fthf10.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(fthf10.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    proton = model.createSpecies()
    check(proton,                                 'create species s1')
    check(proton.setId('H'),                 'set species s1 id')
    check(proton.setCompartment('c'),             'set species s1 compartment')
    check(proton.setConstant(False),              'set "constant" attribute on s1')
    check(proton.setInitialAmount(10),             'set initial amount for s1')
    check(proton.setSubstanceUnits('item'),       'set substance units for s1')
    check(proton.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(proton.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    pi = model.createSpecies()
    check(pi,                                 'create species s1')
    check(pi.setId('PI'),                     'set species s1 id')
    check(pi.setCompartment('c'),            'set species s1 compartment')
    check(pi.setConstant(False),              'set "constant" attribute on s1')
    check(pi.setInitialAmount(10),             'set initial amount for s1')
    check(pi.setSubstanceUnits('item'),       'set substance units for s1')
    check(pi.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(pi.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ppi = model.createSpecies()
    check(ppi,                                 'create species s1')
    check(ppi.setId('PPI'),                     'set species s1 id')
    check(ppi.setCompartment('c'),            'set species s1 compartment')
    check(ppi.setConstant(False),              'set "constant" attribute on s1')
    check(ppi.setInitialAmount(10),             'set initial amount for s1')
    check(ppi.setSubstanceUnits('item'),       'set substance units for s1')
    check(ppi.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ppi.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    thf = model.createSpecies()
    check(thf,                                 'create species s1')
    check(thf.setId('THF'),                     'set species s1 id')
    check(thf.setCompartment('c'),            'set species s1 compartment')
    check(thf.setConstant(False),              'set "constant" attribute on s1')
    check(thf.setInitialAmount(10),             'set initial amount for s1')
    check(thf.setSubstanceUnits('item'),       'set substance units for s1')
    check(thf.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(thf.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    water = model.createSpecies()
    check(water,                                 'create species s1')
    check(water.setId('H2O'),                     'set species s1 id')
    check(water.setCompartment('c'),            'set species s1 compartment')
    check(water.setConstant(False),              'set "constant" attribute on s1')
    check(water.setInitialAmount(1000),             'set initial amount for s1')
    check(water.setSubstanceUnits('item'),       'set substance units for s1')
    check(water.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(water.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    alanine = model.createSpecies()
    check(alanine,                                 'create species s1')
    check(alanine.setId('ALA'),                     'set species s1 id')
    check(alanine.setCompartment('c'),            'set species s1 compartment')
    check(alanine.setConstant(False),              'set "constant" attribute on s1')
    check(alanine.setInitialAmount(10),             'set initial amount for s1')
    check(alanine.setSubstanceUnits('item'),       'set substance units for s1')
    check(alanine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(alanine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    arginine = model.createSpecies()
    check(arginine,                                 'create species s1')
    check(arginine.setId('ARG'),                     'set species s1 id')
    check(arginine.setCompartment('c'),            'set species s1 compartment')
    check(arginine.setConstant(False),              'set "constant" attribute on s1')
    check(arginine.setInitialAmount(10),             'set initial amount for s1')
    check(arginine.setSubstanceUnits('item'),       'set substance units for s1')
    check(arginine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(arginine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    asparagine = model.createSpecies()
    check(asparagine,                                 'create species s1')
    check(asparagine.setId('ASN'),                     'set species s1 id')
    check(asparagine.setCompartment('c'),            'set species s1 compartment')
    check(asparagine.setConstant(False),              'set "constant" attribute on s1')
    check(asparagine.setInitialAmount(10),             'set initial amount for s1')
    check(asparagine.setSubstanceUnits('item'),       'set substance units for s1')
    check(asparagine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(asparagine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    aspartate = model.createSpecies()
    check(aspartate,                                 'create species s1')
    check(aspartate.setId('ASP'),                     'set species s1 id')
    check(aspartate.setCompartment('c'),            'set species s1 compartment')
    check(aspartate.setConstant(False),              'set "constant" attribute on s1')
    check(aspartate.setInitialAmount(10),             'set initial amount for s1')
    check(aspartate.setSubstanceUnits('item'),       'set substance units for s1')
    check(aspartate.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(aspartate.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    cysteine = model.createSpecies()
    check(cysteine,                                 'create species s1')
    check(cysteine.setId('CYS'),                     'set species s1 id')
    check(cysteine.setCompartment('c'),            'set species s1 compartment')
    check(cysteine.setConstant(False),              'set "constant" attribute on s1')
    check(cysteine.setInitialAmount(10),             'set initial amount for s1')
    check(cysteine.setSubstanceUnits('item'),       'set substance units for s1')
    check(cysteine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(cysteine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    glutamate = model.createSpecies()
    check(glutamate,                                 'create species s1')
    check(glutamate.setId('GLU'),                     'set species s1 id')
    check(glutamate.setCompartment('c'),            'set species s1 compartment')
    check(glutamate.setConstant(False),              'set "constant" attribute on s1')
    check(glutamate.setInitialAmount(10),             'set initial amount for s1')
    check(glutamate.setSubstanceUnits('item'),       'set substance units for s1')
    check(glutamate.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(glutamate.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    glutamine = model.createSpecies()
    check(glutamine,                                 'create species s1')
    check(glutamine.setId('GLN'),                     'set species s1 id')
    check(glutamine.setCompartment('c'),            'set species s1 compartment')
    check(glutamine.setConstant(False),              'set "constant" attribute on s1')
    check(glutamine.setInitialAmount(10),             'set initial amount for s1')
    check(glutamine.setSubstanceUnits('item'),       'set substance units for s1')
    check(glutamine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(glutamine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    glycine = model.createSpecies()
    check(glycine,                                 'create species s1')
    check(glycine.setId('GLY'),                     'set species s1 id')
    check(glycine.setCompartment('c'),            'set species s1 compartment')
    check(glycine.setConstant(False),              'set "constant" attribute on s1')
    check(glycine.setInitialAmount(10),             'set initial amount for s1')
    check(glycine.setSubstanceUnits('item'),       'set substance units for s1')
    check(glycine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(glycine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    histidine = model.createSpecies()
    check(histidine,                                 'create species s1')
    check(histidine.setId('HIS'),                     'set species s1 id')
    check(histidine.setCompartment('c'),            'set species s1 compartment')
    check(histidine.setConstant(False),              'set "constant" attribute on s1')
    check(histidine.setInitialAmount(10),             'set initial amount for s1')
    check(histidine.setSubstanceUnits('item'),       'set substance units for s1')
    check(histidine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(histidine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    isoleucine = model.createSpecies()
    check(isoleucine,                                 'create species s1')
    check(isoleucine.setId('ILE'),                     'set species s1 id')
    check(isoleucine.setCompartment('c'),            'set species s1 compartment')
    check(isoleucine.setConstant(False),              'set "constant" attribute on s1')
    check(isoleucine.setInitialAmount(10),             'set initial amount for s1')
    check(isoleucine.setSubstanceUnits('item'),       'set substance units for s1')
    check(isoleucine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(isoleucine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    leucine = model.createSpecies()
    check(leucine,                                 'create species s1')
    check(leucine.setId('LEU'),                     'set species s1 id')
    check(leucine.setCompartment('c'),            'set species s1 compartment')
    check(leucine.setConstant(False),              'set "constant" attribute on s1')
    check(leucine.setInitialAmount(10),             'set initial amount for s1')
    check(leucine.setSubstanceUnits('item'),       'set substance units for s1')
    check(leucine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(leucine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    lysine = model.createSpecies()
    check(lysine,                                 'create species s1')
    check(lysine.setId('LYS'),                     'set species s1 id')
    check(lysine.setCompartment('c'),            'set species s1 compartment')
    check(lysine.setConstant(False),              'set "constant" attribute on s1')
    check(lysine.setInitialAmount(10),             'set initial amount for s1')
    check(lysine.setSubstanceUnits('item'),       'set substance units for s1')
    check(lysine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(lysine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    methionine = model.createSpecies()
    check(methionine,                                 'create species s1')
    check(methionine.setId('MET'),                     'set species s1 id')
    check(methionine.setCompartment('c'),            'set species s1 compartment')
    check(methionine.setConstant(False),              'set "constant" attribute on s1')
    check(methionine.setInitialAmount(10),             'set initial amount for s1')
    check(methionine.setSubstanceUnits('item'),       'set substance units for s1')
    check(methionine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(methionine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    phenylalanine = model.createSpecies()
    check(phenylalanine,                                 'create species s1')
    check(phenylalanine.setId('PHE'),                     'set species s1 id')
    check(phenylalanine.setCompartment('c'),            'set species s1 compartment')
    check(phenylalanine.setConstant(False),              'set "constant" attribute on s1')
    check(phenylalanine.setInitialAmount(10),             'set initial amount for s1')
    check(phenylalanine.setSubstanceUnits('item'),       'set substance units for s1')
    check(phenylalanine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(phenylalanine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    proline = model.createSpecies()
    check(proline,                                 'create species s1')
    check(proline.setId('PRO'),                     'set species s1 id')
    check(proline.setCompartment('c'),            'set species s1 compartment')
    check(proline.setConstant(False),              'set "constant" attribute on s1')
    check(proline.setInitialAmount(10),             'set initial amount for s1')
    check(proline.setSubstanceUnits('item'),       'set substance units for s1')
    check(proline.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(proline.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    serine = model.createSpecies()
    check(serine,                                 'create species s1')
    check(serine.setId('SER'),                    'set species s1 id')
    check(serine.setCompartment('c'),             'set species s1 compartment')
    check(serine.setConstant(False),              'set "constant" attribute on s1')
    check(serine.setInitialAmount(10),             'set initial amount for s1')
    check(serine.setSubstanceUnits('item'),       'set substance units for s1')
    check(serine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(serine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    threonine = model.createSpecies()
    check(threonine,                                 'create species s1')
    check(threonine.setId('THR'),                    'set species s1 id')
    check(threonine.setCompartment('c'),             'set species s1 compartment')
    check(threonine.setConstant(False),              'set "constant" attribute on s1')
    check(threonine.setInitialAmount(10),             'set initial amount for s1')
    check(threonine.setSubstanceUnits('item'),       'set substance units for s1')
    check(threonine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(threonine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    tryptophan = model.createSpecies()
    check(tryptophan,                                 'create species s1')
    check(tryptophan.setId('TRP'),                     'set species s1 id')
    check(tryptophan.setCompartment('c'),            'set species s1 compartment')
    check(tryptophan.setConstant(False),              'set "constant" attribute on s1')
    check(tryptophan.setInitialAmount(10),             'set initial amount for s1')
    check(tryptophan.setSubstanceUnits('item'),       'set substance units for s1')
    check(tryptophan.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(tryptophan.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    tyrosine = model.createSpecies()
    check(tyrosine,                                 'create species s1')
    check(tyrosine.setId('TYR'),                     'set species s1 id')
    check(tyrosine.setCompartment('c'),            'set species s1 compartment')
    check(tyrosine.setConstant(False),              'set "constant" attribute on s1')
    check(tyrosine.setInitialAmount(10),             'set initial amount for s1')
    check(tyrosine.setSubstanceUnits('item'),       'set substance units for s1')
    check(tyrosine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(tyrosine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    valine = model.createSpecies()
    check(valine,                                 'create species s1')
    check(valine.setId('VAL'),                    'set species s1 id')
    check(valine.setCompartment('c'),             'set species s1 compartment')
    check(valine.setConstant(False),              'set "constant" attribute on s1')
    check(valine.setInitialAmount(10),             'set initial amount for s1')
    check(valine.setSubstanceUnits('item'),       'set substance units for s1')
    check(valine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(valine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create species and set the required attributes - tRNAs: unloaded and loaded
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    ala_trna = model.createSpecies()
    check(ala_trna,                                 'create species s1')
    check(ala_trna.setId('MG471'),                     'set species s1 id')
    check(ala_trna.setCompartment('c'),            'set species s1 compartment')
    check(ala_trna.setConstant(False),              'set "constant" attribute on s1')
    check(ala_trna.setInitialAmount(10),             'set initial amount for s1')
    check(ala_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(ala_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ala_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ala_trna_loaded = model.createSpecies()
    check(ala_trna_loaded,                                 'create species s1')
    check(ala_trna_loaded.setId('aminoacylated_MG471'),                     'set species s1 id')
    check(ala_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(ala_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(ala_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(ala_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(ala_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ala_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    arg_trna = model.createSpecies()
    check(arg_trna,                                 'create species s1')
    check(arg_trna.setId('MG492'),                     'set species s1 id')
    check(arg_trna.setCompartment('c'),            'set species s1 compartment')
    check(arg_trna.setConstant(False),              'set "constant" attribute on s1')
    check(arg_trna.setInitialAmount(10),             'set initial amount for s1')
    check(arg_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(arg_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(arg_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    arg_trna_loaded = model.createSpecies()
    check(arg_trna_loaded,                                 'create species s1')
    check(arg_trna_loaded.setId('aminoacylated_MG492'),    'set species s1 id')
    check(arg_trna_loaded.setCompartment('c'),             'set species s1 compartment')
    check(arg_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(arg_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(arg_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(arg_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(arg_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    arg_trna2 = model.createSpecies()
    check(arg_trna2,                                 'create species s1')
    check(arg_trna2.setId('MG495'),                     'set species s1 id')
    check(arg_trna2.setCompartment('c'),            'set species s1 compartment')
    check(arg_trna2.setConstant(False),              'set "constant" attribute on s1')
    check(arg_trna2.setInitialAmount(10),             'set initial amount for s1')
    check(arg_trna2.setSubstanceUnits('item'),       'set substance units for s1')
    check(arg_trna2.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(arg_trna2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    arg_trna2_loaded = model.createSpecies()
    check(arg_trna2_loaded,                                 'create species s1')
    check(arg_trna2_loaded.setId('aminoacylated_MG495'),                     'set species s1 id')
    check(arg_trna2_loaded.setCompartment('c'),            'set species s1 compartment')
    check(arg_trna2_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(arg_trna2_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(arg_trna2_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(arg_trna2_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(arg_trna2_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    arg_trna3 = model.createSpecies()
    check(arg_trna3,                                 'create species s1')
    check(arg_trna3.setId('MG497'),                     'set species s1 id')
    check(arg_trna3.setCompartment('c'),            'set species s1 compartment')
    check(arg_trna3.setConstant(False),              'set "constant" attribute on s1')
    check(arg_trna3.setInitialAmount(10),             'set initial amount for s1')
    check(arg_trna3.setSubstanceUnits('item'),       'set substance units for s1')
    check(arg_trna3.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(arg_trna3.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    arg_trna3_loaded = model.createSpecies()
    check(arg_trna3_loaded,                                 'create species s1')
    check(arg_trna3_loaded.setId('aminoacylated_MG497'),                     'set species s1 id')
    check(arg_trna3_loaded.setCompartment('c'),            'set species s1 compartment')
    check(arg_trna3_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(arg_trna3_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(arg_trna3_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(arg_trna3_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(arg_trna3_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    arg_trna4 = model.createSpecies()
    check(arg_trna4,                                 'create species s1')
    check(arg_trna4.setId('MG523'),                     'set species s1 id')
    check(arg_trna4.setCompartment('c'),            'set species s1 compartment')
    check(arg_trna4.setConstant(False),              'set "constant" attribute on s1')
    check(arg_trna4.setInitialAmount(10),             'set initial amount for s1')
    check(arg_trna4.setSubstanceUnits('item'),       'set substance units for s1')
    check(arg_trna4.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(arg_trna4.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    arg_trna4_loaded = model.createSpecies()
    check(arg_trna4_loaded,                                 'create species s1')
    check(arg_trna4_loaded.setId('aminoacylated_MG523'),                     'set species s1 id')
    check(arg_trna4_loaded.setCompartment('c'),            'set species s1 compartment')
    check(arg_trna4_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(arg_trna4_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(arg_trna4_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(arg_trna4_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(arg_trna4_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    asn_trna = model.createSpecies()
    check(asn_trna,                                 'create species s1')
    check(asn_trna.setId('MG514'),                  'set species s1 id')
    check(asn_trna.setCompartment('c'),             'set species s1 compartment')
    check(asn_trna.setConstant(False),              'set "constant" attribute on s1')
    check(asn_trna.setInitialAmount(10),             'set initial amount for s1')
    check(asn_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(asn_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(asn_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    asn_trna_loaded = model.createSpecies()
    check(asn_trna_loaded,                                 'create species s1')
    check(asn_trna_loaded.setId('aminoacylated_MG514'),    'set species s1 id')
    check(asn_trna_loaded.setCompartment('c'),             'set species s1 compartment')
    check(asn_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(asn_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(asn_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(asn_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(asn_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    asp_trna = model.createSpecies()
    check(asp_trna,                                 'create species s1')
    check(asp_trna.setId('MG489'),                  'set species s1 id')
    check(asp_trna.setCompartment('c'),             'set species s1 compartment')
    check(asp_trna.setConstant(False),              'set "constant" attribute on s1')
    check(asp_trna.setInitialAmount(10),             'set initial amount for s1')
    check(asp_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(asp_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(asp_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    asp_trna_loaded = model.createSpecies()
    check(asp_trna_loaded,                                 'create species s1')
    check(asp_trna_loaded.setId('aminoacylated_MG489'),    'set species s1 id')
    check(asp_trna_loaded.setCompartment('c'),             'set species s1 compartment')
    check(asp_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(asp_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(asp_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(asp_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(asp_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    cys_trna = model.createSpecies()
    check(cys_trna,                                 'create species s1')
    check(cys_trna.setId('MG483'),                  'set species s1 id')
    check(cys_trna.setCompartment('c'),             'set species s1 compartment')
    check(cys_trna.setConstant(False),              'set "constant" attribute on s1')
    check(cys_trna.setInitialAmount(10),             'set initial amount for s1')
    check(cys_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(cys_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(cys_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    cys_trna_loaded = model.createSpecies()
    check(cys_trna_loaded,                                 'create species s1')
    check(cys_trna_loaded.setId('aminoacylated_MG483'),                     'set species s1 id')
    check(cys_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(cys_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(cys_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(cys_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(cys_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(cys_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    gln_trna = model.createSpecies()
    check(gln_trna,                                 'create species s1')
    check(gln_trna.setId('MG502'),                  'set species s1 id')
    check(gln_trna.setCompartment('c'),             'set species s1 compartment')
    check(gln_trna.setConstant(False),              'set "constant" attribute on s1')
    check(gln_trna.setInitialAmount(10),             'set initial amount for s1')
    check(gln_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(gln_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(gln_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    gln_trna_glu_loaded = model.createSpecies()
    check(gln_trna_glu_loaded,                                 'create species s1')
    check(gln_trna_glu_loaded.setId('GLU_aminoacylated_MG502'),                     'set species s1 id')
    check(gln_trna_glu_loaded.setCompartment('c'),            'set species s1 compartment')
    check(gln_trna_glu_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(gln_trna_glu_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(gln_trna_glu_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(gln_trna_glu_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(gln_trna_glu_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    gln_trna_loaded = model.createSpecies()
    check(gln_trna_loaded,                                 'create species s1')
    check(gln_trna_loaded.setId('aminoacylated_MG502'),                     'set species s1 id')
    check(gln_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(gln_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(gln_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(gln_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(gln_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(gln_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    glu_trna = model.createSpecies()
    check(glu_trna,                                 'create species s1')
    check(glu_trna.setId('MG513'),                  'set species s1 id')
    check(glu_trna.setCompartment('c'),             'set species s1 compartment')
    check(glu_trna.setConstant(False),              'set "constant" attribute on s1')
    check(glu_trna.setInitialAmount(10),             'set initial amount for s1')
    check(glu_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(glu_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(glu_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    glu_trna_loaded = model.createSpecies()
    check(glu_trna_loaded,                                 'create species s1')
    check(glu_trna_loaded.setId('aminoacylated_MG513'),                     'set species s1 id')
    check(glu_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(glu_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(glu_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(glu_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(glu_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(glu_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    gly_trna = model.createSpecies()
    check(gly_trna,                                 'create species s1')
    check(gly_trna.setId('MG493'),                  'set species s1 id')
    check(gly_trna.setCompartment('c'),             'set species s1 compartment')
    check(gly_trna.setConstant(False),              'set "constant" attribute on s1')
    check(gly_trna.setInitialAmount(10),             'set initial amount for s1')
    check(gly_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(gly_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(gly_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    gly_trna_loaded = model.createSpecies()
    check(gly_trna_loaded,                                 'create species s1')
    check(gly_trna_loaded.setId('aminoacylated_MG493'),                     'set species s1 id')
    check(gly_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(gly_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(gly_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(gly_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(gly_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(gly_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    gly_trna2 = model.createSpecies()
    check(gly_trna2,                                 'create species s1')
    check(gly_trna2.setId('MG499'),                  'set species s1 id')
    check(gly_trna2.setCompartment('c'),             'set species s1 compartment')
    check(gly_trna2.setConstant(False),              'set "constant" attribute on s1')
    check(gly_trna2.setInitialAmount(10),             'set initial amount for s1')
    check(gly_trna2.setSubstanceUnits('item'),       'set substance units for s1')
    check(gly_trna2.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(gly_trna2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    gly_trna2_loaded = model.createSpecies()
    check(gly_trna2_loaded,                                 'create species s1')
    check(gly_trna2_loaded.setId('aminoacylated_MG499'),                     'set species s1 id')
    check(gly_trna2_loaded.setCompartment('c'),            'set species s1 compartment')
    check(gly_trna2_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(gly_trna2_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(gly_trna2_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(gly_trna2_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(gly_trna2_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    his_trna = model.createSpecies()
    check(his_trna,                                 'create species s1')
    check(his_trna.setId('MG518'),                     'set species s1 id')
    check(his_trna.setCompartment('c'),            'set species s1 compartment')
    check(his_trna.setConstant(False),              'set "constant" attribute on s1')
    check(his_trna.setInitialAmount(10),             'set initial amount for s1')
    check(his_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(his_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(his_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    his_trna_loaded = model.createSpecies()
    check(his_trna_loaded,                                 'create species s1')
    check(his_trna_loaded.setId('aminoacylated_MG518'),                     'set species s1 id')
    check(his_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(his_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(his_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(his_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(his_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(his_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ile_trna = model.createSpecies()
    check(ile_trna,                                 'create species s1')
    check(ile_trna.setId('MG472'),                     'set species s1 id')
    check(ile_trna.setCompartment('c'),            'set species s1 compartment')
    check(ile_trna.setConstant(False),              'set "constant" attribute on s1')
    check(ile_trna.setInitialAmount(10),             'set initial amount for s1')
    check(ile_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(ile_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ile_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ile_trna_loaded = model.createSpecies()
    check(ile_trna_loaded,                                 'create species s1')
    check(ile_trna_loaded.setId('aminoacylated_MG472'),                     'set species s1 id')
    check(ile_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(ile_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(ile_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(ile_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(ile_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ile_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ile_trna2 = model.createSpecies()
    check(ile_trna2,                                 'create species s1')
    check(ile_trna2.setId('MG486'),                     'set species s1 id')
    check(ile_trna2.setCompartment('c'),            'set species s1 compartment')
    check(ile_trna2.setConstant(False),              'set "constant" attribute on s1')
    check(ile_trna2.setInitialAmount(10),             'set initial amount for s1')
    check(ile_trna2.setSubstanceUnits('item'),       'set substance units for s1')
    check(ile_trna2.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ile_trna2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ile_trna2_loaded = model.createSpecies()
    check(ile_trna2_loaded,                                 'create species s1')
    check(ile_trna2_loaded.setId('aminoacylated_MG486'),                     'set species s1 id')
    check(ile_trna2_loaded.setCompartment('c'),            'set species s1 compartment')
    check(ile_trna2_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(ile_trna2_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(ile_trna2_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(ile_trna2_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ile_trna2_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    leu_trna = model.createSpecies()
    check(leu_trna,                                 'create species s1')
    check(leu_trna.setId('MG500'),                     'set species s1 id')
    check(leu_trna.setCompartment('c'),            'set species s1 compartment')
    check(leu_trna.setConstant(False),              'set "constant" attribute on s1')
    check(leu_trna.setInitialAmount(10),             'set initial amount for s1')
    check(leu_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(leu_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(leu_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    leu_trna_loaded = model.createSpecies()
    check(leu_trna_loaded,                                 'create species s1')
    check(leu_trna_loaded.setId('aminoacylated_MG500'),                     'set species s1 id')
    check(leu_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(leu_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(leu_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(leu_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(leu_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(leu_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    leu_trna2 = model.createSpecies()
    check(leu_trna2,                                 'create species s1')
    check(leu_trna2.setId('MG508'),                     'set species s1 id')
    check(leu_trna2.setCompartment('c'),            'set species s1 compartment')
    check(leu_trna2.setConstant(False),              'set "constant" attribute on s1')
    check(leu_trna2.setInitialAmount(10),             'set initial amount for s1')
    check(leu_trna2.setSubstanceUnits('item'),       'set substance units for s1')
    check(leu_trna2.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(leu_trna2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    leu_trna2_loaded = model.createSpecies()
    check(leu_trna2_loaded,                                 'create species s1')
    check(leu_trna2_loaded.setId('aminoacylated_MG508'),                     'set species s1 id')
    check(leu_trna2_loaded.setCompartment('c'),            'set species s1 compartment')
    check(leu_trna2_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(leu_trna2_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(leu_trna2_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(leu_trna2_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(leu_trna2_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    leu_trna3 = model.createSpecies()
    check(leu_trna3,                                 'create species s1')
    check(leu_trna3.setId('MG519'),                     'set species s1 id')
    check(leu_trna3.setCompartment('c'),            'set species s1 compartment')
    check(leu_trna3.setConstant(False),              'set "constant" attribute on s1')
    check(leu_trna3.setInitialAmount(10),             'set initial amount for s1')
    check(leu_trna3.setSubstanceUnits('item'),       'set substance units for s1')
    check(leu_trna3.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(leu_trna3.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    leu_trna3_loaded = model.createSpecies()
    check(leu_trna3_loaded,                                 'create species s1')
    check(leu_trna3_loaded.setId('aminoacylated_MG519'),                     'set species s1 id')
    check(leu_trna3_loaded.setCompartment('c'),            'set species s1 compartment')
    check(leu_trna3_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(leu_trna3_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(leu_trna3_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(leu_trna3_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(leu_trna3_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    leu_trna4 = model.createSpecies()
    check(leu_trna4,                                 'create species s1')
    check(leu_trna4.setId('MG520'),                     'set species s1 id')
    check(leu_trna4.setCompartment('c'),            'set species s1 compartment')
    check(leu_trna4.setConstant(False),              'set "constant" attribute on s1')
    check(leu_trna4.setInitialAmount(10),             'set initial amount for s1')
    check(leu_trna4.setSubstanceUnits('item'),       'set substance units for s1')
    check(leu_trna4.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(leu_trna4.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    leu_trna4_loaded = model.createSpecies()
    check(leu_trna4_loaded,                                 'create species s1')
    check(leu_trna4_loaded.setId('aminoacylated_MG520'),                     'set species s1 id')
    check(leu_trna4_loaded.setCompartment('c'),            'set species s1 compartment')
    check(leu_trna4_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(leu_trna4_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(leu_trna4_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(leu_trna4_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(leu_trna4_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    lys_trna = model.createSpecies()
    check(lys_trna,                                 'create species s1')
    check(lys_trna.setId('MG501'),                     'set species s1 id')
    check(lys_trna.setCompartment('c'),            'set species s1 compartment')
    check(lys_trna.setConstant(False),              'set "constant" attribute on s1')
    check(lys_trna.setInitialAmount(10),             'set initial amount for s1')
    check(lys_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(lys_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(lys_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    lys_trna_loaded = model.createSpecies()
    check(lys_trna_loaded,                                 'create species s1')
    check(lys_trna_loaded.setId('aminoacylated_MG501'),                     'set species s1 id')
    check(lys_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(lys_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(lys_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(lys_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(lys_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(lys_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    lys_trna2 = model.createSpecies()
    check(lys_trna2,                                 'create species s1')
    check(lys_trna2.setId('MG509'),                     'set species s1 id')
    check(lys_trna2.setCompartment('c'),            'set species s1 compartment')
    check(lys_trna2.setConstant(False),              'set "constant" attribute on s1')
    check(lys_trna2.setInitialAmount(10),             'set initial amount for s1')
    check(lys_trna2.setSubstanceUnits('item'),       'set substance units for s1')
    check(lys_trna2.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(lys_trna2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    lys_trna2_loaded = model.createSpecies()
    check(lys_trna2_loaded,                                 'create species s1')
    check(lys_trna2_loaded.setId('aminoacylated_MG509'),                     'set species s1 id')
    check(lys_trna2_loaded.setCompartment('c'),            'set species s1 compartment')
    check(lys_trna2_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(lys_trna2_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(lys_trna2_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(lys_trna2_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(lys_trna2_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    met_trna = model.createSpecies()
    check(met_trna,                                 'create species s1')
    check(met_trna.setId('MG485'),                     'set species s1 id')
    check(met_trna.setCompartment('c'),            'set species s1 compartment')
    check(met_trna.setConstant(False),              'set "constant" attribute on s1')
    check(met_trna.setInitialAmount(10),             'set initial amount for s1')
    check(met_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(met_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(met_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    met_trna_loaded = model.createSpecies()
    check(met_trna_loaded,                                 'create species s1')
    check(met_trna_loaded.setId('aminoacylated_MG485'),                     'set species s1 id')
    check(met_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(met_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(met_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(met_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(met_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(met_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    fmet_trna = model.createSpecies()
    check(fmet_trna,                                 'create species s1')
    check(fmet_trna.setId('MG488'),                     'set species s1 id')
    check(fmet_trna.setCompartment('c'),            'set species s1 compartment')
    check(fmet_trna.setConstant(False),              'set "constant" attribute on s1')
    check(fmet_trna.setInitialAmount(10),             'set initial amount for s1')
    check(fmet_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(fmet_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(fmet_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    fmet_trna_metloaded = model.createSpecies()
    check(fmet_trna_metloaded,                                   'create species s1')
    check(fmet_trna_metloaded.setId('met_aminoacylated_MG488'),  'set species s1 id')
    check(fmet_trna_metloaded.setCompartment('c'),               'set species s1 compartment')
    check(fmet_trna_metloaded.setConstant(False),                'set "constant" attribute on s1')
    check(fmet_trna_metloaded.setInitialAmount(10),               'set initial amount for s1')
    check(fmet_trna_metloaded.setSubstanceUnits('item'),         'set substance units for s1')
    check(fmet_trna_metloaded.setBoundaryCondition(False),       'set "boundaryCondition" on s1')
    check(fmet_trna_metloaded.setHasOnlySubstanceUnits(False),   'set "hasOnlySubstanceUnits" on s1')

    fmet_trna_loaded = model.createSpecies()
    check(fmet_trna_loaded,                                 'create species s1')
    check(fmet_trna_loaded.setId('aminoacylated_MG488'),    'set species s1 id')
    check(fmet_trna_loaded.setCompartment('c'),             'set species s1 compartment')
    check(fmet_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(fmet_trna_loaded.setInitialAmount(1),             'set initial amount for s1')
    check(fmet_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(fmet_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(fmet_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    phe_trna = model.createSpecies()
    check(phe_trna,                                 'create species s1')
    check(phe_trna.setId('MG490'),                     'set species s1 id')
    check(phe_trna.setCompartment('c'),            'set species s1 compartment')
    check(phe_trna.setConstant(False),              'set "constant" attribute on s1')
    check(phe_trna.setInitialAmount(10),             'set initial amount for s1')
    check(phe_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(phe_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(phe_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    phe_trna_loaded = model.createSpecies()
    check(phe_trna_loaded,                                 'create species s1')
    check(phe_trna_loaded.setId('aminoacylated_MG490'),    'set species s1 id')
    check(phe_trna_loaded.setCompartment('c'),             'set species s1 compartment')
    check(phe_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(phe_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(phe_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(phe_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(phe_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    pro_trna = model.createSpecies()
    check(pro_trna,                                 'create species s1')
    check(pro_trna.setId('MG484'),                     'set species s1 id')
    check(pro_trna.setCompartment('c'),            'set species s1 compartment')
    check(pro_trna.setConstant(False),              'set "constant" attribute on s1')
    check(pro_trna.setInitialAmount(10),             'set initial amount for s1')
    check(pro_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(pro_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(pro_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    pro_trna_loaded = model.createSpecies()
    check(pro_trna_loaded,                                 'create species s1')
    check(pro_trna_loaded.setId('aminoacylated_MG484'),                     'set species s1 id')
    check(pro_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(pro_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(pro_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(pro_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(pro_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(pro_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ser_trna = model.createSpecies()
    check(ser_trna,                                 'create species s1')
    check(ser_trna.setId('MG475'),                     'set species s1 id')
    check(ser_trna.setCompartment('c'),            'set species s1 compartment')
    check(ser_trna.setConstant(False),              'set "constant" attribute on s1')
    check(ser_trna.setInitialAmount(10),             'set initial amount for s1')
    check(ser_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(ser_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ser_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ser_trna_loaded = model.createSpecies()
    check(ser_trna_loaded,                                 'create species s1')
    check(ser_trna_loaded.setId('aminoacylated_MG475'),                     'set species s1 id')
    check(ser_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(ser_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(ser_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(ser_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(ser_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ser_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ser_trna2 = model.createSpecies()
    check(ser_trna2,                                 'create species s1')
    check(ser_trna2.setId('MG487'),                     'set species s1 id')
    check(ser_trna2.setCompartment('c'),            'set species s1 compartment')
    check(ser_trna2.setConstant(False),              'set "constant" attribute on s1')
    check(ser_trna2.setInitialAmount(10),             'set initial amount for s1')
    check(ser_trna2.setSubstanceUnits('item'),       'set substance units for s1')
    check(ser_trna2.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ser_trna2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ser_trna2_loaded = model.createSpecies()
    check(ser_trna2_loaded,                                 'create species s1')
    check(ser_trna2_loaded.setId('aminoacylated_MG487'),                     'set species s1 id')
    check(ser_trna2_loaded.setCompartment('c'),            'set species s1 compartment')
    check(ser_trna2_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(ser_trna2_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(ser_trna2_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(ser_trna2_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ser_trna2_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ser_trna3 = model.createSpecies()
    check(ser_trna3,                                 'create species s1')
    check(ser_trna3.setId('MG506'),                     'set species s1 id')
    check(ser_trna3.setCompartment('c'),            'set species s1 compartment')
    check(ser_trna3.setConstant(False),              'set "constant" attribute on s1')
    check(ser_trna3.setInitialAmount(10),             'set initial amount for s1')
    check(ser_trna3.setSubstanceUnits('item'),       'set substance units for s1')
    check(ser_trna3.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ser_trna3.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ser_trna3_loaded = model.createSpecies()
    check(ser_trna3_loaded,                                 'create species s1')
    check(ser_trna3_loaded.setId('aminoacylated_MG506'),                     'set species s1 id')
    check(ser_trna3_loaded.setCompartment('c'),            'set species s1 compartment')
    check(ser_trna3_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(ser_trna3_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(ser_trna3_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(ser_trna3_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ser_trna3_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ser_trna4 = model.createSpecies()
    check(ser_trna4,                                 'create species s1')
    check(ser_trna4.setId('MG507'),                     'set species s1 id')
    check(ser_trna4.setCompartment('c'),            'set species s1 compartment')
    check(ser_trna4.setConstant(False),              'set "constant" attribute on s1')
    check(ser_trna4.setInitialAmount(10),             'set initial amount for s1')
    check(ser_trna4.setSubstanceUnits('item'),       'set substance units for s1')
    check(ser_trna4.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ser_trna4.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ser_trna4_loaded = model.createSpecies()
    check(ser_trna4_loaded,                                 'create species s1')
    check(ser_trna4_loaded.setId('aminoacylated_MG507'),                     'set species s1 id')
    check(ser_trna4_loaded.setCompartment('c'),            'set species s1 compartment')
    check(ser_trna4_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(ser_trna4_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(ser_trna4_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(ser_trna4_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ser_trna4_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    thr_trna = model.createSpecies()
    check(thr_trna,                                 'create species s1')
    check(thr_trna.setId('MG479'),                     'set species s1 id')
    check(thr_trna.setCompartment('c'),            'set species s1 compartment')
    check(thr_trna.setConstant(False),              'set "constant" attribute on s1')
    check(thr_trna.setInitialAmount(10),             'set initial amount for s1')
    check(thr_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(thr_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(thr_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    thr_trna_loaded = model.createSpecies()
    check(thr_trna_loaded,                                 'create species s1')
    check(thr_trna_loaded.setId('aminoacylated_MG479'),                     'set species s1 id')
    check(thr_trna_loaded.setCompartment('c'),            'set species s1 compartment')
    check(thr_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(thr_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(thr_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(thr_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(thr_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    thr_trna2 = model.createSpecies()
    check(thr_trna2,                                 'create species s1')
    check(thr_trna2.setId('MG510'),                     'set species s1 id')
    check(thr_trna2.setCompartment('c'),            'set species s1 compartment')
    check(thr_trna2.setConstant(False),              'set "constant" attribute on s1')
    check(thr_trna2.setInitialAmount(10),             'set initial amount for s1')
    check(thr_trna2.setSubstanceUnits('item'),       'set substance units for s1')
    check(thr_trna2.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(thr_trna2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    thr_trna2_loaded = model.createSpecies()
    check(thr_trna2_loaded,                                 'create species s1')
    check(thr_trna2_loaded.setId('aminoacylated_MG510'),                     'set species s1 id')
    check(thr_trna2_loaded.setCompartment('c'),            'set species s1 compartment')
    check(thr_trna2_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(thr_trna2_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(thr_trna2_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(thr_trna2_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(thr_trna2_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    thr_trna3 = model.createSpecies()
    check(thr_trna3,                                 'create species s1')
    check(thr_trna3.setId('MG512'),                     'set species s1 id')
    check(thr_trna3.setCompartment('c'),            'set species s1 compartment')
    check(thr_trna3.setConstant(False),              'set "constant" attribute on s1')
    check(thr_trna3.setInitialAmount(10),             'set initial amount for s1')
    check(thr_trna3.setSubstanceUnits('item'),       'set substance units for s1')
    check(thr_trna3.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(thr_trna3.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    thr_trna3_loaded = model.createSpecies()
    check(thr_trna3_loaded,                                 'create species s1')
    check(thr_trna3_loaded.setId('aminoacylated_MG512'),                     'set species s1 id')
    check(thr_trna3_loaded.setCompartment('c'),            'set species s1 compartment')
    check(thr_trna3_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(thr_trna3_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(thr_trna3_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(thr_trna3_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(thr_trna3_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    trp_trna = model.createSpecies()
    check(trp_trna,                                 'create species s1')
    check(trp_trna.setId('MG496'),                     'set species s1 id')
    check(trp_trna.setCompartment('c'),            'set species s1 compartment')
    check(trp_trna.setConstant(False),              'set "constant" attribute on s1')
    check(trp_trna.setInitialAmount(10),             'set initial amount for s1')
    check(trp_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(trp_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(trp_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    trp_trna_loaded = model.createSpecies()
    check(trp_trna_loaded,                                 'create species s1')
    check(trp_trna_loaded.setId('aminoacylated_MG496'),    'set species s1 id')
    check(trp_trna_loaded.setCompartment('c'),             'set species s1 compartment')
    check(trp_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(trp_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(trp_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(trp_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(trp_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    trp_trna2 = model.createSpecies()
    check(trp_trna2,                                 'create species s1')
    check(trp_trna2.setId('MG504'),                     'set species s1 id')
    check(trp_trna2.setCompartment('c'),            'set species s1 compartment')
    check(trp_trna2.setConstant(False),              'set "constant" attribute on s1')
    check(trp_trna2.setInitialAmount(10),             'set initial amount for s1')
    check(trp_trna2.setSubstanceUnits('item'),       'set substance units for s1')
    check(trp_trna2.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(trp_trna2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    trp_trna2_loaded = model.createSpecies()
    check(trp_trna2_loaded,                                 'create species s1')
    check(trp_trna2_loaded.setId('aminoacylated_MG504'),    'set species s1 id')
    check(trp_trna2_loaded.setCompartment('c'),             'set species s1 compartment')
    check(trp_trna2_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(trp_trna2_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(trp_trna2_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(trp_trna2_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(trp_trna2_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    tyr_trna = model.createSpecies()
    check(tyr_trna,                                 'create species s1')
    check(tyr_trna.setId('MG503'),                     'set species s1 id')
    check(tyr_trna.setCompartment('c'),            'set species s1 compartment')
    check(tyr_trna.setConstant(False),              'set "constant" attribute on s1')
    check(tyr_trna.setInitialAmount(10),             'set initial amount for s1')
    check(tyr_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(tyr_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(tyr_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    tyr_trna_loaded = model.createSpecies()
    check(tyr_trna_loaded,                                 'create species s1')
    check(tyr_trna_loaded.setId('aminoacylated_MG503'),    'set species s1 id')
    check(tyr_trna_loaded.setCompartment('c'),             'set species s1 compartment')
    check(tyr_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(tyr_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(tyr_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(tyr_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(tyr_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    val_trna = model.createSpecies()
    check(val_trna,                                 'create species s1')
    check(val_trna.setId('MG511'),                     'set species s1 id')
    check(val_trna.setCompartment('c'),            'set species s1 compartment')
    check(val_trna.setConstant(False),              'set "constant" attribute on s1')
    check(val_trna.setInitialAmount(10),             'set initial amount for s1')
    check(val_trna.setSubstanceUnits('item'),       'set substance units for s1')
    check(val_trna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(val_trna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    val_trna_loaded = model.createSpecies()
    check(val_trna_loaded,                                 'create species s1')
    check(val_trna_loaded.setId('aminoacylated_MG511'),    'set species s1 id')
    check(val_trna_loaded.setCompartment('c'),             'set species s1 compartment')
    check(val_trna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(val_trna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(val_trna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(val_trna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(val_trna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    tmrna = model.createSpecies()
    check(tmrna,                                 'create species s1')
    check(tmrna.setId('MG_0004'),                     'set species s1 id')
    check(tmrna.setCompartment('c'),            'set species s1 compartment')
    check(tmrna.setConstant(False),              'set "constant" attribute on s1')
    check(tmrna.setInitialAmount(10),             'set initial amount for s1')
    check(tmrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(tmrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(tmrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    tmrna_loaded = model.createSpecies()
    check(tmrna_loaded,                                 'create species s1')
    check(tmrna_loaded.setId('aminoacylated_MG_0004'),    'set species s1 id')
    check(tmrna_loaded.setCompartment('c'),             'set species s1 compartment')
    check(tmrna_loaded.setConstant(False),              'set "constant" attribute on s1')
    check(tmrna_loaded.setInitialAmount(10),             'set initial amount for s1')
    check(tmrna_loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(tmrna_loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(tmrna_loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create species and set the required attributes - Enzymes
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    ala_trna_ligase = model.createSpecies()
    check(ala_trna_ligase,                                 'create species s1')
    check(ala_trna_ligase.setId('MG_292_TETRAMER'),        'set species s1 id')
    check(ala_trna_ligase.setCompartment('c'),             'set species s1 compartment')
    check(ala_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(ala_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(ala_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(ala_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ala_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    arg_trna_ligase = model.createSpecies()
    check(arg_trna_ligase,                                 'create species s1')
    check(arg_trna_ligase.setId('MG_378_MONOMER'),                     'set species s1 id')
    check(arg_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(arg_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(arg_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(arg_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(arg_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(arg_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    asn_trna_ligase = model.createSpecies()
    check(asn_trna_ligase,                                 'create species s1')
    check(asn_trna_ligase.setId('MG_113_DIMER'),                     'set species s1 id')
    check(asn_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(asn_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(asn_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(asn_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(asn_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(asn_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    asp_trna_ligase = model.createSpecies()
    check(asp_trna_ligase,                                 'create species s1')
    check(asp_trna_ligase.setId('MG_036_DIMER'),                     'set species s1 id')
    check(asp_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(asp_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(asp_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(asp_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(asp_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(asp_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    cys_trna_ligase = model.createSpecies()
    check(cys_trna_ligase,                                 'create species s1')
    check(cys_trna_ligase.setId('MG_253_MONOMER'),                     'set species s1 id')
    check(cys_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(cys_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(cys_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(cys_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(cys_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(cys_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    gln_trna_amidotransferase = model.createSpecies()
    check(gln_trna_amidotransferase,                                 'create species s1')
    check(gln_trna_amidotransferase.setId('MG_098_099_100_TRIMER'),                     'set species s1 id')
    check(gln_trna_amidotransferase.setCompartment('c'),            'set species s1 compartment')
    check(gln_trna_amidotransferase.setConstant(False),              'set "constant" attribute on s1')
    check(gln_trna_amidotransferase.setInitialAmount(10),             'set initial amount for s1')
    check(gln_trna_amidotransferase.setSubstanceUnits('item'),       'set substance units for s1')
    check(gln_trna_amidotransferase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(gln_trna_amidotransferase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    glu_trna_ligase = model.createSpecies()
    check(glu_trna_ligase,                                 'create species s1')
    check(glu_trna_ligase.setId('MG_462_MONOMER'),                     'set species s1 id')
    check(glu_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(glu_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(glu_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(glu_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(glu_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(glu_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    gly_trna_ligase = model.createSpecies()
    check(gly_trna_ligase,                                 'create species s1')
    check(gly_trna_ligase.setId('MG_251_DIMER'),                     'set species s1 id')
    check(gly_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(gly_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(gly_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(gly_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(gly_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(gly_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    his_trna_ligase = model.createSpecies()
    check(his_trna_ligase,                                 'create species s1')
    check(his_trna_ligase.setId('MG_035_DIMER'),                     'set species s1 id')
    check(his_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(his_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(his_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(his_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(his_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(his_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ile_trna_ligase = model.createSpecies()
    check(ile_trna_ligase,                                 'create species s1')
    check(ile_trna_ligase.setId('MG_345_MONOMER'),                     'set species s1 id')
    check(ile_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(ile_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(ile_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(ile_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(ile_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ile_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    leu_trna_ligase = model.createSpecies()
    check(leu_trna_ligase,                                 'create species s1')
    check(leu_trna_ligase.setId('MG_266_MONOMER'),                     'set species s1 id')
    check(leu_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(leu_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(leu_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(leu_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(leu_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(leu_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    lys_trna_ligase = model.createSpecies()
    check(lys_trna_ligase,                                 'create species s1')
    check(lys_trna_ligase.setId('MG_136_DIMER'),                     'set species s1 id')
    check(lys_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(lys_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(lys_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(lys_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(lys_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(lys_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    met_trna_ligase = model.createSpecies()
    check(met_trna_ligase,                                 'create species s1')
    check(met_trna_ligase.setId('MG_021_DIMER'),                     'set species s1 id')
    check(met_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(met_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(met_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(met_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(met_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(met_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    met_trnaformyltrans = model.createSpecies()
    check(met_trnaformyltrans,                                 'create species s1')
    check(met_trnaformyltrans.setId('MG_365_MONOMER'),                     'set species s1 id')
    check(met_trnaformyltrans.setCompartment('c'),            'set species s1 compartment')
    check(met_trnaformyltrans.setConstant(False),              'set "constant" attribute on s1')
    check(met_trnaformyltrans.setInitialAmount(10),             'set initial amount for s1')
    check(met_trnaformyltrans.setSubstanceUnits('item'),       'set substance units for s1')
    check(met_trnaformyltrans.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(met_trnaformyltrans.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    phe_trna_ligase = model.createSpecies()
    check(phe_trna_ligase,                                 'create species s1')
    check(phe_trna_ligase.setId('MG_194_195_TETRAMER'),                     'set species s1 id')
    check(phe_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(phe_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(phe_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(phe_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(phe_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(phe_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    pro_trna_ligase = model.createSpecies()
    check(pro_trna_ligase,                                 'create species s1')
    check(pro_trna_ligase.setId('MG_283_DIMER'),                     'set species s1 id')
    check(pro_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(pro_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(pro_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(pro_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(pro_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(pro_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ser_trna_ligase = model.createSpecies()
    check(ser_trna_ligase,                                 'create species s1')
    check(ser_trna_ligase.setId('MG_005_DIMER'),                     'set species s1 id')
    check(ser_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(ser_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(ser_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(ser_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(ser_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ser_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    thr_trna_ligase = model.createSpecies()
    check(thr_trna_ligase,                                 'create species s1')
    check(thr_trna_ligase.setId('MG_375_DIMER'),                     'set species s1 id')
    check(thr_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(thr_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(thr_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(thr_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(thr_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(thr_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    trp_trna_ligase = model.createSpecies()
    check(trp_trna_ligase,                                 'create species s1')
    check(trp_trna_ligase.setId('MG_126_DIMER'),                     'set species s1 id')
    check(trp_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(trp_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(trp_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(trp_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(trp_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(trp_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    tyr_trna_ligase = model.createSpecies()
    check(tyr_trna_ligase,                                 'create species s1')
    check(tyr_trna_ligase.setId('MG_455_DIMER'),                     'set species s1 id')
    check(tyr_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(tyr_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(tyr_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(tyr_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(tyr_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(tyr_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    val_trna_ligase = model.createSpecies()
    check(val_trna_ligase,                                 'create species s1')
    check(val_trna_ligase.setId('MG_334_MONOMER'),                     'set species s1 id')
    check(val_trna_ligase.setCompartment('c'),            'set species s1 compartment')
    check(val_trna_ligase.setConstant(False),              'set "constant" attribute on s1')
    check(val_trna_ligase.setInitialAmount(10),             'set initial amount for s1')
    check(val_trna_ligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(val_trna_ligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(val_trna_ligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create parameters and set the required attributes
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create a parameter object inside this model, set the required
    # attributes 'id' and 'constant' for a parameter in SBML Level 3, and
    # initialize the parameter with a value along with its units.

    k_mg471_aminoacylation = model.createParameter()
    check(k_mg471_aminoacylation,                                  'create parameter k')
    check(k_mg471_aminoacylation.setId('k_mg471_aminoacylation'),                       'set parameter k id')
    check(k_mg471_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg471_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg471_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg472_aminoacylation = model.createParameter()
    check(k_mg472_aminoacylation,                                  'create parameter k')
    check(k_mg472_aminoacylation.setId('k_mg472_aminoacylation'),                       'set parameter k id')
    check(k_mg472_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg472_aminoacylation.setValue(255.762),                      'set parameter k value')
    check(k_mg472_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg475_aminoacylation = model.createParameter()
    check(k_mg475_aminoacylation,                                  'create parameter k')
    check(k_mg475_aminoacylation.setId('k_mg475_aminoacylation'),                       'set parameter k id')
    check(k_mg475_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg475_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg475_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg479_aminoacylation = model.createParameter()
    check(k_mg479_aminoacylation,                                  'create parameter k')
    check(k_mg479_aminoacylation.setId('k_mg479_aminoacylation'),                       'set parameter k id')
    check(k_mg479_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg479_aminoacylation.setValue(5400),                      'set parameter k value')
    check(k_mg479_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg483_aminoacylation = model.createParameter()
    check(k_mg483_aminoacylation,                                  'create parameter k')
    check(k_mg483_aminoacylation.setId('k_mg483_aminoacylation'),                       'set parameter k id')
    check(k_mg483_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg483_aminoacylation.setValue(8514),                      'set parameter k value')
    check(k_mg483_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg484_aminoacylation = model.createParameter()
    check(k_mg484_aminoacylation,                                  'create parameter k')
    check(k_mg484_aminoacylation.setId('k_mg484_aminoacylation'),                       'set parameter k id')
    check(k_mg484_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg484_aminoacylation.setValue(840),                      'set parameter k value')
    check(k_mg484_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg485_aminoacylation = model.createParameter()
    check(k_mg485_aminoacylation,                                  'create parameter k')
    check(k_mg485_aminoacylation.setId('k_mg485_aminoacylation'),                       'set parameter k id')
    check(k_mg485_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg485_aminoacylation.setValue(192),                      'set parameter k value')
    check(k_mg485_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg486_aminoacylation = model.createParameter()
    check(k_mg486_aminoacylation,                                  'create parameter k')
    check(k_mg486_aminoacylation.setId('k_mg486_aminoacylation'),                       'set parameter k id')
    check(k_mg486_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg486_aminoacylation.setValue(255.762),                      'set parameter k value')
    check(k_mg486_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg487_aminoacylation = model.createParameter()
    check(k_mg487_aminoacylation,                                  'create parameter k')
    check(k_mg487_aminoacylation.setId('k_mg487_aminoacylation'),                       'set parameter k id')
    check(k_mg487_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg487_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg487_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg488_aminoacylation = model.createParameter()
    check(k_mg488_aminoacylation,                                  'create parameter k')
    check(k_mg488_aminoacylation.setId('k_mg488_aminoacylation'),                       'set parameter k id')
    check(k_mg488_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg488_aminoacylation.setValue(192),                      'set parameter k value')
    check(k_mg488_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg488_formyltransferase = model.createParameter()
    check(k_mg488_formyltransferase,                                  'create parameter k')
    check(k_mg488_formyltransferase.setId('k_mg488_formyltransferase'),                       'set parameter k id')
    check(k_mg488_formyltransferase.setConstant(True),                'set parameter k "constant"')
    check(k_mg488_formyltransferase.setValue(456),                      'set parameter k value')
    check(k_mg488_formyltransferase.setUnits('per_minute'),           'set parameter k units')

    k_mg489_aminoacylation = model.createParameter()
    check(k_mg489_aminoacylation,                                  'create parameter k')
    check(k_mg489_aminoacylation.setId('k_mg489_aminoacylation'),                       'set parameter k id')
    check(k_mg489_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg489_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg489_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg490_aminoacylation = model.createParameter()
    check(k_mg490_aminoacylation,                                  'create parameter k')
    check(k_mg490_aminoacylation.setId('k_mg490_aminoacylation'),                       'set parameter k id')
    check(k_mg490_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg490_aminoacylation.setValue(324),                      'set parameter k value')
    check(k_mg490_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg492_aminoacylation = model.createParameter()
    check(k_mg492_aminoacylation,                                  'create parameter k')
    check(k_mg492_aminoacylation.setId('k_mg492_aminoacylation'),                       'set parameter k id')
    check(k_mg492_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg492_aminoacylation.setValue(168),                      'set parameter k value')
    check(k_mg492_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg493_aminoacylation = model.createParameter()
    check(k_mg493_aminoacylation,                                  'create parameter k')
    check(k_mg493_aminoacylation.setId('k_mg493_aminoacylation'),                       'set parameter k id')
    check(k_mg493_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg493_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg493_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg495_aminoacylation = model.createParameter()
    check(k_mg495_aminoacylation,                                  'create parameter k')
    check(k_mg495_aminoacylation.setId('k_mg495_aminoacylation'),                       'set parameter k id')
    check(k_mg495_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg495_aminoacylation.setValue(168),                      'set parameter k value')
    check(k_mg495_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg496_aminoacylation = model.createParameter()
    check(k_mg496_aminoacylation,                                  'create parameter k')
    check(k_mg496_aminoacylation.setId('k_mg496_aminoacylation'),                       'set parameter k id')
    check(k_mg496_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg496_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg496_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg497_aminoacylation = model.createParameter()
    check(k_mg497_aminoacylation,                                  'create parameter k')
    check(k_mg497_aminoacylation.setId('k_mg497_aminoacylation'),                       'set parameter k id')
    check(k_mg497_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg497_aminoacylation.setValue(168),                      'set parameter k value')
    check(k_mg497_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg499_aminoacylation = model.createParameter()
    check(k_mg499_aminoacylation,                                  'create parameter k')
    check(k_mg499_aminoacylation.setId('k_mg499_aminoacylation'),                       'set parameter k id')
    check(k_mg499_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg499_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg499_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg500_aminoacylation = model.createParameter()
    check(k_mg500_aminoacylation,                                  'create parameter k')
    check(k_mg500_aminoacylation.setId('k_mg500_aminoacylation'),                       'set parameter k id')
    check(k_mg500_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg500_aminoacylation.setValue(306),                      'set parameter k value')
    check(k_mg500_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg501_aminoacylation = model.createParameter()
    check(k_mg501_aminoacylation,                                  'create parameter k')
    check(k_mg501_aminoacylation.setId('k_mg501_aminoacylation'),                       'set parameter k id')
    check(k_mg501_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg501_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg501_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg502_aminoacylation = model.createParameter()
    check(k_mg502_aminoacylation,                                  'create parameter k')
    check(k_mg502_aminoacylation.setId('k_mg502_aminoacylation'),                       'set parameter k id')
    check(k_mg502_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg502_aminoacylation.setValue(264),                      'set parameter k value')
    check(k_mg502_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg502_amidotransferase = model.createParameter()
    check(k_mg502_amidotransferase,                                  'create parameter k')
    check(k_mg502_amidotransferase.setId('k_mg502_amidotransferase'),                       'set parameter k id')
    check(k_mg502_amidotransferase.setConstant(True),                'set parameter k "constant"')
    check(k_mg502_amidotransferase.setValue(57.6),                      'set parameter k value')
    check(k_mg502_amidotransferase.setUnits('per_minute'),           'set parameter k units')

    k_mg503_aminoacylation = model.createParameter()
    check(k_mg503_aminoacylation,                                  'create parameter k')
    check(k_mg503_aminoacylation.setId('k_mg503_aminoacylation'),                       'set parameter k id')
    check(k_mg503_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg503_aminoacylation.setValue(44.4),                      'set parameter k value')
    check(k_mg503_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg504_aminoacylation = model.createParameter()
    check(k_mg504_aminoacylation,                                  'create parameter k')
    check(k_mg504_aminoacylation.setId('k_mg504_aminoacylation'),                       'set parameter k id')
    check(k_mg504_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg504_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg504_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg506_aminoacylation = model.createParameter()
    check(k_mg506_aminoacylation,                                  'create parameter k')
    check(k_mg506_aminoacylation.setId('k_mg506_aminoacylation'),                       'set parameter k id')
    check(k_mg506_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg506_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg506_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg507_aminoacylation = model.createParameter()
    check(k_mg507_aminoacylation,                                  'create parameter k')
    check(k_mg507_aminoacylation.setId('k_mg507_aminoacylation'),                       'set parameter k id')
    check(k_mg507_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg507_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg507_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg508_aminoacylation = model.createParameter()
    check(k_mg508_aminoacylation,                                  'create parameter k')
    check(k_mg508_aminoacylation.setId('k_mg508_aminoacylation'),  'set parameter k id')
    check(k_mg508_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg508_aminoacylation.setValue(306),                    'set parameter k value')
    check(k_mg508_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg509_aminoacylation = model.createParameter()
    check(k_mg509_aminoacylation,                                  'create parameter k')
    check(k_mg509_aminoacylation.setId('k_mg509_aminoacylation'),                       'set parameter k id')
    check(k_mg509_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg509_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg509_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg510_aminoacylation = model.createParameter()
    check(k_mg510_aminoacylation,                                  'create parameter k')
    check(k_mg510_aminoacylation.setId('k_mg510_aminoacylation'),                       'set parameter k id')
    check(k_mg510_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg510_aminoacylation.setValue(5400),                      'set parameter k value')
    check(k_mg510_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg511_aminoacylation = model.createParameter()
    check(k_mg511_aminoacylation,                                  'create parameter k')
    check(k_mg511_aminoacylation.setId('k_mg511_aminoacylation'),                       'set parameter k id')
    check(k_mg511_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg511_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg511_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg512_aminoacylation = model.createParameter()
    check(k_mg512_aminoacylation,                                  'create parameter k')
    check(k_mg512_aminoacylation.setId('k_mg512_aminoacylation'),                       'set parameter k id')
    check(k_mg512_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg512_aminoacylation.setValue(5400),                      'set parameter k value')
    check(k_mg512_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg513_aminoacylation = model.createParameter()
    check(k_mg513_aminoacylation,                                  'create parameter k')
    check(k_mg513_aminoacylation.setId('k_mg513_aminoacylation'),                       'set parameter k id')
    check(k_mg513_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg513_aminoacylation.setValue(264),                      'set parameter k value')
    check(k_mg513_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg514_aminoacylation = model.createParameter()
    check(k_mg514_aminoacylation,                                  'create parameter k')
    check(k_mg514_aminoacylation.setId('k_mg514_aminoacylation'),  'set parameter k id')
    check(k_mg514_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg514_aminoacylation.setValue(1620),                   'set parameter k value')
    check(k_mg514_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg518_aminoacylation = model.createParameter()
    check(k_mg518_aminoacylation,                                  'create parameter k')
    check(k_mg518_aminoacylation.setId('k_mg518_aminoacylation'),  'set parameter k id')
    check(k_mg518_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg518_aminoacylation.setValue(8520),                   'set parameter k value')
    check(k_mg518_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg519_aminoacylation = model.createParameter()
    check(k_mg519_aminoacylation,                                  'create parameter k')
    check(k_mg519_aminoacylation.setId('k_mg519_aminoacylation'),  'set parameter k id')
    check(k_mg519_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg519_aminoacylation.setValue(306),                    'set parameter k value')
    check(k_mg519_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg520_aminoacylation = model.createParameter()
    check(k_mg520_aminoacylation,                                  'create parameter k')
    check(k_mg520_aminoacylation.setId('k_mg520_aminoacylation'),  'set parameter k id')
    check(k_mg520_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg520_aminoacylation.setValue(306),                    'set parameter k value')
    check(k_mg520_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg523_aminoacylation = model.createParameter()
    check(k_mg523_aminoacylation,                                  'create parameter k')
    check(k_mg523_aminoacylation.setId('k_mg523_aminoacylation'),  'set parameter k id')
    check(k_mg523_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg523_aminoacylation.setValue(168),                    'set parameter k value')
    check(k_mg523_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    k_mg_0004_aminoacylation = model.createParameter()
    check(k_mg_0004_aminoacylation,                                  'create parameter k')
    check(k_mg_0004_aminoacylation.setId('k_mg_0004_aminoacylation'),                       'set parameter k id')
    check(k_mg_0004_aminoacylation.setConstant(True),                'set parameter k "constant"')
    check(k_mg_0004_aminoacylation.setValue(456),                      'set parameter k value')
    check(k_mg_0004_aminoacylation.setUnits('per_minute'),           'set parameter k units')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG471 tRNA aminoacylation (Alanine)
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

    mg471aminoacylenzyme = mg471aminoacyl.createModifier()
    check(mg471aminoacylenzyme,                       'create reactant')
    check(mg471aminoacylenzyme.setSpecies('MG_292_TETRAMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg471_aminoacylation * MG_292_TETRAMER * MG471 * ALA * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg471aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG472 tRNA aminoacylation (Isoleucine)
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

    mg472aminoacylenzyme = mg472aminoacyl.createModifier()
    check(mg472aminoacylenzyme,                       'create reactant')
    check(mg472aminoacylenzyme.setSpecies('MG_345_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg472_aminoacylation * MG_345_MONOMER * MG472 * ILE * ATP ')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg472aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG475 tRNA aminoacylation (Serine)
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

    mg475aminoacylenzyme = mg475aminoacyl.createModifier()
    check(mg475aminoacylenzyme,                       'create reactant')
    check(mg475aminoacylenzyme.setSpecies('MG_005_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg475_aminoacylation * MG_005_DIMER * MG475 * SER * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg475aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG479 tRNA aminoacylation (Threonine)
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg479aminoacyl = model.createReaction()
    check(mg479aminoacyl,                                 'create reaction')
    check(mg479aminoacyl.setId('MG479_Aminoacylation'),                     'set reaction id')
    check(mg479aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg479aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg479aminoacylreact1 = mg479aminoacyl.createReactant()
    check(mg479aminoacylreact1,                       'create reactant')
    check(mg479aminoacylreact1.setSpecies('THR'),      'assign reactant species')
    check(mg479aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg479aminoacylreact2 = mg479aminoacyl.createReactant()
    check(mg479aminoacylreact2,                       'create reactant')
    check(mg479aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg479aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg479aminoacylreact3 = mg479aminoacyl.createReactant()
    check(mg479aminoacylreact3,                       'create reactant')
    check(mg479aminoacylreact3.setSpecies('MG479'),      'assign reactant species')
    check(mg479aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg479aminoacylenzyme = mg479aminoacyl.createModifier()
    check(mg479aminoacylenzyme,                       'create reactant')
    check(mg479aminoacylenzyme.setSpecies('MG_375_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg479_aminoacylation * MG_375_DIMER * MG479 * THR * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg479aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG483 tRNA aminoacylation (Cysteine)
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

    mg483aminoacylenzyme = mg483aminoacyl.createModifier()
    check(mg483aminoacylenzyme,                       'create reactant')
    check(mg483aminoacylenzyme.setSpecies('MG_253_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg483_aminoacylation * MG_253_MONOMER * MG483 * CYS * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg483aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG484 tRNA aminoacylation (Proline)
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

    mg484aminoacylenzyme = mg484aminoacyl.createModifier()
    check(mg484aminoacylenzyme,                       'create reactant')
    check(mg484aminoacylenzyme.setSpecies('MG_283_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg484_aminoacylation * MG_283_DIMER * MG484 * PRO * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg484aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG485 tRNA aminoacylation (Methionine)
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

    mg485aminoacylenzyme = mg485aminoacyl.createModifier()
    check(mg485aminoacylenzyme,                       'create reactant')
    check(mg485aminoacylenzyme.setSpecies('MG_021_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg485_aminoacylation * MG_021_DIMER * MG485 * MET * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg485aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG486 tRNA aminoacylation (Isoleucine)
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

    mg486aminoenzyme = mg486aminoacyl.createModifier()
    check(mg486aminoenzyme,                       'create reactant')
    check(mg486aminoenzyme.setSpecies('MG_345_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg486_aminoacylation * MG_345_MONOMER * MG486 * ILE * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg486aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG487 tRNA aminoacylation (Serine)
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

    mg487aminoacylenzyme = mg487aminoacyl.createModifier()
    check(mg487aminoacylenzyme,                       'create reactant')
    check(mg487aminoacylenzyme.setSpecies('MG_005_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg487_aminoacylation * MG_005_DIMER * MG487 * SER * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg487aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG488 tRNA aminoacylation (formyl-Methionine)
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

    mg488aminoacylenzyme = mg488aminoacyl.createModifier()
    check(mg488aminoacylenzyme,                       'create reactant')
    check(mg488aminoacylenzyme.setSpecies('MG_021_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg488_aminoacylation * MG_021_DIMER * MG488 * MET * ATP')
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

    mg488methtransenzyme = mg488methtrans.createModifier()
    check(mg488methtransenzyme,                       'create reactant')
    check(mg488methtransenzyme.setSpecies('MG_365_MONOMER'),      'assign reactant species')

    mg488methtransprod1 = mg488methtrans.createProduct()
    check(mg488methtransprod1,                       'create product')
    check(mg488methtransprod1.setSpecies('THF'),      'assign product species')
    check(mg488methtransprod1.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg488methtransprod2 = mg488methtrans.createProduct()
    check(mg488methtransprod2,                       'create product')
    check(mg488methtransprod2.setSpecies('aminoacylated_MG488'),      'assign product species')
    check(mg488methtransprod2.setConstant(False),     'set "constant" on species ref 2')

    math_ast = sbml.parseL3Formula('k_mg488_formyltransferase * MG_365_MONOMER * met_aminoacylated_MG488 * H2O * FTHF10')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg488methtrans.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG489 tRNA aminoacylation (Aspartic acid)
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

    mg489aminoacylenzyme = mg489aminoacyl.createModifier()
    check(mg489aminoacylenzyme,                       'create reactant')
    check(mg489aminoacylenzyme.setSpecies('MG_036_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg489_aminoacylation * MG_036_DIMER * MG489 * ASP * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg489aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG490 tRNA aminoacylation (Phenylalanine)
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

    mg490aminoacylenzyme = mg490aminoacyl.createModifier()
    check(mg490aminoacylenzyme,                       'create reactant')
    check(mg490aminoacylenzyme.setSpecies('MG_194_195_TETRAMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg490_aminoacylation * MG_194_195_TETRAMER * MG490 * PHE * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg490aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG492 tRNA aminoacylation (Arginine)
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

    mg492aminoacylenzyme = mg492aminoacyl.createModifier()
    check(mg492aminoacylenzyme,                       'create reactant')
    check(mg492aminoacylenzyme.setSpecies('MG_378_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg492_aminoacylation * MG_378_MONOMER * MG492 * ARG * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg492aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG493 tRNA aminoacylation (Glycine)
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

    mg493aminoacylenzyme = mg493aminoacyl.createModifier()
    check(mg493aminoacylenzyme,                       'create reactant')
    check(mg493aminoacylenzyme.setSpecies('MG_251_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg493_aminoacylation * MG_251_DIMER * MG493 * GLY * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg493aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG495 tRNA aminoacylation (Arginine)
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

    mg495aminoacylenzyme = mg495aminoacyl.createModifier()
    check(mg495aminoacylenzyme,                       'create reactant')
    check(mg495aminoacylenzyme.setSpecies('MG_378_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg495_aminoacylation * MG_378_MONOMER * MG495 * ARG * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg495aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG496 tRNA aminoacylation (Tryptophan)
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

    mg496aminoacylenzyme = mg496aminoacyl.createModifier()
    check(mg496aminoacylenzyme,                       'create reactant')
    check(mg496aminoacylenzyme.setSpecies('MG_126_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg496_aminoacylation * MG_126_DIMER * MG496 * TRP * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg496aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG497 tRNA aminoacylation (Arginine)
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

    mg497aminoacylenzyme = mg497aminoacyl.createModifier()
    check(mg497aminoacylenzyme,                       'create reactant')
    check(mg497aminoacylenzyme.setSpecies('MG_378_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg497_aminoacylation * MG_378_MONOMER * MG497 * ARG * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg497aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG499 tRNA aminoacylation (Glycine)
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

    mg499aminoacylenzyme = mg499aminoacyl.createModifier()
    check(mg499aminoacylenzyme,                       'create reactant')
    check(mg499aminoacylenzyme.setSpecies('MG_251_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg499_aminoacylation * MG_251_DIMER * MG499 * GLY * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg499aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG500 tRNA aminoacylation (Leucine)
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

    mg500aminoacylenzyme = mg500aminoacyl.createModifier()
    check(mg500aminoacylenzyme,                       'create reactant')
    check(mg500aminoacylenzyme.setSpecies('MG_266_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg500_aminoacylation * MG_266_MONOMER * MG500 * LEU * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg500aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG501 tRNA aminoacylation (Lysine)
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

    mg501aminoacylenzyme = mg501aminoacyl.createModifier()
    check(mg501aminoacylenzyme,                       'create reactant')
    check(mg501aminoacylenzyme.setSpecies('MG_136_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg501_aminoacylation * MG_136_DIMER * MG501 * LYS * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg501aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG502 tRNA aminoacylation (Glutamine)
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

    mg502aminoacylenzyme = mg502aminoacyl.createModifier()
    check(mg502aminoacylenzyme,                       'create reactant')
    check(mg502aminoacylenzyme.setSpecies('MG_462_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg502_aminoacylation * MG_462_MONOMER * MG502 * GLU * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg502aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    # ---------------------
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

    mg502amidotransreact4 = mg502amidotrans.createReactant()
    check(mg502amidotransreact4,                       'create reactant')
    check(mg502amidotransreact4.setSpecies('H2O'),      'assign reactant species')
    check(mg502amidotransreact4.setConstant(False),     'set "constant" on species ref 1')

    mg502amidotransenzyme = mg502amidotrans.createModifier()
    check(mg502amidotransenzyme,                       'create reactant')
    check(mg502amidotransenzyme.setSpecies('MG_098_099_100_TRIMER'),      'assign reactant species')

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

    mg502amidotransprod4 = mg502amidotrans.createProduct()
    check(mg502amidotransprod4,                       'create product')
    check(mg502amidotransprod4.setSpecies('H'),      'assign product species')
    check(mg502amidotransprod4.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg502amidotransprod5 = mg502amidotrans.createProduct()
    check(mg502amidotransprod5,                       'create product')
    check(mg502amidotransprod5.setSpecies('aminoacylated_MG502'),      'assign product species')
    check(mg502amidotransprod5.setConstant(False),     'set "constant" on species ref 2')

    math_ast = sbml.parseL3Formula('k_mg502_amidotransferase * MG_098_099_100_TRIMER * GLU_aminoacylated_MG502 * GLN * ATP * H2O')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg502amidotrans.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG503 tRNA aminoacylation (Tyrosine)
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

    mg503aminoacylenzyme = mg503aminoacyl.createModifier()
    check(mg503aminoacylenzyme,                       'create reactant')
    check(mg503aminoacylenzyme.setSpecies('MG_455_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg503_aminoacylation * MG_455_DIMER * MG503 * TYR * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg503aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG504 tRNA aminoacylation (Tryptophan)
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

    mg504aminoacylenzyme = mg504aminoacyl.createModifier()
    check(mg504aminoacylenzyme,                       'create reactant')
    check(mg504aminoacylenzyme.setSpecies('MG_126_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg504_aminoacylation * MG_126_DIMER * MG504 * TRP * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg504aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG506 tRNA aminoacylation (Serine)
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

    mg506aminoacylenzyme = mg506aminoacyl.createModifier()
    check(mg506aminoacylenzyme,                       'create reactant')
    check(mg506aminoacylenzyme.setSpecies('MG_005_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg506_aminoacylation * MG_005_DIMER * MG506 * SER * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg506aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG507 tRNA aminoacylation (Serine)
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

    mg507aminoacylenzyme = mg507aminoacyl.createModifier()
    check(mg507aminoacylenzyme,                       'create reactant')
    check(mg507aminoacylenzyme.setSpecies('MG_005_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg507_aminoacylation * MG_005_DIMER * MG507 * SER * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg507aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG508 tRNA aminoacylation (Leucine)
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

    mg508aminoacylenzyme = mg508aminoacyl.createModifier()
    check(mg508aminoacylenzyme,                       'create reactant')
    check(mg508aminoacylenzyme.setSpecies('MG_266_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg508_aminoacylation * MG_266_MONOMER * MG508 * LEU * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg508aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG509 tRNA aminoacylation (Lysine)
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

    mg509aminoacylenzyme = mg509aminoacyl.createModifier()
    check(mg509aminoacylenzyme,                       'create reactant')
    check(mg509aminoacylenzyme.setSpecies('MG_136_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg509_aminoacylation * MG_136_DIMER * MG509 * LYS * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg509aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG510 tRNA aminoacylation (Threonine)
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

    mg510aminoacylenzyme = mg510aminoacyl.createModifier()
    check(mg510aminoacylenzyme,                       'create reactant')
    check(mg510aminoacylenzyme.setSpecies('MG_375_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg510_aminoacylation * MG_375_DIMER * MG510 * THR * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg510aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG511 tRNA aminoacylation (Valine)
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

    mg511aminoacylenzyme = mg511aminoacyl.createModifier()
    check(mg511aminoacylenzyme,                       'create reactant')
    check(mg511aminoacylenzyme.setSpecies('MG_334_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg511_aminoacylation * MG_334_MONOMER * MG511 * VAL * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg511aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG512 tRNA aminoacylation (Threonine)
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

    mg512aminoacylenzyme = mg512aminoacyl.createModifier()
    check(mg512aminoacylenzyme,                       'create reactant')
    check(mg512aminoacylenzyme.setSpecies('MG_375_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg512_aminoacylation * MG_375_DIMER * MG512 * THR * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg512aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG513 tRNA aminoacylation (Glutamate)
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

    mg513aminoacylenzyme = mg513aminoacyl.createModifier()
    check(mg513aminoacylenzyme,                       'create reactant')
    check(mg513aminoacylenzyme.setSpecies('MG_462_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg513_aminoacylation * MG_462_MONOMER * MG513 * GLU * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg513aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG514 tRNA aminoacylation (Asparagine)
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

    mg514aminoacylenzyme = mg514aminoacyl.createModifier()
    check(mg514aminoacylenzyme,                       'create reactant')
    check(mg514aminoacylenzyme.setSpecies('MG_113_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg514_aminoacylation * MG_113_DIMER * MG514 * ASN * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg514aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG518 tRNA aminoacylation (Histidine)
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

    mg518aminoacylenzyme = mg518aminoacyl.createModifier()
    check(mg518aminoacylenzyme,                       'create reactant')
    check(mg518aminoacylenzyme.setSpecies('MG_035_DIMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg518_aminoacylation * MG_035_DIMER * MG518 * HIS * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg518aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG519 tRNA aminoacylation (Leucine)
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

    mg519aminoacylenzyme = mg519aminoacyl.createModifier()
    check(mg519aminoacylenzyme,                       'create reactant')
    check(mg519aminoacylenzyme.setSpecies('MG_266_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg519_aminoacylation * MG_266_MONOMER * MG519 * LEU * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg519aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG520 tRNA aminoacylation (Leucine)
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

    mg520aminoacylenzyme = mg520aminoacyl.createModifier()
    check(mg520aminoacylenzyme,                       'create reactant')
    check(mg520aminoacylenzyme.setSpecies('MG_266_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg520_aminoacylation * MG_266_MONOMER * MG520 * LEU * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg520aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG523 tRNA aminoacylation (Arginine)
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

    mg523aminoacylenzyme = mg523aminoacyl.createModifier()
    check(mg523aminoacylenzyme,                       'create reactant')
    check(mg523aminoacylenzyme.setSpecies('MG_378_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k_mg523_aminoacylation * MG_378_MONOMER * MG523 * ARG * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg523aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Create reactions and set the required attributes - MG_0004 tmRNA aminoacylation
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    mg_0004_aminoacyl = model.createReaction()
    check(mg_0004_aminoacyl,                                 'create reaction')
    check(mg_0004_aminoacyl.setId('MG_0004_Aminoacylation'),                     'set reaction id')
    check(mg_0004_aminoacyl.setReversible(False),            'set reaction reversibility flag')
    check(mg_0004_aminoacyl.setFast(False),                  'set reaction "fast" attribute')

    mg_0004_aminoacylreact1 = mg_0004_aminoacyl.createReactant()
    check(mg_0004_aminoacylreact1,                       'create reactant')
    check(mg_0004_aminoacylreact1.setSpecies('ALA'),      'assign reactant species')
    check(mg_0004_aminoacylreact1.setConstant(False),     'set "constant" on species ref 1')

    mg_0004_aminoacylreact2 = mg_0004_aminoacyl.createReactant()
    check(mg_0004_aminoacylreact2,                       'create reactant')
    check(mg_0004_aminoacylreact2.setSpecies('ATP'),      'assign reactant species')
    check(mg_0004_aminoacylreact2.setConstant(False),     'set "constant" on species ref 1')

    mg_0004_aminoacylreact3 = mg_0004_aminoacyl.createReactant()
    check(mg_0004_aminoacylreact3,                       'create reactant')
    check(mg_0004_aminoacylreact3.setSpecies('MG_0004'),      'assign reactant species')
    check(mg_0004_aminoacylreact3.setConstant(False),     'set "constant" on species ref 1')

    mg_0004_aminoacylenzyme = mg_0004_aminoacyl.createModifier()
    check(mg_0004_aminoacylenzyme,                       'create reactant')
    check(mg_0004_aminoacylenzyme.setSpecies('MG_292_TETRAMER'),      'assign reactant species')

    mg_0004_aminoacylprod1 = mg_0004_aminoacyl.createProduct()
    check(mg_0004_aminoacylprod1,                       'create product')
    check(mg_0004_aminoacylprod1.setSpecies('AMP'),      'assign product species')
    check(mg_0004_aminoacylprod1.setConstant(False),     'set "constant" on species ref 2')

    mg_0004_aminoacylprod2 = mg_0004_aminoacyl.createProduct()
    check(mg_0004_aminoacylprod2,                       'create product')
    check(mg_0004_aminoacylprod2.setSpecies('PPI'),      'assign product species')
    check(mg_0004_aminoacylprod2.setConstant(False),     'set "constant" on species ref 2')

    # FIX FROM HERE
    mg_0004_aminoacylprod3 = mg_0004_aminoacyl.createProduct()
    check(mg_0004_aminoacylprod3,                       'create product')
    check(mg_0004_aminoacylprod3.setSpecies('aminoacylated_MG_0004'),      'assign product species')
    check(mg_0004_aminoacylprod3.setConstant(False),     'set "constant" on species ref 2')

    math_ast = sbml.parseL3Formula('k_mg_0004_aminoacylation * MG_292_TETRAMER * MG_0004 * ALA * ATP')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg_0004_aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Write script output - SBML model of aminoacylation as a .XML file
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

    # write the aminoacylation model to an xml file
    sbml.writeSBMLToFile(document, os.path.join('C:\\wc\\2014_VW_modelling_workshop\\wholecell-translation', 'aminoacylation.xml'))

    # return a text string containing the model in XML format.
    return sbml.writeSBMLToString(document)

# if you are a UNIX hacker then you can produce the xml files from bash/terminal:
#       python createAminoAcylation.py > aminoacylation.xml
if __name__ == '__main__':
    print(create_model())