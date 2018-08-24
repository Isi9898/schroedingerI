#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:39:23 2018

@author: isi
"""

import schroed_solver.py
import schroed_visualize.py


schroed_solver.solver("schrodinger.inp")
schroed_visualize.visualize(bulge_factor=2)
