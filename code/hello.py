import os

message = os.environ["MESSAGE"]

print("My message is:")
print(message)

output_file = "/data/hello.txt"
with open(output_file, 'r') as f:
    f.write(message)
