import os
from fpdf import FPDF
from typing import List


def write_array_to_pdf(file_path: str, numbers_array: List[float]) -> None:
    """
    Write an array of numbers to a PDF file with A4 paper size.

    Parameters:
    - file_path (str): The path to the PDF file.
    - numbers_array (List[float]): The array of numbers to be written to the PDF.

    Returns:
    - None
    """
    pdf = FPDF(format='A4')
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Write each number to the PDF
    for number in numbers_array:
        pdf.cell(0, 10, str(number), ln=True)

    # Create the directory if it doesn't exist
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"'{directory}' has been created.")

    # Output PDF to the specified file
    pdf.output(file_path)

    print(f"Array successfully written to PDF file: {file_path}")
