#!/bin/bash

#处理序列每个位置的ATGC频数
#结果输出行为位置 列为ATGC个数
#用cut

((col=`head -2 $1 |wc -m`-2));
for i in `seq "$col"`;
do
  row=`cut -c$i $1 ` #取出每一列
  Ano=`echo $row | grep -o 'A' | wc -c`
  Tno=`echo $row | grep -o 'T' | wc -c`
  Gno=`echo $row | grep -o 'G' | wc -c`
  Cno=`echo $row | grep -o 'C' | wc -c`
  echo -e "$Ano\t$Tno\t$Gno\t$Cno"
done
