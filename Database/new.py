import os
import docling
from docling.document_converter import DocumentConverter

# Path to the PDF file
source = "/home/rrr/ardi/IEEE_Conference_Template/Database/kecamatan-jasinga-dalam-angka-2024.pdf"

# Convert the PDF to a document object
converter = DocumentConverter()
result = converter.convert(source)

# Export the document to markdown format
markdown_content = result.document.export_to_markdown()

# Get the same filename but with .txt extension
base_name = os.path.splitext(os.path.basename(source))[0]
output_path = os.path.join(os.path.dirname(source), f"{base_name}.txt")

# Save to .txt file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(markdown_content)

print(f"Saved markdown content to {output_path}")
