from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Deployment

@api_view(['POST'])
def deploy_project(request):

    repo_url = request.data.get('repo_url')

    deployment = Deployment.objects.create(
        repo_url=repo_url
    )

    return Response({
        "message": "Deployment Started",
        "repo": repo_url,
        "status": deployment.status
    })