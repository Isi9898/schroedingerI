#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 12:59:12 2018

@author: isi
"""

import numpy as np
import matplotlib.pyplot as plt


def visualize(bulge_factor):
    """load data files"""
    xx = np.loadtxt("potential.dat")[:, 0]
    potential = np.loadtxt("potential.dat")[:, 1]
    energies = np.loadtxt("energies.dat")
    wavefuncs = np.loadtxt("wavefuncs.dat")[:, 1:]
    expvalues = np.loadtxt("expvalues.dat")[:, 0]
    uncertainty = np.loadtxt("expvalues.dat")[:, 1]

    #plotting potential, energies, wafefunctions and expactationvalues
    plt.subplot(1, 2, 1)
    plt.plot(xx, potential, color="black")

    aa = bulge_factor

    bb = len(energies)
    for ii in range(0, bb):
        energy = np.linspace(energies[ii], energies[ii], len(xx))
        plt.plot(xx, energy, color="gray")
        plt.plot(expvalues, energies, "xg")
        if ii % 2 == 0:
            plt.plot(xx, aa*wavefuncs[:, ii]+energies[ii], color="blue")
        else:
            plt.plot(xx, aa*wavefuncs[:, ii]+energies[ii], color="red")
    plt.xlim(xx.min() * 1.1, xx.max() * 1.1)
    plt.ylim(energies.min() * (-1.1), energies.max() * 1.1)
    plt.xlabel("$x$ [Bohr]")
    plt.ylabel("Energy [Hartree]")
    plt.title("Potential, eigenstates, ($x$)")

    #plotting energies and uncertainty
    plt.subplot(1, 2, 2)
    bb = len(energies)
    for ii in range(0, bb):
        energy = np.linspace(energies[ii], energies[ii], len(xx))
        plt.plot(xx, energy, color="gray")
        plt.plot(uncertainty, energies, "+m")
        plt.yticks([])
    plt.xlim(0, uncertainty.max() * 1.1)
    plt.ylim(energies.min() * (-1.1), energies.max() * 1.1)
    plt.xlabel("[Bohr]")
    plt.title("$\sigma_\mathrm{x}$")

    plt.savefig("solution_schoedinger.pdf", format="pdf")
