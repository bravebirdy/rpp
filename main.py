import PyPDF2


def remove_pdf_password(input_pdf, output_pdf, password):
    # Open the input PDF file
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Check if the PDF is encrypted
        if reader.is_encrypted:
            # Try to decrypt the PDF with the provided password
            try:
                reader.decrypt(password)
            except Exception as e:
                print(f"Failed to decrypt PDF: {e}")
                return

        # Create a writer object to write the decrypted PDF
        writer = PyPDF2.PdfWriter()

        # Add all pages to the writer
        for page in range(len(reader.pages)):
            writer.add_page(reader.pages[page])

        # Write the decrypted PDF to the output file
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)


if __name__ == "__main__":
    # Example usage
    remove_pdf_password(
        'pdf-with-password.pdf', 'pdf-without-password.pdf', 'my_password'
    )
