# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:29:35 2015

@author: gona
"""

import numpy as np

starting_matrix = np.genfromtxt('1.6.csv', dtype = ('U10','U10','U10','U10','U10','U10'), delimiter=',')

# Takes the starting_matrix, removes repeat genes, and then outputs a matrix
# with the remaining "set-like" genes and the correct study parameters..

def set_like(starting_matrix):
    
    gene_sublist= starting_matrix[0].copy()   
    gene_list = []
    
    for x in starting_matrix:
        gene_list.append(x[0])
        
    gene_set = set(gene_list)
    
    unset_gene_list = []
    
    for y in gene_set:
        unset_gene_list.append(y)
    
    print(unset_gene_list)
    output_matrix = []
    correct_gene_sublist = []
    for z in unset_gene_list:
        correct_gene_sublist = gene_sublist.copy(gene_sublist)
        correct_gene_sublist[0] = z
        output_matrix.append(correct_gene_sublist)
        
    return output_matrix
    
output_matrix = set_like(starting_matrix)  

np.savetxt('1.6_set1.csv', output_matrix, delimiter = ',', fmt = "%s")
print (output_matrix)      
        