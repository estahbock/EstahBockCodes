
# Set so sampling is consistent every time
set.seed(723)

# sample from normal distribution with mean 0 and sd 1

a<-rnorm(1000)
b<-rnorm(1000)
c<-rnorm(1000)
d<-rnorm(1000)
e<-rnorm(1000)
f<-rnorm(1000)
g<-rnorm(1000)
h<-rnorm(1000)

mean(a)
sd(a)
mean(b)
sd(b)
mean(c)
sd(c)
mean(d)
sd(d)
mean(e)
sd(e)
mean(f)
sd(f)
mean(g)
sd(g)
mean(h)
sd(h)

data_samp_1000<-data.frame(a,b,c,d,e,f,g,h)

#boxplots for different sample sizes

boxplot(data_samp_1000) #sample size of 1000 each

boxplot(data_samp_1000[1:3,]) #sample size of 3 each

boxplot(data_samp_1000[1:5,]) #sample size of 5 each

boxplot(data_samp_1000[1:10,]) #sample size of 10 each

boxplot(data_samp_1000[1:15,]) #sample size of 15 each

boxplot(data_samp_1000[1:30,]) #sample size of 30 each

boxplot(data_samp_1000[1:50,]) #sample size of 50 each

boxplot(data_samp_1000[1:100,]) #sample size of 100 each

# t tests for sample size of 30

t.test(a[1:30],b[1:30])

t.test(a[1:30],c[1:30])

t.test(a[1:30],d[1:30])

t.test(a[1:30],e[1:30])

t.test(a[1:30],f[1:30])

t.test(a[1:30],g[1:30])

t.test(a[1:30],h[1:30])

t.test(b[1:30],c[1:30])

t.test(b[1:30],d[1:30])

t.test(b[1:30],e[1:30]) # p-value = 0.04354

t.test(b[1:30],f[1:30])

t.test(b[1:30],g[1:30])

t.test(b[1:30],h[1:30])

t.test(c[1:30],d[1:30])

t.test(c[1:30],e[1:30]) # p-value = 0.008971

t.test(c[1:30],f[1:30])

t.test(c[1:30],g[1:30])

t.test(c[1:30],h[1:30])

t.test(d[1:30],e[1:30])

t.test(d[1:30],f[1:30])

t.test(d[1:30],g[1:30])

t.test(d[1:30],h[1:30])

t.test(e[1:30],f[1:30]) # p-value = 0.03811

t.test(e[1:30],g[1:30])

t.test(e[1:30],h[1:30])

t.test(f[1:30],g[1:30])

t.test(f[1:30],h[1:30])

t.test(g[1:30],h[1:30])

# testing with anova

treatment<-c(rep("a",30),rep("b",30),rep("c",30),rep("d",30),rep("e",30),rep("f",30),rep("g",30),rep("h",30))

outcome<-c(a[1:30],b[1:30],c[1:30],d[1:30],e[1:30],f[1:30],g[1:30],h[1:30])

samp30dataframe<-data.frame(outcome,treatment)

head(samp30dataframe)

samp30_aov <- aov(outcome ~ treatment, data = samp30dataframe)

summary(samp30_aov) # Not significant with ANOVA F value = 1.225, p-value = 0.29

# t-tests with corrections

pairwise.t.test(samp30dataframe$outcome, samp30dataframe$treatment)

pairwise.t.test(samp30dataframe$outcome, samp30dataframe$treatment, p.adjust.method = "BH")

pairwise.t.test(samp30dataframe$outcome, samp30dataframe$treatment, p.adjust.method = "bonferroni")  

pairwise.t.test(samp30dataframe$outcome, samp30dataframe$treatment, p.adjust.method = "fdr")  

# ANOVA with sample size of 3, each

treatment3samp<-c(rep("a",3),rep("b",3),rep("c",3),rep("d",3),rep("e",3),rep("f",3),rep("g",3),rep("h",3))

outcome3samp<-c(a[1:3],b[1:3],c[1:3],d[1:3],e[1:3],f[1:3],g[1:3],h[1:3])

samp3dataframe<-data.frame(outcome3samp,treatment3samp)

head(samp3dataframe)

samp3_aov <- aov(outcome3samp ~ treatment3samp, data = samp3dataframe)

summary(samp3_aov) # Significant with ANOVA F value = 2.837, p-value = 0.0399

