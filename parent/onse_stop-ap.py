import subprocess
import time


subprocess.run(["python3", "/root/ise-landscape/allowed-protocol-api/finalized-ap-post.py"])

subprocess.run(["python3", "/root/ise-landscape/allowed-protocol-api/finalized-ap-put.py"])

subprocess.run(["python3", "//root/ise-landscape/parent/cleanup-ap.py"])
