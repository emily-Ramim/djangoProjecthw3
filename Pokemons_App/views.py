from django.db import connection
from django.shortcuts import render
from .models import Pokemons


def Query_Results(request):
    sql = """
        select Name, Generation
        from Pokemons;
    """
    sql_res = Pokemons.objects.raw(sql)
    return render(request, 'Query_Results.html', {'sql_res': sql_res})



