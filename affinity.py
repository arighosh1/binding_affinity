#!/usr/bin/env python
# coding: utf-8

# In[21]:

import streamlit as st
from Bio.PDB import *


pdbl = PDBList()
filename=''
uploaded_files = st.file_uploader("Choose a  File To Check Its Binding Affinity : ", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    file = uploaded_file.read()
    filename=uploaded_file.name


if len(filename)>0:
    filename=filename.replace(".pdb", "")
    pdbl.retrieve_pdb_file(file, pdir='.', file_format='pdb')

    # In[2]:

    parser = PDBParser(PERMISSIVE=True, QUIET=True)

    # In[3]:
    uploaded_file_name="pdb" + filename + ".ent"
    data = parser.get_structure(filename, uploaded_file_name)

    # In[6]:

    st.text(data.header["name"])

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

    # In[22]:
    st.title("The Entered file has following binding affinity : ")
    st.text(atoms[0].get_vector())
    # In[23]:
    #
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
#
else:
    st.text("Upload PDB file...")
