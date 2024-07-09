import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UploadFileForm
from .input_df import myFunc
from urllib.parse import quote, unquote
import os

# function use to save the uploaded file to the specified directory and return the file path
def handle_uploaded_file(f):
    try:
        file_path = os.path.join('media/upload/', f.name)
        with open(file_path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return file_path
    except Exception as e:
        raise IOError(f"Error saving file: {str(e)}")

# Function use to save the file and redirect to 'transform' view or display error messages
def upload_file(request):
    error_message = None
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                file_path = handle_uploaded_file(request.FILES['file'])
                print("Uploaded file path:", file_path)
                return redirect(reverse('transform', kwargs={'file_name': quote(os.path.basename(file_path))}))
            except Exception as e:
                error_message = f"File upload error: {str(e)}"
        else:
            error_message = "Form is not valid."
    else:
        form = UploadFileForm()
    return render(request, 'transform/upload.html', {'form': form, 'error_message': error_message})

# Function use to transform the input file into the desired output file
def transform(request, file_name):
    error_message = None
    path = ""

    file_path = os.path.join('media/upload', unquote(file_name))
    try:
        print("Check input file path:", file_path)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input file not found at path: {file_path}")

        path = myFunc(file_path)
        print("Generated output file path:", path)

        if not os.path.exists(path):
            raise FileNotFoundError(f"Output file not found at path: {path}")

        # Plot the graph from the output file
        output_df = pd.read_excel(path)
        plt.figure(figsize=(9, 4))  # Increase the width for better label visibility
        output_df.groupby('Product')['Value'].sum().plot(kind='bar')
        plt.title('Total Value by Product')
        plt.xlabel('Product')
        plt.ylabel('Value')
        plt.xticks(rotation=45, ha='right')  # Rotate x labels for better visibility
        plt.tight_layout() 
        plt.subplots_adjust(bottom=0.3)

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()

    except FileNotFoundError as e:
        error_message = f"File not found: {str(e)}"
    except Exception as e:
        error_message = f"Error during transformation: {str(e)}"

    return render(request, 'transform/result.html', {'path': path, 'error_message': error_message, 'plot': image_base64})