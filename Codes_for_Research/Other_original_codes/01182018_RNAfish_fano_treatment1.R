setwd("~") # setting working directory so can open data files that we are using
all_transcripts<-read.table("07262017_random_CellType1_summary.txt", na.strings = "NA", sep="\t", header=T, check.names = F)
# opened data file for all transcripts and converted table into dataframe in R
head(all_transcripts) # show first 5 rows of dataframe
# Make boxplot combined with scatterplot of all transcripts:
par(font.axis=2)
boxplot(all_transcripts, na.rm = T, lwd = 2, outline = FALSE, ylim=c(0,650), cex.axis=1.3)
title(main = "Total RNA transcripts during time course", cex.main=2)
title(ylab = "Total # transcripts/cell", line=2.5, xlab = "Treatment", cex.lab=1.8, font.lab = 2)
box(lwd=2)
abline(h=seq(0,650,by=50),col="black",lty="dotted", lwd=1.5)
stripchart(all_transcripts, vertical = TRUE, method = "jitter", add = TRUE, pch = 20, col = 'darkviolet')

Control<-read.table("Control.txt", na.strings = "NA", sep="\t", header=T, check.names = F)
# opened data file for all transcripts and converted table into dataframe in R
head(Control) # show first 5 rows of dataframe
# Make boxplot combined with scatterplot of all transcripts:
par(font.axis=2)
boxplot(Control, na.rm = T, lwd = 2, outline = FALSE, ylim=c(0,400), cex.axis=1.3)
title(main = "Total RNA transcripts", cex.main=2)
title(ylab = "Total # transcripts/cell", line=2.5, xlab = "9 hr Control", cex.lab=1.8, font.lab = 2)
box(lwd=2)
abline(h=seq(0,400,by=50),col="black",lty="dotted", lwd=1.5)
stripchart(Control, vertical = TRUE, method = "jitter", add = TRUE, pch = 20, col = 'darkviolet')

# making histograms at all time points of all transcripts:
par(font.lab=2)
opar <- par(lwd=3)
par(opar)
h = hist(all_transcripts[,2], breaks=seq(0,700,25))
h$density = h$counts/sum(h$counts)*100
plot(h, main = "30 min. Treatment1", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, freq=FALSE, ylim=c(0,50))
title(ylab="Percent of total cells", line=2.5, cex.lab=2)

h = hist(all_transcripts[,1], breaks=seq(0,700,25))
h$density = h$counts/sum(h$counts)*100
plot(h, main = "9 hr. Control", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, freq=FALSE, ylim=c(0,50))
title(ylab="Percent of total cells", line=2.5, cex.lab=2)

h = hist(all_transcripts[,3], breaks=seq(0,700,25))
h$density = h$counts/sum(h$counts)*100
plot(h, main = "1 hr. Treatment1", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, freq=FALSE, ylim=c(0,50))
title(ylab="Percent of total cells", line=2.5, cex.lab=2)

h = hist(all_transcripts[,4], breaks=seq(0,700,25))
h$density = h$counts/sum(h$counts)*100
plot(h, main = "2 hr. Treatment1", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, freq=FALSE, ylim=c(0,50))
title(ylab="Percent of total cells", line=2.5, cex.lab=2)

h = hist(all_transcripts[,5], breaks=seq(0,700,25))
h$density = h$counts/sum(h$counts)*100
plot(h, main = "3 hr. Treatment1", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, freq=FALSE, ylim=c(0,50))
title(ylab="Percent of total cells", line=2.5, cex.lab=2)

h = hist(all_transcripts[,6], breaks=seq(0,700,25))
h$density = h$counts/sum(h$counts)*100
plot(h, main = "4 hr Treatment1", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, freq=FALSE, ylim=c(0,50))
title(ylab="Percent of total cells", line=2.5, cex.lab=2)

h = hist(all_transcripts[,7], breaks=seq(0,700,25))
h$density = h$counts/sum(h$counts)*100
plot(h, main = "9 hr Treatment1", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, freq=FALSE, ylim=c(0,50))
title(ylab="Percent of total cells", line=2.5, cex.lab=2)

