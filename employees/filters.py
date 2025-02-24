import django_filters # type: ignore
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='From EMP ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label = 'To EMP ID')

    class Meta:
        model = Employee
        fields = ['designation', 'emp_name', 'id_min', 'id_max']

    def filter_by_id_range(self, queryset, name, value):  # Fixed typo 'vlaue' -> 'value'
        if name == 'id_min':
            return queryset.filter(id__gte=value)  # Fixed 'emp_id_gte' -> 'id__gte'
        elif name == 'id_max':
            return queryset.filter(id__lte=value)  # Fixed 'emp_id_lte' -> 'id__lte'
        return queryset

