# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:39:28 2019

@author: Hadyan Pratama
"""

"""An example of showing AVO Similarity."""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Quick Screening of AVO Similarity")
st.markdown(
"""
This is a demo of a Streamlit app that shows quick scrrening of AVO
Similarity. This is my ultimate form of my internship
project at SIS Schlumberger. Use the slider
to pick a similarity value and look at how the curve.
[See source code](https://github.com/streamlit/demo-uber-nyc-pickups/blob/master/app.py)
""")