from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    BaseDocTemplate, 
    PageTemplate, 
    Frame, 
    Table, 
    TableStyle,
    Image, 
    Paragraph, 
    PageBreak
)
from reportlab.lib.colors import Color 
from reportlab.platypus.flowables import Spacer
from reportlab.lib.styles import getSampleStyleSheet


def header(canvas, doc):
    """Draws the header on each page with a title, left-aligned text, and logos on both sides."""
    canvas.saveState()
    canvas.setFont("Helvetica", 10)

    # Centered header title
    header_text = "FarmSetu Technologies"
    text_width = canvas.stringWidth(header_text, "Helvetica", 10)
    
    # Draws centered text 0.7 cm below the top edge of the A4 page.
    canvas.drawString((A4[0] - text_width) / 2, A4[1] - 0.7 * cm, header_text)

    # Left-aligned logo
    logo_path = "C:\\Users\\mypc\\Downloads\\Farmsetu-Logo-full.png"
    logo = Image(logo_path, width=4 * cm, height=1.5 * cm)
    
    # Draws the logo image 1.6 cm below the top edge and 1 cm from the left edge of the A4 page.
    logo.drawOn(canvas, 1 * cm, A4[1] - 1.6 * cm)

    # Right-aligned logo
    logo_path = "C:\\Users\\mypc\\Downloads\\Farmsetu.webp" 
    logo = Image(logo_path, width=1.3 * cm, height=1.3 * cm)
    
    # Draws the logo image 1.4 cm below the top edge and 1.7 cm from the right edge of the A4 page.
    logo.drawOn(canvas, A4[0] - 1.7 * cm, A4[1] - 1.4 * cm)

    canvas.restoreState()


def footer(canvas, doc):
    """Draws the footer on each page with a title, left-aligned text, and the page number."""
    canvas.saveState()
    canvas.setFont("Helvetica", 10)

    # Centered footer text
    footer_text = "FarmSetu"
    footer_width = canvas.stringWidth(footer_text, "Helvetica", 10)

    # Draws the footer text centered at the bottom of the page, 0.7 cm above the bottom edge.
    canvas.drawString((A4[0] - footer_width) / 2, 0.7 * cm, footer_text)

    # Left-aligned footer text
    left_footer_text = "TSP"

    # Draws the left footer text ("TSP") 0.7 cm above the bottom-left corner of the page.
    canvas.drawString(1 * cm, 0.7 * cm, left_footer_text)

    # Right-aligned page number
    page_number = f"{doc.page}"

    # Draws the page number ("page_number") 0.7 cm above the bottom-right corner of the page.
    canvas.drawString(A4[0] - 1 * cm, 0.7 * cm, page_number)
    canvas.restoreState()


def watermark(canvas, doc):
    """
    Adds a visually appealing watermark to each page.
    """
    canvas.saveState()  # Save the current canvas state
    canvas.setFont("Helvetica-Bold", 25)  # Set font and size
    canvas.setFillColor(Color(0.5, 0.5, 0.5, alpha=0.3))  # Set semi-transparent gray color
    watermark_text = "FARMSETU" 
    
    # Define spacing between watermarks
    h_space = 200
    v_space = 150

    # Calculate offsets to center the grid 
    x_offset = (A4[0] % h_space) / 2 
    y_offset = (A4[1] % v_space) / 2 

    # Loop through vertical positions 
    for y in range(-v_space, int(A4[1]) + v_space, v_space): 
        # Loop through horizontal positions
        for x in range(-h_space, int(A4[0]) + h_space, h_space):
            canvas.saveState()  # Save state for individual watermark
            canvas.translate(x + x_offset, y + y_offset)  # Translate to current grid position
            canvas.rotate(45)  # Rotate for diagonal effect
            canvas.drawCentredString(0, 0, watermark_text)  # Draw centered watermark
            canvas.restoreState()  # Restore canvas to previous state

    canvas.restoreState()  # Restore initial canvas state

    