hist(all_transcripts[,2], main = "30 min. Treatment1", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,700,25), ylim=c(0,40))
title(ylab="Frequency", line=2.5, cex.lab=2)
par(opar)
hist(all_transcripts[,3], main = "1 hour Treatment1", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,700,25), ylim=c(0,40))
title(ylab="Frequency", line=2.5, cex.lab=2)
hist(all_transcripts[,4], main = "2 hour Treatment1", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,700,25), ylim=c(0,40))
title(ylab="Frequency", line=2.5, cex.lab=2)
hist(all_transcripts[,5], main = "3 hour Treatment1", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,700,25), ylim=c(0,40))
title(ylab="Frequency", line=2.5, cex.lab=2)
hist(all_transcripts[,6], main = "4 hour Treatment1", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,700,25), ylim=c(0,40))
title(ylab="Frequency", line=2.5, cex.lab=2)
hist(all_transcripts[,7], main = "9 hour Treatment1", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,700,25), ylim=c(0,40))
title(ylab="Frequency", line=2.5, cex.lab=2)
hist(all_transcripts[,1], main = "9 hour Control", xlab = "Total Transcripts in Cell", ylab="", lwd=3, col="lightgreen", cex.lab=2, cex.axis=1.2,cex.main=3, breaks=seq(0,700,25), ylim=c(0,40))
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
min30 <- all_transcripts[,2]
min30 <- min30[!is.na(min30)]
hr1 <- all_transcripts[,3]
hr1 <- hr1[!is.na(hr1)]
hr2 <- all_transcripts[,4]
hr2 <- hr2[!is.na(hr2)]
hr3 <- all_transcripts[,5]
hr3 <- hr3[!is.na(hr3)]
hr4 <- all_transcripts[,6]
hr4 <- hr4[!is.na(hr4)]
hr9 <- all_transcripts[,7]
hr9 <- hr9[!is.na(hr9)]
hr9unstim <- all_transcripts[,1]
hr9unstim <- hr9unstim[!is.na(hr9unstim)]

# Bootstrapping for all treatments/time points, using 10,000 simulations, each:
boot10000_min30<-replicate(10000,sample(min30, length(min30), replace = TRUE))
boot10000_hr1<-replicate(10000,sample(hr1, length(hr1), replace = TRUE))
boot10000_hr2<-replicate(10000,sample(hr2, length(hr2), replace = TRUE))
boot10000_hr3<-replicate(10000,sample(hr3, length(hr3), replace = TRUE))
boot10000_hr4<-replicate(10000,sample(hr4, length(hr4), replace = TRUE))
boot10000_hr9<-replicate(10000,sample(hr9, length(hr9), replace = TRUE))
boot10000_hr9unstim<-replicate(10000,sample(hr9unstim, length(hr9unstim), replace = TRUE))

# Calculating 95% confidence intervals from the bootstrapping:
fanoboot10000_min30<-c()
for(i in 1:10000){
  fanoboot10000_min30[i]<-(((sd(boot10000_min30[,i]))^2)/(mean(boot10000_min30[,i])))
}
Fano_95CI_30min<-quantile(fanoboot10000_min30, probs=c(.025,.975))
Fano_95CI_30min

fanoboot10000_hr1<-c()
for(i in 1:10000){
  fanoboot10000_hr1[i]<-(((sd(boot10000_hr1[,i]))^2)/(mean(boot10000_hr1[,i])))
}
Fano_95CI_hr1<-quantile(fanoboot10000_hr1, probs=c(.025,.975))
Fano_95CI_hr1

fanoboot10000_hr2<-c()
for(i in 1:10000){
  fanoboot10000_hr2[i]<-(((sd(boot10000_hr2[,i]))^2)/(mean(boot10000_hr2[,i])))
}
Fano_95CI_hr2<-quantile(fanoboot10000_hr2, probs=c(.025,.975))
Fano_95CI_hr2

fanoboot10000_hr3<-c()
for(i in 1:10000){
  fanoboot10000_hr3[i]<-(((sd(boot10000_hr3[,i]))^2)/(mean(boot10000_hr3[,i])))
}
Fano_95CI_hr3<-quantile(fanoboot10000_hr3, probs=c(.025,.975))
Fano_95CI_hr3

fanoboot10000_hr4<-c()
for(i in 1:10000){
  fanoboot10000_hr4[i]<-(((sd(boot10000_hr4[,i]))^2)/(mean(boot10000_hr4[,i])))
}
Fano_95CI_hr4<-quantile(fanoboot10000_hr4, probs=c(.025,.975))
Fano_95CI_hr4

fanoboot10000_hr9unstim<-c()
for(i in 1:10000){
  fanoboot10000_hr9unstim[i]<-(((sd(boot10000_hr9unstim[,i]))^2)/(mean(boot10000_hr9unstim[,i])))
}
Fano_95CI_hr9unstim<-quantile(fanoboot10000_hr9unstim, probs=c(.025,.975))
Fano_95CI_hr9unstim

