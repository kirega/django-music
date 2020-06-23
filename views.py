from django.db.models import Q #just import this 'Q' object...
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
from .models import Album
from django.core.urlresolvers import reverse_lazy

class IndexView (generic.ListView):
	template_name='music/index.html'
	context_object_name='all_albums'

	def get_queryset(self):
		#return Album.objects.all()
		#Adding a search for all the album...
		query = self.request.GET.get('q')
		album_qs = Album.objects.filter(
			Q(album_title__icontains='query') | Q(artist__icontains='query')
		).distinct()
		return album_qs
	
		'''
		# - In your HTML you add this

		<form action="{% url 'index' %}" method="get">
		  <input name="q" type="text" placeholder="Search...">
		</form>
		'''

class DetailView(generic.DetailView):
	model = Album;
	template_name= 'music/detail.html'
	

class AlbumCreate(CreateView):
	model=Album
	fields=['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
	model=Album
	fields=['artist','album_title','genre','album_logo']
