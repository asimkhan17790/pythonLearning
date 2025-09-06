# # pip install PyPDF2
# from PyPDF2 import PdfWriter

# merger = PdfWriter()

# for pdf in ["file1.pdf", "file2.pdf"]:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()


# pip install PyPDF2

from PyPDF2 import PdfWriter, PdfReader


def merge_pdfs():
    merger = PdfWriter()

    for pdf_file in ["file3.pdf", "file1.pdf", "file2.pdf", "file3.pdf"]:
        reader = PdfReader(pdf_file)
        if reader.is_encrypted:
            # Decrypt with password '9944' (change if needed)
            try:
                reader.decrypt("9944")
            except Exception as e:
                print(f"Failed to decrypt {pdf_file}: {e}")
                continue
        merger.append(reader)

    with open("merged-pdf.pdf", "wb") as f:
        merger.write(f)
        print("Files merged successfully..")


if __name__ == "__main__":
    merge_pdfs()
