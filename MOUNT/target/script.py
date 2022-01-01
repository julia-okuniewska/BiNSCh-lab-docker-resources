import os
import platform

message = f"This message was generated in {os.getcwd()} by process {os.getpid()}\n\
Platform: {os.name}; {platform.system()}; {platform.release()}\n"
with open('Generated_file.txt', 'a') as f:
    f.write(message)

print(message)
