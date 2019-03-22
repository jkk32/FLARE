
import numpy as np
import matplotlib.pyplot as plt 

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from FLARE.SED import models
import FLARE.filters

import numpy as np
import _pickle as pickle

# import FLARE



# --- create a simple "beta" model with a power law slope and a break at 912.

m = models.beta(np.arange(0., 2000., 1.), -2.5, 1E28, normalisation_wavelength = 1500.)

# --- now move to the observer frame

cosmo = FLARE.default_cosmo()

z = 8.

m.get_fnu(cosmo, z) # --- generate observed frame spectrum (necessary to get broad band photometry)

# --- define filters

filters = FLARE.filters.Euclid

F = FLARE.filters.add_filters(filters, new_lam = m.lam * (1. + z)) 

# --- generates Fnu (broad band fluxes)

m.get_Fnu(F) 

for f in filters: print('{f}: {flux}/nJy'.format(f = f, flux = m.Fnu[f]))

# --- add noise [JK to do]
center = 2.
sigma = 1.

noise = {}
for f in filters: noise[f] = np.random.normal(center, sigma, m.Fnu[f].shape) # MAYBE??

background = 2. # nJy # noise

completeness_limit = 5. * background # the completeness limit (currently def\
ined by an error function)
stretch = 0.5 # stretches error function. if stretch is very big the erf bec\
omes a step

N = 1000

bwL = 0.05
bwz = 0.05

logL1500 = logL1500_middle - bwL/2. + bwL * np.random.random(N)

# --- create EAZY filter RES file

filter_res_file = 'Euclid.FILTER.RES'

FLARE.filters.create_EAZY_filter_res(F, filter_res_file = filter_res_file)


# --- run EAZY [JK to do]
eazy_software_location = '/research/astro/flare/software/eazy/'
eazy_input_location = '/'
eazy_identifier = '/'

os.system(eazy_software_location + ' -p '+eazy_input_location+'/zphot'+eazy_identifier+'.param')


# --- read in EAZY [JK to do]
eazy_output_location = '/'

z_mc = np.loadtxt(eazy_output_location+'photz'+eazy_identifier+'.zout', usecols = -1)




