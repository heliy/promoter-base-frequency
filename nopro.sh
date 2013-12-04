#!/bin/bash

#得非启动子序列
#从GenBank上下载得人类第七号染色体序列的fasta文件
#从中随机抽取300作为非启动子序列
#用awk/cut
#由于数据量过大，随机抽取5行合并，取前300为所得

totalline=`cat $1 | wc -l`
awk 'BEGIN{srand();while(i<200000){k=int(rand()*'$totalline');if(!(k in a)){a[k]++;i++}}}(NR in a)' $1 | grep -v N > tmp
awk 'NR%5==1{print T;T=$0;next}{T=T""$0}' tmp | cut -c1-300
rm tmp
