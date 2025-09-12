########### Caso queira um filtro duplo ################################
import django_filters as df
from django.db.models import Q
from .models import Autor

class AutorFilter(df.FilterSet):
    # ?autor=jorge  → procura em autor OU s_autor (parcial, sem diferenciar maiúsc/minúsc)
    autor = df.CharFilter(method='filter_autor')

    # ?nacio=brasileira → compara case-insensitive (ex.: "Brasileira" == "brasileira")
    nacio = df.CharFilter(field_name='nacio', lookup_expr='iexact')

    def filter_autor(self, qs, value: str):
        if not value:
            return qs
        return qs.filter(Q(autor__icontains=value) | Q(s_autor__icontains=value))

    class Meta:
        model = Autor
        fields = []  # usamos os campos customizados acima
