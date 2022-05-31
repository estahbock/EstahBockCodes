c(.22,.20,.195)->control
c(.99,.98,.985)->mutation1
c(.19,.20,.17)->mutation2
sd(control)
sd(mutation1)
sd(mutation2)
?apply
data<-cbind(control,mutation1,mutation2)
apply(data,2,mean)
?t.test
data[,1]
t.test(control,mutation1)->t.test1
t.test1
c(control,mutation1)->all
all
data
data2<-data.frame(cbind(c("c","c","c","mutation1","mutation1","mutation1"),as.numeric(c(control,mutation1))))
colnames(data2)<-c("treatment","percent")
data2

t.by.permutation <- rep(0,1000)
for(i in 1:1000){
  treatment.random <- sample(data2$treatment)
  as.numeric(as.character(data2[treatment.random=="c",2]))->c.random
  as.numeric(as.character(data2[treatment.random=="mutation1",2]))->mutation1.random
  t.by.permutation[i] <- t.test(c.random,mutation1.random)$statistic
}
1000-sum(abs(t.by.permutation) < abs(t.test1$statistic))

t.by.permutation[abs(t.test1$statistic) < abs(t.by.permutation)]

## abs(t.by.permutation)

sum(abs(t.by.permutation) == abs(t.test1$statistic))

sum(abs(t.by.permutation) == abs(t.test1$statistic))/1000
