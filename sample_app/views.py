from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from sample_app.utils import (
    Smart_Path_Delivery_report_pdf,
    header, 
    footer, 
    watermark
)

def generate_pdf_view(request):
    """
    This function passes the data to function which generates the pdf by using this data dynamically
    """

    table_data = [
        ["Vehicle No", "Capacity", "Vehicle Path", "Carrying Weight", "Remaining Weight", "Total Route Distance"],
        ["VH008", "1000", "ORD010 → ORD015 → ORD024 → ORD008", "999", "1", "646.24 km"],
        ["VH005", "400", "ORD003", "400", "0", "84.06 km"],
        ["VH006", "500", "ORD015 → ORD014 → ORD025", "420", "80", "210.16 km"],
        ["VH004", "600", "ORD001", "600", "0", "142.38 km"],
        ["VH001", "800", "ORD012 → ORD021 → ORD019", "800", "0", "801.60 km"],
        ["VH003", "1000", "ORD009 → ORD016 →ORD005", "990", "10", "323.75 km"],
        ["VH002", "1200", "ORD004 → ORD013 → ORD027", "1160", "40", "648.08 km"],
        ["VH007", "800", "ORD011 → ORD007", "760", "40", "114.04 km"]
    ]
    
    images_data = {
        "image1" : "C:\\Users\\mypc\\Pictures\\Screenshots\\Screenshot 2025-01-17 104955.png",
        "image2" : "C:\\Users\\mypc\\Pictures\\Screenshots\\Screenshot 2025-01-17 004504.png",
        "image3" : "C:\\Users\\mypc\\Pictures\\Screenshots\\Screenshot 2025-01-16 170815.png",
        "image4" : "C:\\Users\\mypc\\Pictures\\Screenshots\\Screenshot 2025-01-16 170718.png",
    }

    first_paragraph = (
        "This is a report on the smart path delivery system. "
        "This system, likely employing a sophisticated route optimization algorithm, aims to streamline the delivery process by identifying "
        "the most efficient path for a vehicle or courier to traverse multiple destinations. It considers various factors such as distance, "
        "traffic conditions, delivery time windows, and any specific constraints or requirements. By calculating the shortest possible route, "
        "the system minimizes travel time and fuel consumption, leading to significant cost savings and improved operational efficiency. "
        "Moreover, ensuring all destinations are visited guarantees that no deliveries are missed, while the return to the starting point "
        "optimizes the overall journey and allows for efficient resource allocation and scheduling. This type of system is particularly valuable "
        "for businesses with large delivery fleets or those operating in complex urban environments where efficient route planning is crucial "
        "for success. Key aspects highlighted in the paragraph: Route Optimization: The core function of the system is to determine the most efficient path. "
        "Multi-location Delivery: The system caters to scenarios involving multiple delivery points. Shortest Path: The primary objective is to minimize the total distance or travel time. "
        "Delivery Requirements: The system accounts for specific constraints like time windows, delivery priorities, and any special instructions. "
        "Complete Coverage: Ensures all destinations are visited, preventing missed deliveries. Return to Origin: Optimizes the overall journey by returning to the starting point. "
        "Benefits: Cost savings, improved efficiency, optimized resource allocation. Applications: Valuable for businesses with large delivery fleets or those operating in complex environments. "
        "This system has the potential to revolutionize logistics and delivery operations by significantly enhancing efficiency and reducing costs."
        )

    second_paragraph = ("Hi My name is Sumeet Shinde, Welcome to Smart_Path_Delivery Report")
    

    header_data = {
        "header_text" : "FarmSetu Technologies",
        "left_logo" : "C:\\Users\\mypc\\Downloads\\Farmsetu-Logo-full.png",
        "right_logo" : "C:\\Users\\mypc\\Downloads\\Farmsetu.webp"
    }
    
    footer_data = {
        "center_footer_text": " FarmSetu",
        "Left_footer_text": "SPDS"
    }

    watermark_data = {
        "watermark_text": "FARMSETU"
    }

    Smart_Path_Delivery_report_pdf(header_data, footer_data, watermark_data, first_paragraph, table_data, images_data, second_paragraph)

    return HttpResponse("PDF Generated")

