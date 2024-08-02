import azure.functions as func
import logging
import pdfkit
import tempfile

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="dpcpdfmerger")
def dpcpdfmerger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON body.",
            status_code=400
        )

    html_content = req_body.get('html')
    if not html_content:
        return func.HttpResponse(
            "Please provide HTML content in the request body.",
            status_code=400
        )

    try:
        # Create a temporary file to store the PDF
        import azure.functions as func
        import logging
        import pdfkit
        import tempfile
        import os
        
        app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
        
        # Path to the wkhtmltopdf binary
        WKHTMLTOPDF_PATH = os.path.join(os.getcwd(), 'wkhtmltopdf', 'wkhtmltopdf')
        
        @app.route(route="dpcpdfmerger")
        def dpcpdfmerger(req: func.HttpRequest) -> func.HttpResponse:
            logging.info('Python HTTP trigger function processed a request.')
        
            try:
                req_body = req.get_json()
            except ValueError:
                return func.HttpResponse(
                    "Invalid JSON body.",
                    status_code=400
                )
        
            html_content = req_body.get('html')
            if not html_content:
                return func.HttpResponse(
                    "Please provide HTML content in the request body.",
                    status_code=400
                )
        
            try:
                # Configure pdfkit to use the local wkhtmltopdf binary
                config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
        
                # Create a temporary file to store the PDF
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                    pdfkit.from_string(html_content, temp_pdf.name, configuration=config)
                    temp_pdf.seek(0)
                    pdf_data = temp_pdf.read()
        
                return func.HttpResponse(
                    pdf_data,
                    mimetype='application/pdf',
                    headers={
                        'Content-Disposition': 'attachment; filename="output.pdf"'
                    }
                )
            except Exception as e:
                logging.error(f"Error converting HTML to PDF: {e}")
                return func.HttpResponse(
                    "An error occurred while converting HTML to PDF.",
                    status_code=500
                )ith tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            pdfkit.from_string(html_content, temp_pdf.name)
            temp_pdf.seek(0)
            pdf_data = temp_pdf.read()

        return func.HttpResponse(
            pdf_data,
            mimetype='application/pdf',
            headers={
                'Content-Disposition': 'attachment; filename="output.pdf"'
            }
        )
    except Exception as e:
        logging.error(f"Error converting HTML to PDF: {e}")
        return func.HttpResponse(
            "An error occurred while converting HTML to PDF.",
            status_code=500
        )