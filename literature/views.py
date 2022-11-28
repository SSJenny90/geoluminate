from literature.models import Publication, Author
from django.views.generic import DetailView
from django_filters.views import FilterView
from .filters import PublicationFilter
from django.utils.translation import gettext_lazy as _
from crossref.views import WorksByYearMixin
from crossref.models import Work
from .menu import PublicationMenu
from .api.serialize import AuthorSerializer
from datatables.views import DatatablesReadOnlyView
from .api.serialize import AuthorSerializer
import datatables
from django.shortcuts import get_object_or_404
from geoluminate.utils import DATABASE


class PublicationList(FilterView, WorksByYearMixin):
    model = Work
    template_name = 'literature/list.html'
    partial_template = 'literature/partials/publication_list.html'
    publication_template = 'crossref/publication.html'

    paginate_by = 50
    filterset_class = PublicationFilter

    def get_template_names(self):
        if self.request.htmx:
            return [self.partial_template]
        else:
            return [self.template_name]  # The actual form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.filterset_class:
            context['parameters'] = self.get_filter_parameters()
        context['pub_template'] = self.publication_template
        return context

    def get_queryset(self):
        return super().get_queryset()

    def get_filter_parameters(self):
        """Gets url parameters from the filter and returns as a string to be placed behind paginator links"""
        request_copy = self.request.GET.copy()
        request_copy.pop('page', True)
        if request_copy:
            return '&' + request_copy.urlencode()
        else:
            return ''


class PublicationDetail(DetailView):
    template_name = "literature/details.html"
    model = Publication

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_menu'] = PublicationMenu(context['object'])
        return context


@datatables.register
class AuthorList(DatatablesReadOnlyView):
    model = Author
    queryset = Author.objects.with_work_counts().filter(as_lead__gt=0)
    search_fields = ('family', 'given')
    fields = ['family', 'given', 'ORCID', 'id', 'as_lead', 'as_supporting']
    ordering_fields = ['-as_lead', '-as_supporting']
    base_serializer = AuthorSerializer
    invisible_fields = ['id', ]
    datatables = dict(
        rowId='id',
        scrollY='100vh',
        deferRender=True,
        scroller=True,
    )


class AuthorDetail(DetailView):
    template_name = "main/author_detail.html"
    model = Author


class HTMXDetail(DetailView):
    """Shortcut for calling Detail view with model=Publication from `urls.py`.
    """
    model = Publication

    def get_template_names(self):
        return [f"literature/hx/{self.template_name}"]


# class MapView(KeplerFullPageView):


HX = HTMXDetail.as_view


def get_related_publications(request, pk):
    pub = get_object_or_404(Publication, pk=pk)
    bbox = pub.bbox
    DATABASE.object.filter(geom__in=bbox)