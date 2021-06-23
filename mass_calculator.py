import streamlit as st
import numpy as np
import pandas as pd
from mass_converter import MassConverter

st.title('Mass calculator for mass spectrometry')


def build_column_of_isotopes(neutral_mass, charge):
    mass_converter = MassConverter()
    isotopes = []
    for isotope in range(0, 10):
        isotopes += [mass_converter.NeutralMonoisotopicMassToObservedMz(
            neutral_mass, charge, isotope)]
    return isotopes


def build_mass_table(neutral_mass):
    charges = []
    for charge in range(-10, 11):
        charges += [build_column_of_isotopes(neutral_mass, charge)]
    return charges


neutral_mass = st.number_input(
    label='Enter a neutral monoisotopic mass', format="%.5f")

charges = ['-10', '-9', '-8', '-7', '-6', '-5', '-4', '-3', '-2',
           '-1', 'Neutral mass', '+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+8', '+10']

mass_table = build_mass_table(neutral_mass)
mass_data_frame = pd.DataFrame(mass_table, columns=['Monoisotopic m/z', 'Isotope 1', 'Isotope 2',
                               'Isotope 3', 'Isotope 4', 'Isotope 5', 'Isotope 6', 'Isotope 7', 'Isotope 8', 'Isotope 9'],
                               )
mass_data_frame.insert(loc=0, column='Charge', value=charges)

st.dataframe(mass_data_frame.style.format({1: '{:.5f}'}))

st.markdown('## Mass error calculator')

expected_mass = abs(st.number_input(
    label='Enter an expected mass', format="%.5f"))
observed_mass = abs(st.number_input(
    label='Enter an observed mass', format="%.5f"))

if (expected_mass > 0 and observed_mass > 0):
    ppm_error = abs(observed_mass - expected_mass) / expected_mass * 1e6
    st.markdown(f'### Mass error = {ppm_error:.5f} ppm')
