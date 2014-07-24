args <- commandArgs(TRUE)
if(length(args)){
    input <- strsplit(strsplit(args,split=",")[[1]],"")
    me <- input[[1]]
    opponent <- input[[2]]
    sharpness <- 0
    for(i in seq_along(opponent)){
        if(opponent[i]=="S") sharpness <- sharpness + 1
        if(opponent[i]=="P") sharpness <- sharpness - 1
        }
    out <- ifelse(sharpness>0,"B","S")
    bfree <- me[me!="B"]
    r <- rle(bfree) #run length encoding
    S_sequence <- r$length[r$value=="S"]
    P_sequence <- r$length[r$value=="P"]
    if(!length(P_sequence)) P_sequence <- 0
    if(tail(S_sequence,1)==5 & tail(P_sequence,1)!=5) out <- "P"
}else{out <- "S"}
cat(out)