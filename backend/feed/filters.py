import django_filters
from django.db.models import Q, Count
from .models import Post

SORT_CHOICES = (
    ('recent', 'Most Recent'),
    ('popular', 'Most Popular'),
)


class SandwichFilter(django_filters.FilterSet):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['veggies'].field.widget.attrs.update({'class': 'multi-limit'})
        self.filters['sauces'].field.widget.attrs.update({'class': 'multi-limit'})

    # VEGAN
    vegan = django_filters.ChoiceFilter(
        choices=[('Vegan', 'Vegan')],  # Override Non Vegan option
        label='Vegan',
        empty_label='--------'
    )

    # PRICE
    price__gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte', label='Min Price'
    )
    price__lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte', label='Max Price'
    )

    # VEGGIES + SAUCES
    veggies = django_filters.MultipleChoiceFilter(
        label="Veggies",
        choices=Post.VEGGIE_CHOICES,
        method='filter_by_veggies'
    )

    sauces = django_filters.MultipleChoiceFilter(
        label="Sauces",
        choices=Post.SAUCE_CHOICES,
        method='filter_by_sauces'
    )

    def filter_by_veggies(self, queryset, name, values):
        for value in values:
            queryset = queryset.filter(
                Q(veggie_1=value) | Q(veggie_2=value) | Q(veggie_3=value)
            )
        return queryset.distinct()

    def filter_by_sauces(self, queryset, name, values):
        for value in values:
            queryset = queryset.filter(
                Q(sauce_1=value) | Q(sauce_2=value) | Q(sauce_3=value)
            )
        return queryset.distinct()

    # POPULARITY
    sort = django_filters.ChoiceFilter(
        label='Sort By',
        choices=SORT_CHOICES,
        method='filter_by_sort',
        empty_label=None,
    )

    def filter_by_sort(self, queryset, name, value):
        if value == 'popular':
            return queryset.order_by('-num_likes', '-date_posted')
        return queryset.order_by('-date_posted')

    # CATEGORIES

    class Meta:
        model = Post
        fields = [
            'sort',
            'vegan',
            'size',
            'bread',
            'meat',
            'cheese',
            'veggies',
            'sauces',
            'temp',
            'price__gt',
            'price__lt'
        ]