fanoboot10000_hr9<-c()
for(i in 1:10000){
  fanoboot10000_hr9[i]<-(((sd(boot10000_hr9[,i]))^2)/(mean(boot10000_hr9[,i])))
}
Fano_95CI_hr9<-quantile(fanoboot10000_hr9, probs=c(.025,.975))
Fano_95CI_hr9

### cdfgam(fano_factors[,1], para = c(((length(min20)-1)/2),2)) #shape= (n-1)/2, scale=2

# download nascent results and make boxplots and histograms (including 9 hour Treatment1!)

# also calculate p-values in Matlab and comment this code!

# Analyzing nascent transcripts:

nascent_transcripts<-read.table("07262017_nascent_random_CellType1_summary_fixed.txt", na.strings = "NA", sep="\t", header=T, check.names = F)
# opened nascent transcript summary file and put in an R dataframe
head(nascent_transcripts) # viewing first 5 rows of nascent dataset

#boxplot(nascent_transcripts, na.rm = T, lwd = 2, xlab = "Treatment", ylab = "", main = "Nascent transcripts during time course", outline = FALSE, ylim=c(0,150), cex.axis=1.4, cex.lab=1.5, cex.main=2)
#title(ylab="# nascent transcripts/TS", line=2.5, cex.lab=1.5)
#box(lwd=2)
#abline(h=seq(0,150,by=25),col="black",lty="dotted", lwd=1.5)
#stripchart(nascent_transcripts, vertical = TRUE, method = "jitter", add = TRUE, pch = 20, col = 'darkviolet')

par(mgp = c(0, 0.6, 0))
par(oma = c(1, 1, 0, 0))

par(font.axis=2)
boxplot(nascent_transcripts, na.rm = T, lwd = 4, outline = FALSE, ylim=c(0,300), names=c("9 hr\n Control","30 min\n Treatment1","1 hr\n Treatment1","2 hr\n Treatment1","3 hr\n Treatment1","4 hr\n Treatment1"), las=2, cex.axis=1.3)
title(main = "Nascent RNA transcripts \nduring time course", cex.main=2)
title(ylab = "# nascent transcripts/TS", line=2.75, cex.lab=1.8, font.lab=2)
title(xlab = "Treatment", cex.lab=1.8, font.lab = 2, line=3.5, cex.lab=1.8, font.lab=2)
box(lwd=2)
abline(h=seq(0,300,by=25),col="black",lty="dotted", lwd=1.5)
stripchart(nascent_transcripts, vertical = TRUE, method = "jitter", add = TRUE, pch = 21, lwd=3, bg = 'magenta', cex=1)

par(mgp = c(0, 0.9, 0))
par(oma = c(0, 0, 0, 0))

# made boxplot combined with scatterplot of nascent transcripts

# making histograms of nascent transcripts at each time point:
hist(nascent_transcripts[,2], main = "Nascent Transcripts 30 min. Treatment1", xlab = "Nascent Transcripts in Cell")
hist(nascent_transcripts[,3], main = "Nascent Transcripts 1 hour Treatment1", xlab = "Nascent Transcripts in Cell")
hist(nascent_transcripts[,4], main = "Nascent Transcripts 2 hours Treatment1", xlab = "Nascent Transcripts in Cell")
hist(nascent_transcripts[,5], main = "Nascent Transcripts 3 hours Treatment1", xlab = "Nascent Transcripts in Cell")
hist(nascent_transcripts[,6], main = "Nascent Transcripts 4 hours Treatment1", xlab = "Nascent Transcripts in Cell")
hist(nascent_transcripts[,1], main = "Nascent Transcripts 9 hours Control", xlab = "Nascent Transcripts in Cell")

# Variance calculations and bootstrapping:

# Can use bootstrapping simulations from before (above)

# making function to calculate variances:
make_var<-function(x){
  var_temp<-(sd(x, na.rm = T)^2)
  return(var_temp)
}
# applying variance calculation function to each time point:
var_factors<-apply(all_transcripts, 2, make_var)
var_factors # tells us the variances calculated

# calculating variances from bootstrapping and getting 95% CI

varboot10000_min30<-c()
for(i in 1:10000){
  varboot10000_min30[i]<-(sd(boot10000_min30[,i])^2)
}
var_95CI_min30<-quantile(varboot10000_min30, probs=c(.025,.975))
var_95CI_min30

varboot10000_hr1<-c()
for(i in 1:10000){
  varboot10000_hr1[i]<-(sd(boot10000_hr1[,i])^2)
}
var_95CI_hr1<-quantile(varboot10000_hr1, probs=c(.025,.975))
var_95CI_hr1

varboot10000_hr2<-c()
for(i in 1:10000){
  varboot10000_hr2[i]<-(sd(boot10000_hr2[,i])^2)
}
var_95CI_hr2<-quantile(varboot10000_hr2, probs=c(.025,.975))
var_95CI_hr2

