import os

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from django.core.files.storage import FileSystemStorage
from django.http import FileResponse


# Create your views here.
class UploadViewSet(ViewSet):  

    def list(self, request):
        filename = request.GET.get('filename')
        response = FileResponse(open(r'./DocumentStore/' + filename, 'rb'))

        return response

    def create(self, request):
        response = 'it is good'
        response_dicts=[]

        fs = FileSystemStorage()
        if(os.path.exists('./DocumentStore/') != True):
                os.mkdir('./DocumentStore')

        for i in range(0, len(request.data), 1):
            file_dict = {}
            file_uploaded = request.data.get('FILES_' + str(i))
            print('the file upload type is:', (file_uploaded))
            content_type = file_uploaded.content_type
            print('the content type is:', type(content_type))
            file_dict['name'] = file_uploaded.name
            file_dict['type'] = content_type
            response_dicts.append(file_dict)

            if (file_uploaded.name in os.listdir('./DocumentStore/') ):
                os.remove('./DocumentStore/' + file_uploaded.name)

            fs = FileSystemStorage('./DocumentStore/')
            print(file_uploaded)
            filename = fs.save(file_uploaded.name, file_uploaded)
            uploaded_file_url = fs.url(filename)
            print('the url is:', uploaded_file_url)

            # with open(r'Path of the SharePoint synced Folder' + file_uploaded.name, 'wb + ') as destination:
            #     for chunk in file_uploaded.chunks():
            #         destination.write(chunk)
            #     print('pushed', 'pushed')

        response = response_dicts
        return Response(response)

    def delete(self, request):
        print('the delete query params are:', request.GET.get('filename'))
        filename = request.GET.get('filename')
        os.remove('./DocumentStore/' + filename)
        # os.remove(r'Path of the SharePoint synced Folder' + filename)
        response = 'The {} file deleted successfully'.format(filename)

        return Response(response)
