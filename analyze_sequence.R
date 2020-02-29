GC <- read.csv("outputnew.csv")
str(GC)

glm((Reads*X.GC.content ~ , data= GC))

#Subset data into High and Low GC content based on mean GC content
GC_data1 <- ifelse(GC$X.GC.content >=0.356, "High", "Low")
str(GC_data1)

GC_data1<- as.factor(GC_data1)
str(GC_data1)

mod1<- glm(GC$X.GC.content ~ GC_data1, family= binomial)
summary(mod1)
