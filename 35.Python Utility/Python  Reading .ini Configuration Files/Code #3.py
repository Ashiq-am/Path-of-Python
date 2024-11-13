configur.set('server','port','9000')
configur.set('debug','log_errors','False')

import sys
configur.write(sys.stdout)
