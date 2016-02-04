# Copyright 2015-2016 David Hadka
#
# This file is part of Rhodium, a Python module for robust decision making and
# exploratory modeling.
#
# Rhodium is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Rhodium is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Rhodium.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import division, print_function, absolute_import

import six
import random
from abc import ABCMeta
from collections import OrderedDict
from .model import ListOfDict
        
def sample_lhs(model, nsamples):
    samples = OrderedDict()
    
    for uncertainty in model.uncertainties:
        levels = uncertainty.levels(nsamples)
        random.shuffle(levels)
        samples[uncertainty.name] = levels
        
    result = ListOfDict()
        
    for i in range(nsamples):
        entry = OrderedDict()
        
        for key, values in six.iteritems(samples):
            entry[key] = values[i]
    
        result.append(entry)
        
    return result
