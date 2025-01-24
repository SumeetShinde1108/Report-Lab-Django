from django.shortcuts import render
from django.http import HttpResponse
from reportlab.platypus import Image
from sample_app.utils import (
    Smart_Path_Delivery_report_pdf,
    header, 
    footer, 
    watermark
)
from reportlab.lib.units import cm

def generate_pdf_view(request):
    """
    This function passes the data to function which generates the pdf by using this data dynamically
    """

    table_data = [
        ["Name", "Sumeet", "Pratik", "Vikas", "Om"],
        ["Age", "21", "23", "23", "24"],
        [
            "Image", 
            Image(r"C:\Users\mypc\Downloads\Image5.jpg", width=2*cm, height=2*cm),
            Image(r"C:\Users\mypc\Downloads\Image6.jpg", width=2*cm, height=2*cm),
            Image(r"C:\Users\mypc\Downloads\Image7.jpg", width=2*cm, height=2*cm),
            Image(r"C:\Users\mypc\Downloads\Image8.jpg", width=2*cm, height=2*cm)
        ],
    ]


    images_data = {
        "image1" : r"C:\Users\mypc\Downloads\Image1.jpg",
        "image2" : r"C:\Users\mypc\Downloads\Image2.jpg",
        "image3" : r"C:\Users\mypc\Downloads\Image3.jpg",
        "image4" : r"C:\Users\mypc\Downloads\Image4.jpg",
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

    