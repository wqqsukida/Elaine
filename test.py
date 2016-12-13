#!/usr/bin/env python
# coding:utf-8
from multiprocessing import Pool
import time

def f(x):
	time.sleep(2)
	return x*x

if __name__ == '__main__':
	p = Pool(5)
	print p.map(f,[1,2,3,4,5])
