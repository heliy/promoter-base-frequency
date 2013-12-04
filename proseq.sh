#!/bin/bash

#处理ped上的启动子序列为完整的序列信息
#行为每个启动子的碱基
#输入文件为 **.pl html保存的靠边
#用awk

awk '/to/{print T;T="";next}{T=T""$0}' $1 | grep -v N 

