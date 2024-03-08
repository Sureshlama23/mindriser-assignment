from rest_framework.pagination import PageNumberPagination


class ListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'records'