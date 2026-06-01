#!/usr/bin/env python3
"""
Admin Check - Verify administrator privileges
"""

import os
import ctypes
import sys

def check_admin():
    """Check if script is running with administrator privileges"""
    try:
        return ctypes.windll.shell.IsUserAnAdmin()
    except:
        return False

def get_admin_privileges():
    """Attempt to get administrator privileges"""
    if not check_admin():
        ctypes.windll.shell.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
