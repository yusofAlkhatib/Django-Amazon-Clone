from rest_framework.pagination import PageNumberPagination

class CunstomPagination(PageNumberPagination):
    page_size = 20