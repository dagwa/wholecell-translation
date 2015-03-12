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

    # Create a compartment inside this model, and set the required
    # attributes for an SBML compartment in SBML Level 3.

    cytocompartment = model.createCompartment()
    check(cytocompartment,                                 'create compartment')
    check(cytocompartment.setId('c'),                     'set compartment id')
    check(cytocompartment.setConstant(True),               'set compartment "constant"')
    check(cytocompartment.setSize(0.01),                   'set compartment "size"')
    check(cytocompartment.setSpatialDimensions(3),         'set compartment dimensions')
    check(cytocompartment.setUnits('litre'),               'set compartment size units')

    # Create species for the model, set the required attributes
    # for each species in SBML Level 3 (which are the 'id', 'compartment',
    # 'constant', 'hasOnlySubstanceUnits', and 'boundaryCondition'
    # attributes), and initialize the amount of the species along with the
    # units of the amount.

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Metabolites
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    atp = model.createSpecies()
    check(atp,                                 'create species s1')
    check(atp.setId('ATP'),                     'set species s1 id')
    check(atp.setCompartment('c'),            'set species s1 compartment')
    check(atp.setConstant(False),              'set "constant" attribute on s1')
    check(atp.setInitialAmount(0),             'set initial amount for s1')
    check(atp.setSubstanceUnits('item'),       'set substance units for s1')
    check(atp.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(atp.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    amp = model.createSpecies()
    check(amp,                                 'create species s1')
    check(amp.setId('AMP'),                     'set species s1 id')
    check(amp.setCompartment('c'),            'set species s1 compartment')
    check(amp.setConstant(False),              'set "constant" attribute on s1')
    check(amp.setInitialAmount(0),             'set initial amount for s1')
    check(amp.setSubstanceUnits('item'),       'set substance units for s1')
    check(amp.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(amp.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    fthf10 = model.createSpecies()
    check(fthf10,                                 'create species s1')
    check(fthf10.setId('FTHF10'),                     'set species s1 id')
    check(fthf10.setCompartment('c'),            'set species s1 compartment')
    check(fthf10.setConstant(False),              'set "constant" attribute on s1')
    check(fthf10.setInitialAmount(0),             'set initial amount for s1')
    check(fthf10.setSubstanceUnits('item'),       'set substance units for s1')
    check(fthf10.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(fthf10.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    ppi = model.createSpecies()
    check(ppi,                                 'create species s1')
    check(ppi.setId('PPI'),                     'set species s1 id')
    check(ppi.setCompartment('c'),            'set species s1 compartment')
    check(ppi.setConstant(False),              'set "constant" attribute on s1')
    check(ppi.setInitialAmount(0),             'set initial amount for s1')
    check(ppi.setSubstanceUnits('item'),       'set substance units for s1')
    check(ppi.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(ppi.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    thf = model.createSpecies()
    check(thf,                                 'create species s1')
    check(thf.setId('THF'),                     'set species s1 id')
    check(thf.setCompartment('c'),            'set species s1 compartment')
    check(thf.setConstant(False),              'set "constant" attribute on s1')
    check(thf.setInitialAmount(0),             'set initial amount for s1')
    check(thf.setSubstanceUnits('item'),       'set substance units for s1')
    check(thf.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(thf.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    water = model.createSpecies()
    check(water,                                 'create species s1')
    check(water.setId('H2O'),                     'set species s1 id')
    check(water.setCompartment('c'),            'set species s1 compartment')
    check(water.setConstant(False),              'set "constant" attribute on s1')
    check(water.setInitialAmount(0),             'set initial amount for s1')
    check(water.setSubstanceUnits('item'),       'set substance units for s1')
    check(water.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(water.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    alanine = model.createSpecies()
    check(alanine,                                 'create species s1')
    check(alanine.setId('ALA'),                     'set species s1 id')
    check(alanine.setCompartment('c'),            'set species s1 compartment')
    check(alanine.setConstant(False),              'set "constant" attribute on s1')
    check(alanine.setInitialAmount(0),             'set initial amount for s1')
    check(alanine.setSubstanceUnits('item'),       'set substance units for s1')
    check(alanine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(alanine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    arginine = model.createSpecies()
    check(arginine,                                 'create species s1')
    check(arginine.setId('ARG'),                     'set species s1 id')
    check(arginine.setCompartment('c'),            'set species s1 compartment')
    check(arginine.setConstant(False),              'set "constant" attribute on s1')
    check(arginine.setInitialAmount(0),             'set initial amount for s1')
    check(arginine.setSubstanceUnits('item'),       'set substance units for s1')
    check(arginine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(arginine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    aspartate = model.createSpecies()
    check(aspartate,                                 'create species s1')
    check(aspartate.setId('ASP'),                     'set species s1 id')
    check(aspartate.setCompartment('c'),            'set species s1 compartment')
    check(aspartate.setConstant(False),              'set "constant" attribute on s1')
    check(aspartate.setInitialAmount(0),             'set initial amount for s1')
    check(aspartate.setSubstanceUnits('item'),       'set substance units for s1')
    check(aspartate.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(aspartate.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    cysteine = model.createSpecies()
    check(cysteine,                                 'create species s1')
    check(cysteine.setId('CYS'),                     'set species s1 id')
    check(cysteine.setCompartment('c'),            'set species s1 compartment')
    check(cysteine.setConstant(False),              'set "constant" attribute on s1')
    check(cysteine.setInitialAmount(0),             'set initial amount for s1')
    check(cysteine.setSubstanceUnits('item'),       'set substance units for s1')
    check(cysteine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(cysteine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    glycine = model.createSpecies()
    check(glycine,                                 'create species s1')
    check(glycine.setId('GLY'),                     'set species s1 id')
    check(glycine.setCompartment('c'),            'set species s1 compartment')
    check(glycine.setConstant(False),              'set "constant" attribute on s1')
    check(glycine.setInitialAmount(0),             'set initial amount for s1')
    check(glycine.setSubstanceUnits('item'),       'set substance units for s1')
    check(glycine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(glycine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    isoleucine = model.createSpecies()
    check(isoleucine,                                 'create species s1')
    check(isoleucine.setId('ILE'),                     'set species s1 id')
    check(isoleucine.setCompartment('c'),            'set species s1 compartment')
    check(isoleucine.setConstant(False),              'set "constant" attribute on s1')
    check(isoleucine.setInitialAmount(0),             'set initial amount for s1')
    check(isoleucine.setSubstanceUnits('item'),       'set substance units for s1')
    check(isoleucine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(isoleucine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    methionine = model.createSpecies()
    check(methionine,                                 'create species s1')
    check(methionine.setId('MET'),                     'set species s1 id')
    check(methionine.setCompartment('c'),            'set species s1 compartment')
    check(methionine.setConstant(False),              'set "constant" attribute on s1')
    check(methionine.setInitialAmount(0),             'set initial amount for s1')
    check(methionine.setSubstanceUnits('item'),       'set substance units for s1')
    check(methionine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(methionine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    phenylalanine = model.createSpecies()
    check(phenylalanine,                                 'create species s1')
    check(phenylalanine.setId('PHE'),                     'set species s1 id')
    check(phenylalanine.setCompartment('c'),            'set species s1 compartment')
    check(phenylalanine.setConstant(False),              'set "constant" attribute on s1')
    check(phenylalanine.setInitialAmount(0),             'set initial amount for s1')
    check(phenylalanine.setSubstanceUnits('item'),       'set substance units for s1')
    check(phenylalanine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(phenylalanine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    proline = model.createSpecies()
    check(proline,                                 'create species s1')
    check(proline.setId('PRO'),                     'set species s1 id')
    check(proline.setCompartment('c'),            'set species s1 compartment')
    check(proline.setConstant(False),              'set "constant" attribute on s1')
    check(proline.setInitialAmount(0),             'set initial amount for s1')
    check(proline.setSubstanceUnits('item'),       'set substance units for s1')
    check(proline.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(proline.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    serine = model.createSpecies()
    check(serine,                                 'create species s1')
    check(serine.setId('SER'),                     'set species s1 id')
    check(serine.setCompartment('c'),            'set species s1 compartment')
    check(serine.setConstant(False),              'set "constant" attribute on s1')
    check(serine.setInitialAmount(0),             'set initial amount for s1')
    check(serine.setSubstanceUnits('item'),       'set substance units for s1')
    check(serine.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(serine.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    tryptophan = model.createSpecies()
    check(tryptophan,                                 'create species s1')
    check(tryptophan.setId('TRP'),                     'set species s1 id')
    check(tryptophan.setCompartment('c'),            'set species s1 compartment')
    check(tryptophan.setConstant(False),              'set "constant" attribute on s1')
    check(tryptophan.setInitialAmount(0),             'set initial amount for s1')
    check(tryptophan.setSubstanceUnits('item'),       'set substance units for s1')
    check(tryptophan.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(tryptophan.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # tRNAs: unloaded and loaded
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    alatrna = model.createSpecies()
    check(alatrna,                                 'create species s1')
    check(alatrna.setId('MG471'),                     'set species s1 id')
    check(alatrna.setCompartment('c'),            'set species s1 compartment')
    check(alatrna.setConstant(False),              'set "constant" attribute on s1')
    check(alatrna.setInitialAmount(0),             'set initial amount for s1')
    check(alatrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(alatrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(alatrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    alatrnaloaded = model.createSpecies()
    check(alatrnaloaded,                                 'create species s1')
    check(alatrnaloaded.setId('aminoacylated_MG471'),                     'set species s1 id')
    check(alatrnaloaded.setCompartment('c'),            'set species s1 compartment')
    check(alatrnaloaded.setConstant(False),              'set "constant" attribute on s1')
    check(alatrnaloaded.setInitialAmount(0),             'set initial amount for s1')
    check(alatrnaloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(alatrnaloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(alatrnaloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    argtrna = model.createSpecies()
    check(argtrna,                                 'create species s1')
    check(argtrna.setId('MG492'),                     'set species s1 id')
    check(argtrna.setCompartment('c'),            'set species s1 compartment')
    check(argtrna.setConstant(False),              'set "constant" attribute on s1')
    check(argtrna.setInitialAmount(0),             'set initial amount for s1')
    check(argtrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(argtrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(argtrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    argtrnaloaded = model.createSpecies()
    check(argtrnaloaded,                                 'create species s1')
    check(argtrnaloaded.setId('aminoacylated_MG492'),                     'set species s1 id')
    check(argtrnaloaded.setCompartment('c'),            'set species s1 compartment')
    check(argtrnaloaded.setConstant(False),              'set "constant" attribute on s1')
    check(argtrnaloaded.setInitialAmount(0),             'set initial amount for s1')
    check(argtrnaloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(argtrnaloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(argtrnaloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    argtrna2 = model.createSpecies()
    check(argtrna2,                                 'create species s1')
    check(argtrna2.setId('MG495'),                     'set species s1 id')
    check(argtrna2.setCompartment('c'),            'set species s1 compartment')
    check(argtrna2.setConstant(False),              'set "constant" attribute on s1')
    check(argtrna2.setInitialAmount(0),             'set initial amount for s1')
    check(argtrna2.setSubstanceUnits('item'),       'set substance units for s1')
    check(argtrna2.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(argtrna2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    argtrna2loaded = model.createSpecies()
    check(argtrna2loaded,                                 'create species s1')
    check(argtrna2loaded.setId('aminoacylated_MG495'),                     'set species s1 id')
    check(argtrna2loaded.setCompartment('c'),            'set species s1 compartment')
    check(argtrna2loaded.setConstant(False),              'set "constant" attribute on s1')
    check(argtrna2loaded.setInitialAmount(0),             'set initial amount for s1')
    check(argtrna2loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(argtrna2loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(argtrna2loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    asptrna = model.createSpecies()
    check(asptrna,                                 'create species s1')
    check(asptrna.setId('MG489'),                     'set species s1 id')
    check(asptrna.setCompartment('c'),            'set species s1 compartment')
    check(asptrna.setConstant(False),              'set "constant" attribute on s1')
    check(asptrna.setInitialAmount(0),             'set initial amount for s1')
    check(asptrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(asptrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(asptrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    asptrnaloaded = model.createSpecies()
    check(asptrnaloaded,                                 'create species s1')
    check(asptrnaloaded.setId('aminoacylated_MG489'),                     'set species s1 id')
    check(asptrnaloaded.setCompartment('c'),            'set species s1 compartment')
    check(asptrnaloaded.setConstant(False),              'set "constant" attribute on s1')
    check(asptrnaloaded.setInitialAmount(0),             'set initial amount for s1')
    check(asptrnaloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(asptrnaloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(asptrnaloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    cystrna = model.createSpecies()
    check(cystrna,                                 'create species s1')
    check(cystrna.setId('MG483'),                     'set species s1 id')
    check(cystrna.setCompartment('c'),            'set species s1 compartment')
    check(cystrna.setConstant(False),              'set "constant" attribute on s1')
    check(cystrna.setInitialAmount(0),             'set initial amount for s1')
    check(cystrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(cystrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(cystrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    cystrnaloaded = model.createSpecies()
    check(cystrnaloaded,                                 'create species s1')
    check(cystrnaloaded.setId('aminoacylated_MG483'),                     'set species s1 id')
    check(cystrnaloaded.setCompartment('c'),            'set species s1 compartment')
    check(cystrnaloaded.setConstant(False),              'set "constant" attribute on s1')
    check(cystrnaloaded.setInitialAmount(0),             'set initial amount for s1')
    check(cystrnaloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(cystrnaloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(cystrnaloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    glytrna = model.createSpecies()
    check(glytrna,                                 'create species s1')
    check(glytrna.setId('MG493'),                     'set species s1 id')
    check(glytrna.setCompartment('c'),            'set species s1 compartment')
    check(glytrna.setConstant(False),              'set "constant" attribute on s1')
    check(glytrna.setInitialAmount(0),             'set initial amount for s1')
    check(glytrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(glytrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(glytrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    glytrnaloaded = model.createSpecies()
    check(glytrnaloaded,                                 'create species s1')
    check(glytrnaloaded.setId('aminoacylated_MG493'),                     'set species s1 id')
    check(glytrnaloaded.setCompartment('c'),            'set species s1 compartment')
    check(glytrnaloaded.setConstant(False),              'set "constant" attribute on s1')
    check(glytrnaloaded.setInitialAmount(0),             'set initial amount for s1')
    check(glytrnaloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(glytrnaloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(glytrnaloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    iletrna = model.createSpecies()
    check(iletrna,                                 'create species s1')
    check(iletrna.setId('MG472'),                     'set species s1 id')
    check(iletrna.setCompartment('c'),            'set species s1 compartment')
    check(iletrna.setConstant(False),              'set "constant" attribute on s1')
    check(iletrna.setInitialAmount(0),             'set initial amount for s1')
    check(iletrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(iletrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(iletrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    iletrnaloaded = model.createSpecies()
    check(iletrnaloaded,                                 'create species s1')
    check(iletrnaloaded.setId('aminoacylated_MG472'),                     'set species s1 id')
    check(iletrnaloaded.setCompartment('c'),            'set species s1 compartment')
    check(iletrnaloaded.setConstant(False),              'set "constant" attribute on s1')
    check(iletrnaloaded.setInitialAmount(0),             'set initial amount for s1')
    check(iletrnaloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(iletrnaloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(iletrnaloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    iletrna2 = model.createSpecies()
    check(iletrna2,                                 'create species s1')
    check(iletrna2.setId('MG486'),                     'set species s1 id')
    check(iletrna2.setCompartment('c'),            'set species s1 compartment')
    check(iletrna2.setConstant(False),              'set "constant" attribute on s1')
    check(iletrna2.setInitialAmount(0),             'set initial amount for s1')
    check(iletrna2.setSubstanceUnits('item'),       'set substance units for s1')
    check(iletrna2.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(iletrna2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    iletrna2loaded = model.createSpecies()
    check(iletrna2loaded,                                 'create species s1')
    check(iletrna2loaded.setId('aminoacylated_MG486'),                     'set species s1 id')
    check(iletrna2loaded.setCompartment('c'),            'set species s1 compartment')
    check(iletrna2loaded.setConstant(False),              'set "constant" attribute on s1')
    check(iletrna2loaded.setInitialAmount(0),             'set initial amount for s1')
    check(iletrna2loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(iletrna2loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(iletrna2loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    mettrna = model.createSpecies()
    check(mettrna,                                 'create species s1')
    check(mettrna.setId('MG485'),                     'set species s1 id')
    check(mettrna.setCompartment('c'),            'set species s1 compartment')
    check(mettrna.setConstant(False),              'set "constant" attribute on s1')
    check(mettrna.setInitialAmount(0),             'set initial amount for s1')
    check(mettrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(mettrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(mettrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    mettrnaloaded = model.createSpecies()
    check(mettrnaloaded,                                 'create species s1')
    check(mettrnaloaded.setId('aminoacylated_MG485'),                     'set species s1 id')
    check(mettrnaloaded.setCompartment('c'),            'set species s1 compartment')
    check(mettrnaloaded.setConstant(False),              'set "constant" attribute on s1')
    check(mettrnaloaded.setInitialAmount(0),             'set initial amount for s1')
    check(mettrnaloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(mettrnaloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(mettrnaloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    fmettrna = model.createSpecies()
    check(fmettrna,                                 'create species s1')
    check(fmettrna.setId('MG488'),                     'set species s1 id')
    check(fmettrna.setCompartment('c'),            'set species s1 compartment')
    check(fmettrna.setConstant(False),              'set "constant" attribute on s1')
    check(fmettrna.setInitialAmount(0),             'set initial amount for s1')
    check(fmettrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(fmettrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(fmettrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    fmettrnametloaded = model.createSpecies()
    check(fmettrnametloaded,                                 'create species s1')
    check(fmettrnametloaded.setId('met_aminoacylated_MG488'),                     'set species s1 id')
    check(fmettrnametloaded.setCompartment('c'),            'set species s1 compartment')
    check(fmettrnametloaded.setConstant(False),              'set "constant" attribute on s1')
    check(fmettrnametloaded.setInitialAmount(0),             'set initial amount for s1')
    check(fmettrnametloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(fmettrnametloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(fmettrnametloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    fmettrnaloaded = model.createSpecies()
    check(fmettrnaloaded,                                 'create species s1')
    check(fmettrnaloaded.setId('aminoacylated_MG488'),                     'set species s1 id')
    check(fmettrnaloaded.setCompartment('c'),            'set species s1 compartment')
    check(fmettrnaloaded.setConstant(False),              'set "constant" attribute on s1')
    check(fmettrnaloaded.setInitialAmount(0),             'set initial amount for s1')
    check(fmettrnaloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(fmettrnaloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(fmettrnaloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    phetrna = model.createSpecies()
    check(phetrna,                                 'create species s1')
    check(phetrna.setId('MG490'),                     'set species s1 id')
    check(phetrna.setCompartment('c'),            'set species s1 compartment')
    check(phetrna.setConstant(False),              'set "constant" attribute on s1')
    check(phetrna.setInitialAmount(0),             'set initial amount for s1')
    check(phetrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(phetrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(phetrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    phetrnaloaded = model.createSpecies()
    check(phetrnaloaded,                                 'create species s1')
    check(phetrnaloaded.setId('aminoacylated_MG490'),                     'set species s1 id')
    check(phetrnaloaded.setCompartment('c'),            'set species s1 compartment')
    check(phetrnaloaded.setConstant(False),              'set "constant" attribute on s1')
    check(phetrnaloaded.setInitialAmount(0),             'set initial amount for s1')
    check(phetrnaloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(phetrnaloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(phetrnaloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    protrna = model.createSpecies()
    check(protrna,                                 'create species s1')
    check(protrna.setId('MG484'),                     'set species s1 id')
    check(protrna.setCompartment('c'),            'set species s1 compartment')
    check(protrna.setConstant(False),              'set "constant" attribute on s1')
    check(protrna.setInitialAmount(0),             'set initial amount for s1')
    check(protrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(protrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(protrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    protrnaloaded = model.createSpecies()
    check(protrnaloaded,                                 'create species s1')
    check(protrnaloaded.setId('aminoacylated_MG484'),                     'set species s1 id')
    check(protrnaloaded.setCompartment('c'),            'set species s1 compartment')
    check(protrnaloaded.setConstant(False),              'set "constant" attribute on s1')
    check(protrnaloaded.setInitialAmount(0),             'set initial amount for s1')
    check(protrnaloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(protrnaloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(protrnaloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    sertrna = model.createSpecies()
    check(sertrna,                                 'create species s1')
    check(sertrna.setId('MG475'),                     'set species s1 id')
    check(sertrna.setCompartment('c'),            'set species s1 compartment')
    check(sertrna.setConstant(False),              'set "constant" attribute on s1')
    check(sertrna.setInitialAmount(0),             'set initial amount for s1')
    check(sertrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(sertrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(sertrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    sertrnaloaded = model.createSpecies()
    check(sertrnaloaded,                                 'create species s1')
    check(sertrnaloaded.setId('aminoacylated_MG475'),                     'set species s1 id')
    check(sertrnaloaded.setCompartment('c'),            'set species s1 compartment')
    check(sertrnaloaded.setConstant(False),              'set "constant" attribute on s1')
    check(sertrnaloaded.setInitialAmount(0),             'set initial amount for s1')
    check(sertrnaloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(sertrnaloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(sertrnaloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    sertrna2 = model.createSpecies()
    check(sertrna2,                                 'create species s1')
    check(sertrna2.setId('MG479'),                     'set species s1 id')
    check(sertrna2.setCompartment('c'),            'set species s1 compartment')
    check(sertrna2.setConstant(False),              'set "constant" attribute on s1')
    check(sertrna2.setInitialAmount(0),             'set initial amount for s1')
    check(sertrna2.setSubstanceUnits('item'),       'set substance units for s1')
    check(sertrna2.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(sertrna2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    sertrna2loaded = model.createSpecies()
    check(sertrna2loaded,                                 'create species s1')
    check(sertrna2loaded.setId('aminoacylated_MG479'),                     'set species s1 id')
    check(sertrna2loaded.setCompartment('c'),            'set species s1 compartment')
    check(sertrna2loaded.setConstant(False),              'set "constant" attribute on s1')
    check(sertrna2loaded.setInitialAmount(0),             'set initial amount for s1')
    check(sertrna2loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(sertrna2loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(sertrna2loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    sertrna3 = model.createSpecies()
    check(sertrna3,                                 'create species s1')
    check(sertrna3.setId('MG487'),                     'set species s1 id')
    check(sertrna3.setCompartment('c'),            'set species s1 compartment')
    check(sertrna3.setConstant(False),              'set "constant" attribute on s1')
    check(sertrna3.setInitialAmount(0),             'set initial amount for s1')
    check(sertrna3.setSubstanceUnits('item'),       'set substance units for s1')
    check(sertrna3.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(sertrna3.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    sertrna3loaded = model.createSpecies()
    check(sertrna3loaded,                                 'create species s1')
    check(sertrna3loaded.setId('aminoacylated_MG487'),                     'set species s1 id')
    check(sertrna3loaded.setCompartment('c'),            'set species s1 compartment')
    check(sertrna3loaded.setConstant(False),              'set "constant" attribute on s1')
    check(sertrna3loaded.setInitialAmount(0),             'set initial amount for s1')
    check(sertrna3loaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(sertrna3loaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(sertrna3loaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    trptrna = model.createSpecies()
    check(trptrna,                                 'create species s1')
    check(trptrna.setId('MG496'),                     'set species s1 id')
    check(trptrna.setCompartment('c'),            'set species s1 compartment')
    check(trptrna.setConstant(False),              'set "constant" attribute on s1')
    check(trptrna.setInitialAmount(0),             'set initial amount for s1')
    check(trptrna.setSubstanceUnits('item'),       'set substance units for s1')
    check(trptrna.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(trptrna.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    trptrnaloaded = model.createSpecies()
    check(trptrnaloaded,                                 'create species s1')
    check(trptrnaloaded.setId('aminoacylated_MG496'),                     'set species s1 id')
    check(trptrnaloaded.setCompartment('c'),            'set species s1 compartment')
    check(trptrnaloaded.setConstant(False),              'set "constant" attribute on s1')
    check(trptrnaloaded.setInitialAmount(0),             'set initial amount for s1')
    check(trptrnaloaded.setSubstanceUnits('item'),       'set substance units for s1')
    check(trptrnaloaded.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(trptrnaloaded.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    # Enzymes
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
    alatrnaligase = model.createSpecies()
    check(alatrnaligase,                                 'create species s1')
    check(alatrnaligase.setId('MG_292_TETRAMER'),                     'set species s1 id')
    check(alatrnaligase.setCompartment('c'),            'set species s1 compartment')
    check(alatrnaligase.setConstant(False),              'set "constant" attribute on s1')
    check(alatrnaligase.setInitialAmount(0),             'set initial amount for s1')
    check(alatrnaligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(alatrnaligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(alatrnaligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    argtrnaligase = model.createSpecies()
    check(argtrnaligase,                                 'create species s1')
    check(argtrnaligase.setId('MG_378_MONOMER'),                     'set species s1 id')
    check(argtrnaligase.setCompartment('c'),            'set species s1 compartment')
    check(argtrnaligase.setConstant(False),              'set "constant" attribute on s1')
    check(argtrnaligase.setInitialAmount(0),             'set initial amount for s1')
    check(argtrnaligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(argtrnaligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(argtrnaligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    asptrnaligase = model.createSpecies()
    check(asptrnaligase,                                 'create species s1')
    check(asptrnaligase.setId('MG_036_DIMER'),                     'set species s1 id')
    check(asptrnaligase.setCompartment('c'),            'set species s1 compartment')
    check(asptrnaligase.setConstant(False),              'set "constant" attribute on s1')
    check(asptrnaligase.setInitialAmount(0),             'set initial amount for s1')
    check(asptrnaligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(asptrnaligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(asptrnaligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    cystrnaligase = model.createSpecies()
    check(cystrnaligase,                                 'create species s1')
    check(cystrnaligase.setId('MG_253_MONOMER'),                     'set species s1 id')
    check(cystrnaligase.setCompartment('c'),            'set species s1 compartment')
    check(cystrnaligase.setConstant(False),              'set "constant" attribute on s1')
    check(cystrnaligase.setInitialAmount(0),             'set initial amount for s1')
    check(cystrnaligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(cystrnaligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(cystrnaligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    glytrnaligase = model.createSpecies()
    check(glytrnaligase,                                 'create species s1')
    check(glytrnaligase.setId('MG_251_DIMER'),                     'set species s1 id')
    check(glytrnaligase.setCompartment('c'),            'set species s1 compartment')
    check(glytrnaligase.setConstant(False),              'set "constant" attribute on s1')
    check(glytrnaligase.setInitialAmount(0),             'set initial amount for s1')
    check(glytrnaligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(glytrnaligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(glytrnaligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    iletrnaligase = model.createSpecies()
    check(iletrnaligase,                                 'create species s1')
    check(iletrnaligase.setId('MG_345_MONOMER'),                     'set species s1 id')
    check(iletrnaligase.setCompartment('c'),            'set species s1 compartment')
    check(iletrnaligase.setConstant(False),              'set "constant" attribute on s1')
    check(iletrnaligase.setInitialAmount(0),             'set initial amount for s1')
    check(iletrnaligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(iletrnaligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(iletrnaligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    mettrnaligase = model.createSpecies()
    check(mettrnaligase,                                 'create species s1')
    check(mettrnaligase.setId('MG_021_DIMER'),                     'set species s1 id')
    check(mettrnaligase.setCompartment('c'),            'set species s1 compartment')
    check(mettrnaligase.setConstant(False),              'set "constant" attribute on s1')
    check(mettrnaligase.setInitialAmount(0),             'set initial amount for s1')
    check(mettrnaligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(mettrnaligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(mettrnaligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    mettrnaformyltrans = model.createSpecies()
    check(mettrnaformyltrans,                                 'create species s1')
    check(mettrnaformyltrans.setId('MG_365_MONOMER'),                     'set species s1 id')
    check(mettrnaformyltrans.setCompartment('c'),            'set species s1 compartment')
    check(mettrnaformyltrans.setConstant(False),              'set "constant" attribute on s1')
    check(mettrnaformyltrans.setInitialAmount(0),             'set initial amount for s1')
    check(mettrnaformyltrans.setSubstanceUnits('item'),       'set substance units for s1')
    check(mettrnaformyltrans.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(mettrnaformyltrans.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    phetrnaligase = model.createSpecies()
    check(phetrnaligase,                                 'create species s1')
    check(phetrnaligase.setId('MG_194_195_TETRAMER'),                     'set species s1 id')
    check(phetrnaligase.setCompartment('c'),            'set species s1 compartment')
    check(phetrnaligase.setConstant(False),              'set "constant" attribute on s1')
    check(phetrnaligase.setInitialAmount(0),             'set initial amount for s1')
    check(phetrnaligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(phetrnaligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(phetrnaligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    protrnaligase = model.createSpecies()
    check(protrnaligase,                                 'create species s1')
    check(protrnaligase.setId('MG_283_DIMER'),                     'set species s1 id')
    check(protrnaligase.setCompartment('c'),            'set species s1 compartment')
    check(protrnaligase.setConstant(False),              'set "constant" attribute on s1')
    check(protrnaligase.setInitialAmount(0),             'set initial amount for s1')
    check(protrnaligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(protrnaligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(protrnaligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    sertrnaligase = model.createSpecies()
    check(sertrnaligase,                                 'create species s1')
    check(sertrnaligase.setId('MG_005_DIMER'),                     'set species s1 id')
    check(sertrnaligase.setCompartment('c'),            'set species s1 compartment')
    check(sertrnaligase.setConstant(False),              'set "constant" attribute on s1')
    check(sertrnaligase.setInitialAmount(0),             'set initial amount for s1')
    check(sertrnaligase.setSubstanceUnits('item'),       'set substance units for s1')
    check(sertrnaligase.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(sertrnaligase.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

    sertrnaligase2 = model.createSpecies()
    check(sertrnaligase2,                                 'create species s1')
    check(sertrnaligase2.setId('MG_375_DIMER'),                     'set species s1 id')
    check(sertrnaligase2.setCompartment('c'),            'set species s1 compartment')
    check(sertrnaligase2.setConstant(False),              'set "constant" attribute on s1')
    check(sertrnaligase2.setInitialAmount(0),             'set initial amount for s1')
    check(sertrnaligase2.setSubstanceUnits('item'),       'set substance units for s1')
    check(sertrnaligase2.setBoundaryCondition(False),     'set "boundaryCondition" on s1')
    check(sertrnaligase2.setHasOnlySubstanceUnits(False), 'set "hasOnlySubstanceUnits" on s1')

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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    mg502aminoacylenzyme = mg502aminoacyl.createModifier()
    check(mg502aminoacylenzyme,                       'create reactant')
    check(mg502aminoacylenzyme.setSpecies('MG_295_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    mg502amidotransenzyme = mg502amidotrans.createModifier()
    check(mg502amidotransenzyme,                       'create reactant')
    check(mg502amidotransenzyme.setSpecies('MG_462_MONOMER'),      'assign reactant species')

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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
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

    math_ast = sbml.parseL3Formula('k * s1 * c1')
    check(math_ast,                           'create AST for rate expression')

    kinetic_law = mg523aminoacyl.createKineticLaw()
    check(kinetic_law,                        'create kinetic law')
    check(kinetic_law.setMath(math_ast),      'set math on kinetic law')

    # write the aminoacylation model to an xml file
    sbml.writeSBMLToFile(document, os.path.join('C:\\wc\\2014_VW_modelling_workshop\\wholecell-translation', 'aminoacylation.xml'))

    # return a text string containing the model in XML format.
    return sbml.writeSBMLToString(document)

# if you are a UNIX hacker then you can produce the xml files from bash/terminal:
#       python createAminoAcylation.py > aminoacylation.xml
if __name__ == '__main__':
    print(create_model())