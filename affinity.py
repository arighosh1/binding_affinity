#!/usr/bin/env python
# coding: utf-8

# In[21]:

import streamlit as st
from Bio.PDB import *
pdbl = PDBList()
pdbfile_id=""
pdbfile_id=input("Enter pdb id: ")
if len(pdbfile_id)>0:
    pdbl.retrieve_pdb_file(pdbfile_id, pdir='.', file_format='pdb')

    # In[2]:

    parser = PDBParser(PERMISSIVE=True, QUIET=True)

    # In[3]:

    data = parser.get_structure(pdbfile_id, "pdb" + pdbfile_id + ".ent")

    # In[6]:

    st.title(data.header["name"])

    # In[7]:

    model = data.get_models()
    model

    # In[8]:

    models = list(model)

    # In[10]:

    chains = list(models[0].get_chains())
    chains

    # In[12]:

    residue = list(chains[0].get_residues())
    atoms = list(residue[0].get_atoms())
    atoms

    # In[22]:

    st.title("binding affinity of protein is:", atoms[0].get_vector())

    # In[23]:

    # for model in data:   # X-Ray generally only have 1 model, while more in NMR
    #     for chain in model:
    #         for residue in chain:
    #             for atom in residue:
    #                 print(atom)
    #
    #
    # # In[26]:
    #
    #
    # atom.get_sigatm()        # std. dev. of atomic parameters
    #
    #
    # # In[27]:
    #
    #
    # atom.get_siguij()
    #
    #
    # # In[28]:
    #
    #
    # res_list = Selection.unfold_entities(data, 'R')
    #
    #
    # # In[29]:
    #
    #
    # res_list
    #
    #
    # # In[31]:
    #
    #
    # resolution = data.header['resolution']
    # resolution

else:
    st.text("Enter PDB ID")