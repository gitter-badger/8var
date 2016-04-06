inp=raw_input("Drag and drop a file or enter /path/to/file.md++ here.")
out=raw_input("enter the desired name of output or /path/to/output.html here.")
input=open(inp, "r").read()
open(out, "w").write(input)
