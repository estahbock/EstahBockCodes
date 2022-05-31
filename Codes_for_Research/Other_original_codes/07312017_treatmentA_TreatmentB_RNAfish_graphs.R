setwd("~") # setting working directory so can open data files that we are using
all_transcripts<-read.table("TreatmentA_TreatmentB_all_12hr.txt", na.strings = "NA", sep="\t", header=T, check.names = F)
# opened data file for all transcripts and converted table into dataframe in R
head(all_transcripts) # show first 5 rows of dataframe
par(font.axis=2)
boxplot(all_transcripts, na.rm = T, lwd = 2, outline = FALSE, cex.axis=1.3, ylim=c(0,200))
title(main = "Total RNA transcripts by treatment", cex.main=2)
title(ylab = "Total # transcripts/cell", line=2.5, xlab = "Treatment", cex.lab=1.8, font.lab = 2)
box(lwd=2)
abline(h=seq(0,200,by=50),col="black",lty="dotted", lwd=2)
abline(h=seq(0,200,by=10),col="black",lty="dotted", lwd=1)
stripchart(all_transcripts, vertical = TRUE, method = "jitter", add = TRUE, pch = 20, col = 'darkviolet')

# Made boxplot combined with scatterplot of all transcripts

# making histograms at all time points of all transcripts:
par(font.lab=2)
opar <- par(lwd=3)

h = hist(all_transcripts[,1], breaks=seq(0,150,10))
h$density = h$counts/sum(h$counts)*100
plot(h,, main = "TreatmentA", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, freq=FALSE, ylim=c(0,50))
title(ylab="Percent of total cells", line=2.5, cex.lab=2)

h = hist(all_transcripts[,2], breaks=seq(0,150,10))
h$density = h$counts/sum(h$counts)*100
plot(h,, main = "TreatmentB", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, freq=FALSE, ylim=c(0,50))
title(ylab="Percent of total cells", line=2.5, cex.lab=2)

h = hist(all_transcripts[,3], breaks=seq(0,150,10))
h$density = h$counts/sum(h$counts)*100
plot(h,, main = "TreatmentA + TreatmentB", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, freq=FALSE, ylim=c(0,50))
title(ylab="Percent of total cells", line=2.5, cex.lab=2)

hist(all_transcripts[,1], main = "12 hr TreatmentA", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,150,15))
title(ylab="Frequency", line=2.5, cex.lab=2)
hist(all_transcripts[,2], main = "12 hr TreatmentB", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,100,10))
title(ylab="Frequency", line=2.5, cex.lab=2)
hist(all_transcripts[,3], main = "12 hr TreatmentA + TreatmentB", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,150,15))
title(ylab="Frequency", line=2.5, cex.lab=2)

par(font.lab=2)
opar <- par(lwd=3)
hist(all_transcripts[,1], main = "TreatmentA", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,150,15))
title(ylab="Frequency", line=2.5, cex.lab=2)
hist(all_transcripts[,2], main = "TreatmentB", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,100,10))
title(ylab="Frequency", line=2.5, cex.lab=2)
hist(all_transcripts[,3], main = "TreatmentA + TreatmentB", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,150,15))
title(ylab="Frequency", line=2.5, cex.lab=2)

# Calculating fano factors for each time point:
# making function to calculate fano factors:
make_fano<-function(x){
  fano_factors_temp<-(sd(x, na.rm = T)^2)/(mean(x, na.rm = T))
  return(fano_factors_temp)
}
# applying fano factor calculation function to each time point:
fano_factors<-apply(all_transcripts, 2, make_fano)
fano_factors # tells us the fano factors calculated


# barplot((fano_factors), xlab = "Treatment", ylab = "Fano Factor", main = "Fano Factor for Treatment")

# Bootstrapping to get 95% CI for fano factors:
# converting each column to a list of values to make it easier to bootstrap and removing NA values:

TreatmentA12 <- all_transcripts[,1]
TreatmentA12 <- TreatmentA12[!is.na(TreatmentA12)]
TreatmentB12 <- all_transcripts[,2]
TreatmentB12 <- TreatmentB12[!is.na(TreatmentB12)]
rb12 <- all_transcripts[,3]
rb12 <- rb12[!is.na(rb12)]

# Bootstrapping for all treatments/time points, using 10,000 simulations, each:
boot10000_TreatmentA12<-replicate(10000,sample(TreatmentA12, length(TreatmentA12), replace = TRUE))
boot10000_TreatmentB12<-replicate(10000,sample(TreatmentB12, length(TreatmentB12), replace = TRUE))
boot10000_rb12<-replicate(10000,sample(rb12, length(rb12), replace = TRUE))

# Calculating 95% confidence intervals from the bootstrapping:

fanoboot10000_TreatmentA12<-c()
for(i in 1:10000){
  fanoboot10000_TreatmentA12[i]<-(((sd(boot10000_TreatmentA12[,i]))^2)/(mean(boot10000_TreatmentA12[,i])))
}
Fano_95CI_TreatmentA12<-quantile(fanoboot10000_TreatmentA12, probs=c(.025,.975))
Fano_95CI_TreatmentA12