TukeyHSD(samp3_aov) # d vs h is statistically significant even after correction, with p-adj = 0.0411657


# Try also t-test and ANOVA with random sampling from skewed distribution





# Look at correlations:

head(data_samp_1000)

plot(a,b)

plot(a[1:10],b[1:10])

plot(a,c)

plot(a[1:10],c[1:10])

plot(a,d)

plot(a[1:10],d[1:10])

plot(a,e)

plot(a[1:10],e[1:10])

plot(a,f)

plot(a[1:10],f[1:10])

plot(a,g)

plot(a[1:10],g[1:10])

plot(a,h)

plot(a[1:10],h[1:10])

# install.packages("ggpubr")

# library("ggpubr")

# cor(x, y, method = c("pearson", "kendall", "spearman"))
# cor.test(x, y, method=c("pearson", "kendall", "spearman"))

# Shapiro-Wilk normality test

shapiro.test(a[1:10])
shapiro.test(b[1:10])
shapiro.test(c[1:10])
shapiro.test(d[1:10])
shapiro.test(e[1:10])
shapiro.test(f[1:10])
shapiro.test(g[1:10])
shapiro.test(h[1:10])

test_cor_ab<-cor.test(a, b, method = "pearson")

test_cor_ab

test_cor_ab_10<-cor.test(a[1:10], b[1:10], method = "pearson")

test_cor_ab_10

test_cor_ac_10<-cor.test(a[1:10], c[1:10], method = "pearson")

test_cor_ac_10

test_cor_ad_10<-cor.test(a[1:10], d[1:10], method = "pearson")

test_cor_ad_10

test_cor_ae_10<-cor.test(a[1:10], e[1:10], method = "pearson")

test_cor_ae_10

test_cor_af_10<-cor.test(a[1:10], f[1:10], method = "pearson")

test_cor_af_10

test_cor_ag_10<-cor.test(a[1:10], g[1:10], method = "pearson")

test_cor_ag_10

test_cor_ah_10<-cor.test(a[1:10], h[1:10], method = "pearson")

test_cor_ah_10

test_cor_bc_10<-cor.test(b[1:10], c[1:10], method = "pearson")

test_cor_bc_10

test_cor_bd_10<-cor.test(b[1:10], d[1:10], method = "pearson")

test_cor_bd_10

test_cor_be_10<-cor.test(b[1:10], e[1:10], method = "pearson")

test_cor_be_10

test_cor_bf_10<-cor.test(b[1:10], f[1:10], method = "pearson")

test_cor_bf_10

test_cor_bg_10<-cor.test(b[1:10], g[1:10], method = "pearson")

test_cor_bg_10

test_cor_bh_10<-cor.test(b[1:10], h[1:10], method = "pearson")

test_cor_bh_10

test_cor_cd_10<-cor.test(c[1:10], d[1:10], method = "pearson")

test_cor_cd_10

test_cor_ce_10<-cor.test(c[1:10], e[1:10], method = "pearson")

test_cor_ce_10

test_cor_cf_10<-cor.test(c[1:10], f[1:10], method = "pearson")

test_cor_cf_10

test_cor_cg_10<-cor.test(c[1:10], g[1:10], method = "pearson")

test_cor_cg_10

test_cor_ch_10<-cor.test(c[1:10], h[1:10], method = "pearson")

test_cor_ch_10 # p-value = 0.02707, cor = -0.690495 

plot(c[1:10],h[1:10])

test_cor_de_10<-cor.test(d[1:10], e[1:10], method = "pearson")

test_cor_de_10

test_cor_df_10<-cor.test(d[1:10], f[1:10], method = "pearson")

test_cor_df_10

test_cor_dg_10<-cor.test(d[1:10], g[1:10], method = "pearson")

test_cor_dg_10 # p-value = 0.0398, cor = 0.6550618

plot(d[1:10],g[1:10])

test_cor_dh_10<-cor.test(d[1:10], h[1:10], method = "pearson")

test_cor_dh_10 # p-value = 0.01283, cor = -0.7481

plot(d[1:10],h[1:10])

test_cor_ef_10<-cor.test(e[1:10], f[1:10], method = "pearson")

test_cor_ef_10

test_cor_eg_10<-cor.test(e[1:10], g[1:10], method = "pearson")

test_cor_eg_10

