# Platform-specific code to send interrupts to an APL instance 

import WinDyalog
import os, platform, signal  

def interrupt(pid):
    if os.name=='nt' and not 'CYGWIN' in platform.system():
        # standard Windows, use the Windows API
        WinDyalog.interrupt(pid)
    elif os.name=='posix' and not 'CYGWIN' in platform.system():
		# standard Unix, send SIGINT 
		os.kill(pid, signal.SIGINT)
    elif 'CYGWIN' in platform.system():
        # TODO: Cygwin support
        raise NotImplementedError()

    else:
        raise RuntimeError("OS not supported")
		