import os

message = os.environ["MESSAGE"]

print("My message is:")
print(message)

output_file = "/results/hello.txt"
with open(output_file, 'w') as f:
    f.write(message)
