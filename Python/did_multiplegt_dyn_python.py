# Windows:
# Add R info to environmental variables
# 1. Add R to PATH: C:\Program Files\R\R-4.3.2\bin\x64
# 2. Create R_HOME: C:\Program Files\R\R-4.3.2
# 3. Create R_USER: user from Sys.info()

# Download latest version of rpy2: http://www.lfd.uci.edu/~gohlke/pythonlibs/#rpy2
# pip install rpy2-2.9.5-cp37-cp37m-win_amd64.whl

# pip install wooldridge
# pip install tzlocal

import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects import numpy2ri
import wooldridge

pandas2ri.activate()
wagepan = pandas2ri.py2ri(wooldridge.data('wagepan'))

did = robjects.r('''
                 library(DIDmultiplegtDYN)
                 did_multiplegt_dyn(df = wagepan, outcome = "lwage", group = "nr", time = "year", treatment = "union", effects = 2)
                 ''')
print(did[1][1])