fanoboot10000_TreatmentB12<-c()
for(i in 1:10000){
  fanoboot10000_TreatmentB12[i]<-(((sd(boot10000_TreatmentB12[,i]))^2)/(mean(boot10000_TreatmentB12[,i])))
}
Fano_95CI_TreatmentB12<-quantile(fanoboot10000_TreatmentB12, probs=c(.025,.975))
Fano_95CI_TreatmentB12

fanoboot10000_rb12<-c()
for(i in 1:10000){
  fanoboot10000_rb12[i]<-(((sd(boot10000_rb12[,i]))^2)/(mean(boot10000_rb12[,i])))
}
Fano_95CI_rb12<-quantile(fanoboot10000_rb12, probs=c(.025,.975))
Fano_95CI_rb12

# Calculating variances for each time point:
# making function to calculate variances:
make_var<-function(x){
  var_temp<-(sd(x, na.rm = T)^2)
  return(var_temp)
}
# applying variance calculation function to each time point:
vars_x<-apply(all_transcripts, 2, make_var)
vars_x # tells us the variances calculated

# Calculating 95% confidence intervals from the bootstrapping:

varboot10000_TreatmentA12<-c()
for(i in 1:10000){
  varboot10000_TreatmentA12[i]<-((sd(boot10000_TreatmentA12[,i]))^2)
}
var_95CI_TreatmentA12<-quantile(varboot10000_TreatmentA12, probs=c(.025,.975))
var_95CI_TreatmentA12

varboot10000_TreatmentB12<-c()
for(i in 1:10000){
  varboot10000_TreatmentB12[i]<-((sd(boot10000_TreatmentB12[,i]))^2)
}
var_95CI_TreatmentB12<-quantile(varboot10000_TreatmentB12, probs=c(.025,.975))
var_95CI_TreatmentB12

varboot10000_rb12<-c()
for(i in 1:10000){
  varboot10000_rb12[i]<-((sd(boot10000_rb12[,i]))^2)
}
var_95CI_rb12<-quantile(varboot10000_rb12, probs=c(.025,.975))
var_95CI_rb12

# Nascent Transcript Analysis
nas_drugs<-read.table("Nasc_TreatmentA_TreatmentB_10182017.txt", na.strings = "NA", sep="\t", header=T, check.names = F)
# opened data file for nascent transcripts and converted table into dataframe in R
head(nas_drugs) # show first 5 rows of dataframe
max(nas_drugs,na.rm=T)
par(font.axis=2)
boxplot(nas_drugs, na.rm = T, lwd = 2, outline = FALSE, ylim=c(0,40), cex.axis=1.3)
title(main = "Nascent RNA transcripts by treatment", cex.main=2)
title(ylab = "# Nascent transcripts/TS", line=2.5, xlab = "Treatment", cex.lab=1.8, font.lab = 2)
box(lwd=2)
abline(h=seq(0,40,by=5),col="black",lty="dotted", lwd=1.5)
stripchart(nas_drugs, vertical = TRUE, method = "jitter", add = TRUE, pch = 20, col = 'darkviolet')

nTreatmentA <- nas_drugs[,1]
nTreatmentA <- nTreatmentA[!is.na(nTreatmentA)]
nTreatmentB <- nas_drugs[,2]
nTreatmentB <- nTreatmentB[!is.na(nTreatmentB)]
nbr <- nas_drugs[,3]
nbr <- nbr[!is.na(nbr)]

# Statistical Testing:

# All transcripts:

drug_counts<-c(TreatmentA12,TreatmentB12,rb12)
drug<-c(rep("TreatmentA",78),rep("TreatmentB",52),rep("TreatmentA+TreatmentB",60))
drug_dat<-data.frame(drug_counts,drug)
head(drug_dat)

# Nascent transcripts:

ndrug_counts<-c(nTreatmentA,nTreatmentB,nbr)
ndrug<-c(rep("TreatmentA",29),rep("TreatmentB",38),rep("TreatmentA+TreatmentB",30))
ndrug_dat<-data.frame(ndrug_counts,ndrug)
head(ndrug_dat)

# Assess nascent variance:

# applying variance calculation function to each time point:
vars_x<-apply(nas_drugs, 2, make_var)
vars_x # tells us the variances calculated

# Kruskal Wallis Test because unequal variance for all transcripts and nascent transcripts:


kruskal.test(drug_counts ~ drug, data=drug_dat)
kruskal.test(ndrug_counts ~ ndrug, data=ndrug_dat)

## Dunn test
# install.packages("FSA")
library(FSA)
# Cite FSA if used in publication!!!! 
##      FSA package, version 0.8.5        ##
##    Derek H. Ogle, Northland College    ##
dunn_drug_dat = dunnTest(drug_counts ~ drug,
              data=drug_dat,
              method="bh")    
dunn_drug_dat

## Dunn test
library(FSA)
dunn_ndrug_dat = dunnTest(ndrug_counts ~ ndrug,
                         data=ndrug_dat,
                         method="bh")    
dunn_ndrug_dat


