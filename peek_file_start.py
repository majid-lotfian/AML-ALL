file_path = r"I:\AML_ALL\Data\BC_labuitslag_13-04-2026.csv"

with open(file_path, "rb") as f:
    first_bytes = f.read(500)

print(first_bytes)
