# import di altri componenti
from django.db import models
from django.utils import timezone

# questo definisce il model (e' un oggetto)
# class: indica che stiamo definendo un oggetto
# Post: nome del modello (inizia sempre con una maiuscola)
# models.Model: indica a Django che è un modello, e quindi va salvato nel DB

class Post(models.Model):
	# definiamo le properties del modello:
	# chiave esterna verso un altro oggetto (author)
    author = models.ForeignKey('auth.User')
	# stringa di max 200 caratteri
    title = models.CharField(max_length=200)
	# stringa di testo senza limiti (per il corpo del post)
    text = models.TextField()
	# campo data/ora
    created_date = models.DateTimeField(
            default=timezone.now)
	# campo data/ora
    published_date = models.DateTimeField(
            blank=True, null=True)

	# metodo "publish": una funzione (va sempre in minuscolo)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

	# la funzione restituisce un valore
    def __str__(self):
        return self.title
