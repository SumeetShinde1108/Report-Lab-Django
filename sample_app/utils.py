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


def header(canvas, doc, header_text, left_logo, right_logo):
    """Draws the header dynamically with passed data."""
    canvas.saveState()
    canvas.setFont("Helvetica", 10)

    # Centered header text
    text_width = canvas.stringWidth(header_text, "Helvetica", 10)
    # Draws centered text 0.7 cm below the top edge of the A4 page.    
    canvas.drawString((A4[0] - text_width) / 2, A4[1] - 0.7 * cm, header_text)

    # Left-aligned logo
    left_logo_img = Image(left_logo, width=4 * cm, height=1.5 * cm)
    # Draws the logo image 1.6 cm below the top edge and 0.8 cm from the left edge of the A4 page.
    left_logo_img.drawOn(canvas, 0.8 * cm, A4[1] - 1.6 * cm)

    # Right-aligned logo
    right_logo_img = Image(right_logo, width=1.3 * cm, height=1.3 * cm)
    
    # Draws the logo image 1.6 cm below the top edge and 2.5 cm from the right edge of the A4 page.
    right_logo_img.drawOn(canvas, A4[0] - 2.5 * cm, A4[1] - 1.6 * cm)

    canvas.restoreState()


def footer(canvas, doc, footer_text, left_footer_text):
    """Draws the footer dynamically with passed data."""
    canvas.saveState()
    canvas.setFont("Helvetica", 10)

    # Centered footer text
    text_width = canvas.stringWidth(footer_text, "Helvetica", 10)
    
    # Draws the footer text centered at the bottom of the page, 0.7 cm above the bottom edge.
    canvas.drawString((A4[0] - text_width) / 2, 0.7 * cm, footer_text)

    # Left-aligned footer text
    # Draws the left footer text ("TSP") 0.7 cm above the bottom-left corner of the page.
    canvas.drawString(1 * cm, 0.7 * cm, left_footer_text)

    # Right-aligned page number
    page_number = f"Page {doc.page}"

    # Draws the page number ("page_number") 0.7 cm above the bottom-right corner of the page.
    canvas.drawString(A4[0] - 2 * cm, 0.7 * cm, page_number)

    canvas.restoreState()


def watermark(canvas, doc, watermark_text):
    """Adds a dynamic watermark."""
    canvas.saveState()  # Save the current canvas state
    canvas.setFont("Helvetica-Bold", 25) # Set font and size
    canvas.setFillColor(Color(0.5, 0.5, 0.5, alpha=0.2)) # Set semi-transparent gray color

    # Spacing and offset for repeating watermark
    h_space = 200
    v_space = 150
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

    canvas.restoreState() # Restore initial canvas state


def Smart_Path_Delivery_report_pdf(
    header_data, footer_data, watermark_data, first_paragraph, table_data, images_data, second_paragraph
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
    

    def add_page_decorations(canvas, doc):
        """Adds the header and footer to each page."""
        # Extract header data
        header_text = header_data.get("header_text", "")
        left_logo = header_data.get("left_logo", "")
        right_logo = header_data.get("right_logo", "")

        # Add header
        header(canvas, doc, header_text, left_logo, right_logo)

        # Extract footer data
        footer_text = footer_data.get("center_footer_text", "")
        left_footer_text = footer_data.get("Left_footer_text", "")

        # Add footer
        footer(canvas, doc, footer_text, left_footer_text)

        # Add watermark
        watermark_text = watermark_data.get("watermark_text", "")
        watermark(canvas, doc, watermark_text)

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

    styles = getSampleStyleSheet()


    # Paragraph style
    styles = getSampleStyleSheet()
    paragraph_style = styles['Normal']
    paragraph_style.firstLineIndent = 0  # No excessive indent
    paragraph_style.leftIndent = 0       # No left indent
    paragraph_style.fontSize = 8         # Font size for better readability
    paragraph_style.wordWrap = 'LTR'     # Word wrapping
    paragraph_style.alignment = 0        # Left alignment

    # Process the table data
    processed_data = []
    
    for row in table_data:
        processed_row = []
    
        for cell in row:
            if isinstance(cell, Image):
                cell.drawWidth = 1.5* cm  # Limit image width
                cell.drawHeight = 1.5 * cm  # Limit image height
                processed_row.append(cell)
            else:
                # Wrap text inside the cell
                para = Paragraph(str(cell), paragraph_style)
                processed_row.append(para)
        processed_data.append(processed_row)

    # Define the usable width for the table (A4 width minus margins)
    usable_width = A4[0] - (2 * cm + 2 * cm)  # Left and right margins

    """
    Calculate the maximum length for each column by finding the longest string length in each column,
    This helps to determine how much space each column should occupy in the final layout.
    """
    max_lengths = [max(len(str(row[col])) for row in processed_data) for col in range(len(processed_data[0]))]


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

    # Create the table with proportional column widths
    table = Table(processed_data, colWidths=col_widths)

    # Table styling
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Font for entire table
        ('FONTSIZE', (0, 0), (-1, -1), 8),  # Font size
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center alignment
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical alignment
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Gridlines
        ('WORDWRAP', (0, 0), (-1, -1), 'CJK'),  # Enable word wrapping for all cells    
    ])
    table.setStyle(style)
    
    # Images for visualization
    images = []

    # Loop through the dictionary and create Image objects for each file path
    for image_key, image_path in images_data.items():
        images.append(Image(image_path, width=4*cm, height=4*cm))

    # Arranging images in a table
    image_data = [
        [images[0], images[1]],
        [images[2], images[3]],
    ]  
    image_table = Table(image_data, colWidths=5 * cm, rowHeights=5 * cm)

    # Final paragraph
    paragraph2 = Paragraph(
        second_paragraph,
        paragraph_style
    )

    # Adding elements to the document
    elements = [
        paragraph1,
        Spacer(1, 2 * cm),
        table,
        Spacer(1, 0.5 * cm),
        PageBreak(),
        image_table,
        PageBreak(),
        Spacer(1, 15 * cm),
        paragraph2
    ]

    # Building the document
    doc.build(elements)


if __name__ == '__main__':
    Smart_Path_Delivery_report_pdf()