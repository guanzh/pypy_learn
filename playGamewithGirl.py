
malePro = 0.8
femalePro = 0.2
N = 100
P = 1000
bG = 3
lG = 1
lo = -2
maleG = numeric()
f = numeric()
plot(1:20,xlim = c(0,N),ylim = c(-100,100),type = "n")

for (j in 1:P){
    male <- sample(c(1,0), size=N, replace=TRUE, prob=c(malePro, 1-malePro))
    female <- sample(c(1,0), size=N, replace=TRUE, prob=c(femalePro, 1-femalePro))
    for (i in 1:N){
        if (male[i]==1 & female[i]==1){
            maleG[i] = bG
        } else if (male[i]==0 & female[i]==0){
            maleG[i]= lG
        } else maleG[i]=lO
    }
    lines(cumsum(maleG))
    f[j] = cumsum(maleG)[N]
}

hist(f)
