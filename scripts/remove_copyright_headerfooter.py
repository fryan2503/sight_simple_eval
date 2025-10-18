import fitz  # PyMuPDF

######################################################################
# (1) Shorten the PDF
######################################################################

# Input and output filenames
input_file = "../../gov_pdfs/UR5e_Universal_Robots User Manual.pdf"
output_file = "ur5_shortened_manual.pdf"


# Define 1-based page ranges (based on PDF Viewer)
page_ranges = [
    (12, 23),
    (28, 36),
    (39, 39),
    (50, 51),
    (55, 71),
    (84, 95),
    (98, 132),
    (181, 188),
    (192, 204)
]

# Open the source PDF
src = fitz.open(input_file)

# Create a new empty PDF
dst = fitz.open()

# Copy selected pages
for start, end in page_ranges:
    for page_num in range(start - 1, end):  # convert to 0-based
        dst.insert_pdf(src, from_page=page_num, to_page=page_num)

# Save the result
dst.save(output_file)
dst.close()
src.close()

print(f"Created {output_file} successfully!")

######################################################################
# (2) Crop the copyrights from the manual
######################################################################

# Inputs
input_file = "ur5_shortened_manual.pdf"
output_file = "ur5_shortened_cropped.pdf"

# Fraction of page to remove from each side (e.g., 0.06 = 6%)
crop_percent = 0.075

doc = fitz.open(input_file)

for page in doc:
    rect = page.rect
    width = rect.width
    height = rect.height

    # Compute margins to trim
    lm = width * crop_percent
    rm = width * crop_percent
    tm = height * crop_percent
    bm = height * crop_percent

    # Create cropped rectangle
    new_rect = fitz.Rect(
        rect.x0 + lm,
        rect.y0 + tm,
        rect.x1 - rm,
        rect.y1 - bm
    )

    # Apply crop
    page.set_cropbox(new_rect)

# Save cropped PDF (compressed and cleaned)
doc.save(output_file, deflate=True, garbage=4)
doc.close()

print(f"Cropped file written to {output_file}")
