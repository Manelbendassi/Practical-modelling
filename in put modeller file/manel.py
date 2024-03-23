# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:22:17 2024

@author: Skymil
"""

from modeller import *
from modeller.automodel import *

env = environ()


env.io.pdb_files_directory = ['C:\\Users\\Skymil\\Desktop\\atom_files\\1KXQ_A.pdb']

knowns = '1KXQ_A'

sequence = 'sp_P29957_AMY_PSEHA'

a = AutoModel(env,
  alnfile='alig.pir', 
  knowns=knowns,
  sequence=sequence,
  assess_methods=[assess.DOPE,
                  assess.GA341])
                  
a.starting_model = 1
a.ending_model = 10

a.make()


print("Modeling completed!")
