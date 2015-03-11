
##############################################
#load and save all peptides df (TODO)

#setwd("nameFolder")
library("xlsx")
proteinsDFfull <- read.xlsx2("./knowledgebase.xlsx",sheetIndex=16)
names(proteinsDFfull)
proteinsDFtosave <- cbind(proteinsDFfull["WholeCellModelID"],proteinsDFfull["Length"],
                          proteinsDFfull["Sequence"])

proteinDFtosaveRefined <- proteinsDFtosave[which(proteinsDFtosave$WholeCellModelID!=
                                             "MG_449_MONOMER"),]    

#write.csv(proteinDFtosaveRefined,"ProtSeq.csv",row.names = FALSE)


