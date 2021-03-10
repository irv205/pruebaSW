from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.utils.urls import replace_query_param
from rest_framework.views import Response


class PageNumberPagination(PageNumberPagination):

    page_size_query_param = 'per_page'

    def build_link(self, index):
        if not index:
            return None
        url = self.request and self.request.build_absolute_uri() or ''
        return replace_query_param(url, self.page_query_param, index)

    def get_paginated_response(self, data):
        next = None
        previous = None

        if self.page.has_next():
            next = self.page.next_page_number()
        if self.page.has_previous():
            previous = self.page.previous_page_number()

        if next is None:
            next = ''
        else:
            next = self.build_link(next)

        if previous is None:
            prev = ''
        else:
            prev = self.build_link(previous)

        return Response({
            'data': data,
            'pages': {
                'total_items': self.page.paginator.count,
                'items_per_page': self.get_page_size(self.request),
                'current_page': self.page.number,
                'urls': OrderedDict([
                    ('next', next),
                    ('prev', prev)
                ])
            }
        })