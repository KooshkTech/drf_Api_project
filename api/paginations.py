from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'  # Allows users to specify page size
    page_query_param = 'page_num'  # Changes "page" to "page_num"
    max_page_size = 10  # Prevents excessive page size requests

    def get_paginated_response(self, data):  # Fixed method name (removed `_`)
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_size': self.get_page_size,  # Correct way to get page_size
            'results': data
        })
