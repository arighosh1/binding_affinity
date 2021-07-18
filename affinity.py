#!/usr/bin/env python
# coding: utf-8

# In[21]:

import streamlit as st
from Bio.PDB import *
from quantiprot.metrics.aaindex import get_aa2charge, get_aa2hydropathy
import os
import streamlit as st
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def affinity():
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
        st.text("Enter PDB ID")

def antigency():
    # !/usr/bin/env python
    # coding: utf-8

    # In[51]:

    
    file = ''
    uploaded_files = st.file_uploader("Choose a Protein File To Check Its Antigenicity : ", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        file = uploaded_file.read()

    if file != '':

        X = ProteinAnalysis(str(file))

        # st.write("number of alanine in protein is = ", X.count_amino_acids()['A'])
        # st.write("number of valine in protein is = ",X.count_amino_acids()['V'])
        # st.write("number of  isoleucine in protein is = ",X.count_amino_acids()['L'])
        # st.write("number of leucine in protein is = ",X.count_amino_acids()['I'])
        alanine = X.get_amino_acids_percent()['A']
        valine = X.get_amino_acids_percent()['V']
        isoleucine = X.get_amino_acids_percent()['I']
        leucine = X.get_amino_acids_percent()['L']
        # st.write(alanine)
        # st.write(valine)
        # st.write(isoleucine)
        # st.write(leucine)
        # st.write("molecular_weight =", X.molecular_weight())
        # st.write("Aromaticity = ",X.aromaticity())
        # st.write("instability_index = ",X.instability_index())
        # st.write("Isoelectric point = ",X.isoelectric_point())
        sec_struc = X.secondary_structure_fraction()
        # st.write("Secondary structure fraction = ",sec_struc[0])
        epsilon_prot = X.molar_extinction_coefficient()
        # st.write(epsilon_prot)

        # In[52]:

        # Aliphatic index = X(Ala) + a * X(Val) + b * ( X(Ile) + X(Leu) )
        Aliphatic_index = ((alanine + 2.9) * (valine + 3.9) * (isoleucine + leucine)) / 10

        # In[53]:

        # st.write(Aliphatic_index)

        # In[54]:

        if Aliphatic_index >= 0.1:
            st.title("The Protein is antigenic protein")
        else:
            st.title("The Protein is non-antigenic protein")

    else:
        st.text("Input Your Sequence")


binding_affinity=st.button("Binding Affinity")
antigencity=st.button("Antigencity")

if(binding_affinity==True):
    affinity()
elif antigencity==True:
    antigency()
