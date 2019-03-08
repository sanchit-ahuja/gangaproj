import sys
import os
docker=str(sys.argv[1])
open('docker.sh', 'w').write("""#!/bin/bash
docker run %s
"""%docker)
os.system('chmod +x docker.sh')
j = Job()
j.application.exe = File('docker.sh')
j.submit()