from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnlyAndNotOwner, IsSupporterOrReadOnly
from django.http import Http404
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PledgeDetailSerializer
from rest_framework.views import exception_handler


class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        print(request.GET)
        
        order = request.GET.get('order', None)
        print("order", order)
        projects = Project.objects.all()
        
        if order is not None:
            projects =projects.order_by('-' + order)
        
        most_pledges = request.GET.get('most_pledges', None)
        if most_pledges is not None:
            projects = sorted(list(projects), key=lambda project: project.pledge_sum, reverse=True)
        
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response (
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response (
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    
    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        project = self.get_object(pk)
        print(project)
        print(project.pledge_sum)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status.HTTP_204_NO_CONTENT)   

class PledgeList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSupporterOrReadOnlyAndNotOwner
    ]   

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        project_id = request.data.get('project')
        print('id', project_id)
        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            return Response({'error': 'The project does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        if not project.is_open:
            return Response({'error': 'This project is not accepting pledges'}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response (
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSupporterOrReadOnly
    ]
    
    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer =  PledgeDetailSerializer(pledge)
        return Response(serializer.data)
    
    def put(self, request, pk):
        pledge = self.get_object(pk)
        serializer =  PledgeDetailSerializer(
            instance = pledge,
            data = request.data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status = status.HTTP_404_NOT_FOUND
        )
    
    def delete(self, request, pk):
        pledge = self.get_object(pk)
        pledge.delete()
        return Response(status.HTTP_204_NO_CONTENT)