test_cor_eh_10<-cor.test(e[1:10], h[1:10], method = "pearson")

test_cor_eh_10

test_cor_fg_10<-cor.test(f[1:10], g[1:10], method = "pearson")

test_cor_fg_10

test_cor_fh_10<-cor.test(f[1:10], h[1:10], method = "pearson")

test_cor_fh_10

test_cor_gh_10<-cor.test(g[1:10], h[1:10], method = "pearson")

test_cor_gh_10 # p-value = 0.02886, cor = -0.6849203

plot(g[1:10],h[1:10])

# correlation with large sample sizes

x<-rnorm(1000000)
y<-rnorm(1000000)

test_cor_xy_10<-cor.test(x[1:10], y[1:10], method = "pearson")

test_cor_xy_10 # p-value = 0.02066, cor = 0.712896

lm_1mil<-lm(y ~ x)

summary(lm_1mil) # with linear regression, ns

lm_10<-lm(y[1:10] ~ x[1:10])

summary(lm_10) # p-value: 0.02066, p-val = 0.0207 for slope = 0.7565

plot(x[1:10],y[1:10])

lm_15<-lm(y[1:15] ~ x[1:15])

summary(lm_15) # ns

plot(x[1:15],y[1:15])

lm_20<-lm(y[1:20] ~ x[1:20])

summary(lm_20) # ns

lm_25<-lm(y[1:25] ~ x[1:25])

summary(lm_25) # p-value: 0.04295, p-val = 0.043 for slope 0.46358

plot(x[1:25],y[1:25])

lm_30<-lm(y[1:30] ~ x[1:30])

summary(lm_30) # ns

lm_35<-lm(y[1:35] ~ x[1:35])

summary(lm_35) # p-value: 0.03058, p-val = 0.0306 for slope 0.3475

plot(x[1:35],y[1:35])

lm_40<-lm(y[1:40] ~ x[1:40])

summary(lm_40) # p-value: 0.01613, p-val = 0.0161 for slope 0.35923

plot(x[1:40],y[1:40])

lm_45<-lm(y[1:45] ~ x[1:45])

summary(lm_45) # p-value: 0.006304, p-val = 0.0063 for slope 0.38890

plot(x[1:45],y[1:45])

lm_50<-lm(y[1:50] ~ x[1:50])

summary(lm_50) # p-value: 0.00864, p-val = 0.00864 for slope 0.355432

plot(x[1:50],y[1:50])

lm_55<-lm(y[1:55] ~ x[1:55])

summary(lm_55) # p-value: 0.02148, p-val = 0.0215 for slope 0.29863

plot(x[1:55],y[1:55])

lm_60<-lm(y[1:60] ~ x[1:60])

summary(lm_60) # p-value: 0.0241, p-val = 0.0241 for slope 0.2901

plot(x[1:60],y[1:60])

lm_65<-lm(y[1:65] ~ x[1:65])

summary(lm_65) # p-value: 0.01133, p-val = 0.0113 for slope 0.31303

plot(x[1:65],y[1:65])

lm_70<-lm(y[1:70] ~ x[1:70])

summary(lm_70) # p-value: 0.005404, p-val = 0.0054 for slope 0.32522

plot(x[1:70],y[1:70])

lm_75<-lm(y[1:75] ~ x[1:75])

summary(lm_75) # ns

plot(x[1:75],y[1:75])

lm_80<-lm(y[1:80] ~ x[1:80])

summary(lm_80) # ns

lm_85<-lm(y[1:85] ~ x[1:85])

summary(lm_85) # ns

plot(x[1:85],y[1:85])

lm_90<-lm(y[1:90] ~ x[1:90])

summary(lm_90) # ns

lm_95<-lm(y[1:95] ~ x[1:95])

summary(lm_95) # ns

plot(x[1:95],y[1:95])

lm_100<-lm(y[1:100] ~ x[1:100])

summary(lm_100) # ns

lm_150<-lm(y[1:150] ~ x[1:150])

summary(lm_150) # ns

lm_1000<-lm(y[1:1000] ~ x[1:1000])

summary(lm_1000) # ns

lm_10000<-lm(y[1:10000] ~ x[1:10000])

summary(lm_10000) # ns

lm_100000<-lm(y[1:100000] ~ x[1:100000])

summary(lm_100000) # ns

