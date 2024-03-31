import clang.cindex

# Create an index
index = clang.cindex.Index.create()

# Parse the file
tu = index.parse(file_path)

# Print the translation unit
print(tu)
