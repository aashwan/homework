

set -ex



python -c "import ctypes; assert 11100 == ctypes.cdll[r'libtbb.so.2']       ['TBB_runtime_interface_version']()"
exit 0
