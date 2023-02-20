# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
filtered = dataiku.Dataset("filtered")
filtered_df = filtered.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test1_df = filtered_df # For this sample code, simply copy input to output


# Write recipe outputs
test1 = dataiku.Dataset("test1")
test1.write_with_schema(test1_df)