varboot10000_hr3<-c()
for(i in 1:10000){
  varboot10000_hr3[i]<-(sd(boot10000_hr3[,i])^2)
}
var_95CI_hr3<-quantile(varboot10000_hr3, probs=c(.025,.975))
var_95CI_hr3

varboot10000_hr4<-c()
for(i in 1:10000){
  varboot10000_hr4[i]<-(sd(boot10000_hr4[,i])^2)
}
var_95CI_hr4<-quantile(varboot10000_hr4, probs=c(.025,.975))
var_95CI_hr4

varboot10000_hr9<-c()
for(i in 1:10000){
  varboot10000_hr9[i]<-(sd(boot10000_hr9[,i])^2)
}
var_95CI_hr9<-quantile(varboot10000_hr9, probs=c(.025,.975))
var_95CI_hr9

varboot10000_hr9unstim<-c()
for(i in 1:10000){
  varboot10000_hr9unstim[i]<-(sd(boot10000_hr9unstim[,i])^2)
}
var_95CI_hr9unstim<-quantile(varboot10000_hr9unstim, probs=c(.025,.975))
var_95CI_hr9unstim

# Fano Factor and Variance Graphs:

# Derived from: https://www.uvm.edu/~ngotelli/Rscripts/Asymmetric%20Confidence%20Intervals.R
# plotting points with asymmetric confidence intervals
# using only graphical annotations
# 12 March 2013
# NJG

# fully blank plot
plot(1:5,1:5,xlim=c(0.5,6),ylim=c(0,200),type="n",
     axes= FALSE,ann=FALSE)

# add axes with labels
par(font.axis=2)
par(lwd=2)
axis(1,at=seq(1:6),labels=c("9 hr. Control", "30 min. Treatment1", "1 hr. Treatment1", "2 hr. Treatment1", "3 hr. Treatment1", "4 hr. Treatment1"), cex.axis=1.5)
axis(2, cex.axis=1.5)
mtext("Fano Factor",side=2,line=2.5, cex=2, font=2)
mtext("Treatment",side=1,line=2.5, cex=2, font=2)
mtext("Fano Factor by Treatment \nin CellType1 Cells",side=3,line=0, cex=2.3, font=2)
box(bty="L", lwd=2)
fano<-c(112.05478,61.9984,32.1164,34.09882,40.37208,68.72841)
fano_L<-c(59.91336,35.5845,22.94598,22.94114,28.50255,50.1292)
fano_U<-c(151.50821,93.55298,41.70535,44.91767,52.16581,87.81883)

arrows(1:6,fano,1:6,fano_L,angle=90,length=0.1)
arrows(1:6,fano,1:6,fano_U,angle=90,length=0.1)
points(1:6,fano,pch=19,cex=1.5,col="blue",bg="blue")
abline(h=seq(0,200,by=10),col="black",lty="dotted", lwd=1)
abline(h=seq(0,200,by=50),col="black",lty="dotted", lwd=2)

# fully blank plot
plot(1:5,1:5,xlim=c(0.5,7),ylim=c(0,20000),type="n",
     axes= FALSE,ann=FALSE)

# add axes with labels
par(font.axis=2)
par(lwd=2)
axis(1,at=seq(1:7),labels=c("30 min. Treatment1", "1 hr. Treatment1", "2 hr. Treatment1", "3 hr. Treatment1", "4 hr. Treatment1", "9 hr. Treatment1", "9 hr. Control"), cex.axis=1.5)
axis(2, cex.axis=1.5)
mtext("Variance",side=2,line=2.5, cex=2, font=2)
mtext("Treatment",side=1,line=2.5, cex=2, font=2)
mtext("Variance by Treatment \nin CellType1 Cells",side=3,line=0, cex=2.3, font=2)
box(bty="L", lwd=2)
vars<-c(3202.755,3463.237,3033.06,5450.082,15175.995,8257.02,7155.488)
vars_L<-c(5489.693,4527.225,4040.472,7185.257,19859.45,12190.525,12010.269)
vars_U<-c(1520.068,2427.684,1976.856,3740.437,11006.45,3535.422,2758.258)

arrows(1:7,vars,1:7,vars_L,angle=90,length=0.1)
arrows(1:7,vars,1:7,vars_U,angle=90,length=0.1)
points(1:7,vars,pch=19,cex=1.5,col="blue",bg="blue")
abline(h=seq(0,20000,by=500),col="black",lty="dotted", lwd=1)
abline(h=seq(0,20000,by=1000),col="black",lty="dotted", lwd=2)

