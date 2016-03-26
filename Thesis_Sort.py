import numpy as np

def initialize(input_matrix):

    print(type(input_matrix))
    
def set_2_list(set_object):
    
    new_list  = []
    
    for x in set_object:
        new_list.append(x)
        
    return new_list
    
    
def all_possible(input_matrix):
    
    column_sets = []
    
    for x in np.arange(len(input_matrix[0])):
        
        column = []
        
        for y in np.arange(len(input_matrix)):
            
            column.append(input_matrix[y][x])
        
        set_var = set(column)
        unset_var = set_2_list(set_var)
        column_sets.append(unset_var)
        
        unset_column_sets = []
        for set_val in column_sets: 
            unset_column_sets.append(set_val)
        
    return unset_column_sets
    
def search_list(input_matrix, values_matrix):
    
    def position_check(row_position, row_matrix, values_matrix):
        check = 0
        for y in values_matrix[row_position]:
            print (y, row_matrix[row_position])
            if y == row_matrix[row_position] or None:
                check = 1
                print ('hi')
                return check
        return check
        
    gene_list = []
    full_gene_list = []
    full_list = []
    
    for row in input_matrix:
        for row_position in np.arange(len(row)):
            #print(position_check(row_position, row, values_matrix))
            if position_check(row_position, row, values_matrix) == 0:
                break
            
        gene_list.append(row[0])
        full_gene_list.append(row[0])
        full_list.append(row)
            
    set_gene_list = set(gene_list)
    unset_gene_list = set_2_list(set_gene_list) 
        
    return (unset_gene_list, full_gene_list, full_list)
            

#def create_set_or(input_matrix, values_matrix):
#    
#    gene_list = []
#    full_gene_list = []
#    stop = 0
#    
#    for w in np.arange(len(values_matrix)):
#        if stop == 1:
#            break
#        for x in values_matrix[w]:
#            for y in input_matrix:
#                for z in y:
#                    if x != None:
#                        stop = 1
#                        post_w_values = values_matrix[w + 1: len(values_matrix)]
#                        print (post_w_values)
#                        if x == z:
#                            print ('hi')
#                            contains = 0
#                            for w_1 in post_w_values:
#                                for x_1 in w_1:
#                                    if search(w_1,x):
#                                        contains = 1
#                            if contains == 1:
#                                gene_list.append(x[y][0])
#                                full_gene_list.append(x[y][0])
#                        
#    set_gene_list = set(gene_list)
#    unset_gene_list = set_2_list(set_gene_list) 
#        
#    return (unset_gene_list, full_gene_list)
    
# Cleanup removes a provided list of values from a provided list
                    
def cleanup(gene_list, removal_list):

    clean_gene_list = gene_list[:]    
    
    for x in removal_list:
        for z in gene_list:
            if x == z:
                clean_gene_list.remove(z)
                    
    return clean_gene_list
    
# Counter counts the number of repeats for each gene based on the original gene list. 
# Returns a dictionary with gene names as keys, and their counts as values
    
def counter(starting_matrix, clean_gene_list):
    
    gene_counts = []
    
    for x in clean_gene_list:
        counter = 0
        for y in starting_matrix:
            if x == y:
                counter = counter + 1
                
        gene_counts.append(counter)
    
    gene_count_dictionary = dict(zip(clean_gene_list, gene_counts))
        
    return gene_count_dictionary
                    
                
        
    
        
        
# Main Body

# Read in the data (Pre-processed Article_List)
starting_matrix = np.genfromtxt('Article_List.csv', dtype = ('U10','U10','U10','U10','U10','U10'), delimiter=',', skip_header = 1)
# List all possible values from the starting matrix
column_sets_list = all_possible(starting_matrix)

# Given a list of values, generates a list of all pertinent gene data 
values = [[],[], ['S','M'],[],[],['T']] # Exposure Types
#values = ['M'] # Exposure Type: Metals
(set_thing, raw_gene_list, full_list) = search_list(starting_matrix, values)

# Given a list of genes, removes the genes from a given gene list
clean_set_thing = cleanup(set_thing, [ 'xa' , 'blank' ])

# Counts the number of gene repeats in the value-based 
count_dict = counter(raw_gene_list, clean_set_thing)

print(count_dict, 'Values:', values)
print(len(count_dict))







