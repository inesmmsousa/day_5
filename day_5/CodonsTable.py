'''
Created on 09/02/2018

@author: Utilizador
'''
from Bio import SeqIO
import csv

class CodonsTable(object):
    '''
    classdocs
    '''

    dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    
    def __init__(self):
        '''
        Constructor
        '''
        self.lst_data = []
        for i in range(64): self.lst_data.append([0] * 64)
        
    def count_codons(self, file_in):
        '''
        param: fasta file
        return: None
        '''
        
        with open(file_in) as handle_in:
            for seq in SeqIO.parse(handle_in, 'fasta'):
                self.count_codons_by_sequence(str(seq.seq).upper())
                
    def count_codons_by_sequence(self, sequence):
        '''
        param: dna sequence
        return: None
        '''
        for i in range(5, len(sequence), 3):
            self.count_pair_codons(sequence[i-5], sequence[i-4], sequence[i-3], sequence[i-2], sequence[i-1], sequence[i] )
            
    def count_pair_codons(self, C1_1, C1_2, C1_3, C2_1, C2_2, C2_3):
        '''
        '''
        index_1 = self.get_pos_codon(C1_1, C1_2, C1_3)
        if (index_1 == -1): return
        index_2 = self.get_pos_codon(C2_1, C2_2, C2_3)
        if (index_2 == -1): return
        self.lst_data[self.get_pos_codon(C1_1, C1_2, C1_3)][self.get_pos_codon(C2_1, C2_2, C2_3)] += 1
        
    def get_pos_codon(self, b1, b2, b3):
            
            if ( b1 in self.dict and b2 in self.dict and b3 in self.dict):
                return (self.dict[b1] << 4) + (self.dict[b2] << 2) + (self.dict[b3])
            else: return -1
            return
    def save_table_in_file(self, file_out):
        '''
        param: file_out
        return: None
        '''
        with open(file_out, 'w', newline='') as handle_out:
            csv_writer = csv.writer(handle_out, delimiter=',', quoting=csv.QUOTE_NONE)
            
            for lst_row in self.lst_data:
                csv_writer.writerow(lst_row)   
        