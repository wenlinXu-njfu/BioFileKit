#!/usr/env/bin Rscript

cmd=commandArgs(trailingOnly=TRUE)
input=cmd[1]
output=cmd[2]
d=read.table(input)
png(file=output)
hist(d$V1,main="Insertion Size distribution",ylab="Read Count",xlab="Insert Size",xaxt="n",breaks=seq
(0,max(d$V1,by=1)))
axis(side=1,at=seq(0,max(d$V1),by=100),labels=seq(0,max(d$V1),by=100))
dev.off()