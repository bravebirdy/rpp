import PyPDF2
import argparse  # Import argparse for command-line argument parsing


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
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description='Remove password from a PDF file.')
    parser.add_argument('input_pdf', type=str,
                        help='Path to the input PDF file')
    parser.add_argument('output_pdf', type=str,
                        help='Path to the output PDF file')
    parser.add_argument('password', type=str,
                        help='Password for the input PDF file')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function with the provided arguments
    remove_pdf_password(args.input_pdf, args.output_pdf, args.password)
