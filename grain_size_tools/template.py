# ============================================================================ #
#                                                                              #
#    This is part of the "GrainSizeTools Script"                               #
#    A Python script for characterizing grain size from thin sections          #
#                                                                              #
#    Copyright (c) 2014-present   Marco A. Lopez-Sanchez                       #
#                                                                              #
#    Licensed under the Apache License, Version 2.0 (the "License");           #
#    you may not use this file except in compliance with the License.          #
#    You may obtain a copy of the License at                                   #
#                                                                              #
#        http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                              #
#    Unless required by applicable law or agreed to in writing, software       #
#    distributed under the License is distributed on an "AS IS" BASIS,         #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#    See the License for the specific language governing permissions and       #
#    limitations under the License.                                            #
#                                                                              #
#    Version 3.0rc                                                             #
#    For details see: http://marcoalopez.github.io/GrainSizeTools/             #
#    download at https://github.com/marcoalopez/GrainSizeTools/releases        #
#                                                                              #
# ============================================================================ #

import matplotlib as mpl
from cycler import cycler

# Set the plot style
mpl.rcParams['font.family'] = 'Helvetica Neue'  # set your own font family
mpl.rcParams['font.size'] = 14.0
mpl.rcParams['svg.fonttype'] = 'path'
mpl.rcParams['lines.linewidth'] = 3.0
mpl.rcParams['lines.markersize'] = 12.0
mpl.rcParams['lines.solid_capstyle'] = 'butt'
mpl.rcParams['legend.fancybox'] = True

mpl.rcParams['axes.prop_cycle'] = cycler(color=['#008fd5', '#fc4f30', '#e5ae38', '#6d904f', '#8b8b8b', '#810f7c'])
mpl.rcParams['axes.facecolor'] = 'ffffff'
mpl.rcParams['axes.labelsize'] = 'large'
mpl.rcParams['axes.axisbelow'] = True
mpl.rcParams['axes.grid'] = True
mpl.rcParams['axes.edgecolor'] = 'ffffff'
mpl.rcParams['axes.linewidth'] = 2.0
mpl.rcParams['axes.titlesize'] = 'x-large'

mpl.rcParams['patch.edgecolor'] = 'f0f0f0'
mpl.rcParams['patch.linewidth'] = 0.5

mpl.rcParams['grid.linestyle'] = '-'
mpl.rcParams['grid.linewidth'] = 1.0
mpl.rcParams['grid.color'] = 'cbcbcb'

mpl.rcParams['xtick.major.size'] = 0
mpl.rcParams['xtick.minor.size'] = 0
mpl.rcParams['ytick.major.size'] = 0
mpl.rcParams['ytick.minor.size'] = 0
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['xtick.color'] = '#252525'
mpl.rcParams['ytick.color'] = '#252525'

mpl.rcParams['savefig.edgecolor'] = 'ffffff'
mpl.rcParams['savefig.facecolor'] = 'ffffff'

mpl.rcParams['figure.subplot.left'] = 0.125
mpl.rcParams['figure.subplot.right'] = 0.9
mpl.rcParams['figure.subplot.bottom'] = 0.11
mpl.rcParams['figure.subplot.top'] = 0.88
mpl.rcParams['figure.facecolor'] = 'ffffff'

if __name__ == '__main__':
    pass
else:
    print('module template imported')
