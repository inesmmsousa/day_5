'''
Created on 09/02/2018

@author: Utilizador
'''
import unittest
from CodonsTable import CodonsTable
import os


class Test(unittest.TestCase):

    def test_count_codons(self):
        codons_table = CodonsTable()
        codons_table.count_codons(os.path.join('tests', 'test_fasta_file.fasta'))
        self.assertEqual(3, codons_table.lst_data[0] [21])
        self.assertEqual(1, codons_table.lst_data[21] [21])
        self.assertEqual(2, codons_table.lst_data[0] [63])
         
        pass
    
    def test_count_codons_by_sequence(self):
        codons_table = CodonsTable()
        self.assertEqual(0, codons_table.lst_data[0][21])
        codons_table.count_codons_by_sequence('AAACCC')
        self.assertEqual(1, codons_table.lst_data[0][21])
        codons_table.count_codons_by_sequence('AAACCC')  
        self.assertEqual(2, codons_table.lst_data[0][21])
        codons_table.count_codons_by_sequence('AAACCCCCC')
        self.assertEqual(3, codons_table.lst_data[0][21])
        self.assertEqual(1, codons_table.lst_data[21][21])
        
        self.assertEqual(0, codons_table.lst_data[0][63])
        codons_table.count_codons_by_sequence('AAACCC')
        self.assertEqual(1, codons_table.lst_data[0][63])
        codons_table.count_codons_by_sequence('AAATTTC')  
        self.assertEqual(2, codons_table.lst_data[0][63])
       
       
    
    def test_count_pair_codons(self):
        codons_table = CodonsTable()
        self.assertEqual(0, codons_table.lst_data[0][0])
        codons_table.count_pair_codons('A', 'A', 'A', 'A', 'A', 'A')
        self.assertEqual(1, codons_table.lst_data[0][0])
        
        self.assertEqual(0, codons_table.lst_data[63][0])
        codons_table.count_pair_codons('T', 'T', 'T', 'A', 'A', 'A')
        
        self.assertEqual(0, codons_table.lst_data[63][63])
        codons_table.count_pair_codons('T', 'T', 'T', 'T', 'T', 'T')
        self.assertEqual(1, codons_table.lst_data[63][63])
        codons_table.count_pair_codons('T', 'T', 'T', 'T', 'T', 'T')
        self.assertEqual(2, codons_table.lst_data[63][63])
        codons_table.count_pair_codons('T', 'T', 'T', 'A', 'c', 'd')
        
        
        
    
    def test_get_pos_codons(self):
        codons_table = CodonsTable()
        self.assertEqual(0, codons_table.get_pos_codon('A', 'A', 'A'))
        self.assertEqual(-1, codons_table.get_pos_codon('A', 'A', 'a'))
        self.assertEqual(-1, codons_table.get_pos_codon('A', 'a', 'C'))
        self.assertEqual(-1, codons_table.get_pos_codon('z', 'A', 'G'))
        self.assertEqual(63, codons_table.get_pos_codon('T', 'T', 'T'))
        self.assertEqual(3, codons_table.get_pos_codon('A', 'A', 'T'))
        self.assertEqual(15, codons_table.get_pos_codon('A', 'T', 'T'))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_count_codons_by_sequence']
    unittest.main()