# Make boxplot combined with scatterplot of all transcripts during time course (9 hr. Control last):

all_transcripts<-read.table("10152017_random_CellType1_summary.txt", na.strings = "NA", sep="\t", header=T, check.names = F)

head(all_transcripts) # show first 5 rows of dataframe
# Make boxplot combined with scatterplot of all transcripts:
par(font.axis=2)
par(mgp = c(0, 0.6, 0))
par(oma = c(1, 1, 0, 0))
boxplot(all_transcripts, na.rm = T, lwd = 4, outline = FALSE, ylim=c(0,1000), names=c("30 min\n Treatment1","1 hr\n Treatment1","2 hr\n Treatment1","3 hr\n Treatment1","4 hr\n Treatment1","9 hr\n Treatment1","9 hr\n Control"), las=2, cex.axis=1.3)
title(main = "Total RNA transcripts during time course", cex.main=2)
title(ylab = "Total # transcripts/cell", line=2.75, cex.lab=1.8, font.lab=2)
title(xlab = "Treatment", cex.lab=1.8, font.lab = 2, line=3.5, cex.lab=1.8, font.lab=2)
box(lwd=2)
abline(h=seq(0,1000,by=50),col="black",lty="dotted", lwd=1.5)
stripchart(all_transcripts, vertical = TRUE, method = "jitter", add = TRUE, pch = 21, lwd=3, bg = 'magenta', cex=1)

par(mgp = c(0, 0.9, 0))
par(oma = c(0, 0, 0, 0))

# One way ANOVA:

# All transcripts

time_course_cells<-c(min30,hr1,hr2,hr3,hr4,hr9unstim)
time_course_treatment<-c(rep("min30",72),rep("hr1",79),rep("hr2",45),rep("hr3",80),rep("hr4",127),rep("hr9unstim",43))
time_course<-data.frame(time_course_cells,time_course_treatment)

#aov_time_course <- aov(time_course_cells ~ time_course_treatment, data=time_course)
#summary(aov_time_course)

# Nascent transcripts
nashr9unstim <- nascent_transcripts[,1]
nashr9unstim <- nashr9unstim[!is.na(nashr9unstim)]
nasmin30 <- nascent_transcripts[,2]
nasmin30 <- nasmin30[!is.na(nasmin30)]
nashr1 <- nascent_transcripts[,3]
nashr1 <- nashr1[!is.na(nashr1)]
nashr2 <- nascent_transcripts[,4]
nashr2 <- nashr2[!is.na(nashr2)]
nashr3 <- nascent_transcripts[,5]
nashr3 <- nashr3[!is.na(nashr3)]
nashr4 <- nascent_transcripts[,6]
nashr4 <- nashr4[!is.na(nashr4)]

nas_counts<-c(nashr9unstim,nasmin30,nashr1,nashr2,nashr3,nashr4)
nas_treatments<-c(rep("hr9unstim",8),rep("min30",23),rep("hr1",48),rep("hr2",28),rep("hr3",50),rep("hr4",18))
nas<-data.frame(nas_counts,nas_treatments)
head(nas)

#aov_nas <- aov(nas_counts ~ nas_treatments, data=nas)
#summary(aov_nas)

# Tukey's HSD:

# All transcripts

#TukeyHSD(aov_time_course, conf.level = 0.95)

# Nascent transcripts

#TukeyHSD(aov_nas, conf.level = 0.95)

# Statistical Testing:

# Assess nascent variance:

# applying variance calculation function to each time point:
# 24 hour:
vars_x<-apply(nas_drugs24, 2, make_var)
vars_x # tells us the variances calculated
# 6 hour:
vars_x<-apply(nas_drugs6, 2, make_var)
vars_x # tells us the variances calculated

# Kruskal Wallis Test because unequal variance for all transcripts and nascent transcripts:

# All transcripts
kruskal.test(time_course_cells ~ time_course_treatment, data=time_course)
# Nascent transcripts
kruskal.test(nas_counts ~ nas_treatments, data=nas)

## Dunn test
# install.packages("FSA")
library(FSA)
# Cite FSA if used in publication!!!! 
##      FSA package, version 0.8.5        ##
##    Derek H. Ogle, Northland College    ##
# All transcripts:
dunn_drug_dat = dunnTest(time_course_cells ~ time_course_treatment,
                         data=time_course,
                         method="bh")    
dunn_drug_dat

## Dunn test
# Nascent transcripts:
dunn_ndrug_dat = dunnTest(nas_counts ~ nas_treatments,
                            data=nas,
                            method="bh")    
dunn_ndrug_dat




