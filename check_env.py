import sys
import os

print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("Sys path:")
for path in sys.path:
    print("  ", path)

print("Environment variables:")
for key, value in os.environ.items():
    print(f"  {key}: {value}")
