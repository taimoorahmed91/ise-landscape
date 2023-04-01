import subprocess
import time


# Run the other script
subprocess.run(["python3", "/root/ise-landscape/authz/inset_dacl.py"])


#time.sleep(3)
subprocess.run(["python3", "/root/ise-landscape/dacl-api/finalized-dacl-post.py"])





subprocess.run(["python3", "/root/ise-landscape/dacl-api/finalized-dacl-put.py"])

subprocess.run(["python3", "/root/ise-landscape/authz/post_authz.py"])

subprocess.run(["python3", "/root/ise-landscape/parent/cleanup.py"])


print("hello")