def add_page_decorations(canvas, doc):
    """Adds the header and footer to each page."""
    header(canvas, doc)
    footer(canvas, doc)
    watermark(canvas, doc)


def Smart_Path_Delivery_report_pdf(
    first_paragraph, data, images_data, second_paragraph
):
    """
    Generates a PDF report for the Smart Path Delivery system with text, tables, images, and page decorations.
    """
    
    # Setting up the document with custom margins
    doc = BaseDocTemplate(
        "Smart_Path_Delivery_Report.pdf",
        pagesize=A4,
    )
    
    """
    Creates a content frame with 2 cm left/right margins, 2 cm top margin, 
    and 2 cm bottom margin, to fit within the A4 page dimensions.
    """
    left_margin = 2 * cm
    top_margin = 2 * cm
    right_margin = 2 * cm
    bottom_margin = 2 * cm

    # Calculate usable width and height based on the A4 dimensions
    usable_width = A4[0] - left_margin - right_margin
    usable_height = A4[1] - top_margin - bottom_margin

    # Create the frame
    frame = Frame(left_margin, bottom_margin, usable_width, usable_height, showBoundary=5)
    
    # Adding the page template
    template = PageTemplate(id="report_template", frames=frame, onPage=add_page_decorations)
    doc.addPageTemplates([template])

    # Style setup for paragraphs
    styles = getSampleStyleSheet()

    paragraph_style = styles['Normal']
    paragraph_style.firstLineIndent = 40  # Indent the first line
    paragraph_style.leftIndent = 10       # Indent the entire paragraph
    paragraph_style.fontSize = 8         # Set font size

    # Main introductory paragraph
    paragraph1 = Paragraph(
        first_paragraph,
        paragraph_style
    )

    table_data = data #data for table  

    # Define the usable width for the table (in centimeters)
    usable_width = 17 * cm
    
    """
    Calculate the maximum length for each column by finding the longest string length in each column,
    This helps to determine how much space each column should occupy in the final layout.
    """
    max_lengths = [max(len(str(row[col])) for row in table_data) for col in range(len(table_data[0]))]
    
    """
    Sum up all the maximum lengths across columns to calculate the total length required for all columns,
    This helps in determining how to proportionally allocate the space (usable width) to each column.
    """
    total_length = sum(max_lengths)
    
    """
    Calculate the relative width of each column by using a proportional distribution of the usable width,
    Each column gets a portion of the usable width based on the relative length of the content in that column.
    """    
    col_widths = [(usable_width * (length / total_length)) for length in max_lengths]
    
    # Creating the table with styling
    table = Table(table_data, colWidths=col_widths)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Font for entire table
        ('FONTSIZE', (0, 0), (-1, -1), 8),  # Font size
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center alignm=ent
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Gridlines
        ('WORDWRAP', (0, 0), (-1, -1), 'CJK'),  # Enable word wrapping for all cells
    ])
    table.setStyle(style)

    # Images for visualization
    images = []

    # Loop through the dictionary and create Image objects for each file path
    for image_key, image_path in images_data.items():
        images.append(Image(image_path, width=6*cm, height=4*cm))

    # Arranging images in a table
    image_data = [
        [images[0], images[1]],
        [images[2], images[3]],
    ]  
    image_table = Table(image_data, colWidths=9 * cm, rowHeights=6 * cm)

    # Final paragraph
    paragraph2 = Paragraph(
        second_paragraph,
        paragraph_style
    )

    # Adding elements to the document
    elements = [
        paragraph1,
        Spacer(1, 15 * cm),
        table,
        Spacer(1, 0.5 * cm),
        PageBreak(),
        image_table,
        PageBreak(),
        paragraph2
    ]

    # Building the document
    doc.build(elements)

if __name__ == '__main__':
    Smart_Path_Delivery_report_pdf()
