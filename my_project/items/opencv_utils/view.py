# opencv_utils/view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from items.opencv_utils.image_processing import convert_to_grayscale
from django.http import FileResponse
import os

class ImageProcessingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        input_image_path = request.data.get('input_image_path')
        output_image_path = request.data.get('output_image_path')

        try:
            # Convert image to grayscale
            convert_to_grayscale(input_image_path, output_image_path)
            
            # Open the file to return it as a response
            image_file = open(output_image_path, 'rb')
            
            # Return the grayscale image as a downloadable file
            response = FileResponse(image_file, as_attachment=True, filename=os.path.basename(output_image_path))
            return response

        except FileNotFoundError as e:
            return Response({"error": str(e)}, status=400)
