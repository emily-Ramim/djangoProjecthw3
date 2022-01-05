from django.db import connection
from django.shortcuts import render
from .models import Pokemons


def Index(request):
    sql = """
        select Name, poke.Generation
        from Pokemons, (select Generation, MAX(HP+Attack+Defense) as total
        from Pokemons
        group by Generation) poke
        where poke.Generation=Pokemons.Generation and (Pokemons.HP+Pokemons.Attack+Pokemons.Defense)=poke.total and Pokemons.Legendary='true'
        order by Pokemons.Generation;
    """
    sql_res = Pokemons.objects.raw(sql)
    return render(request, 'Index.html', {'sql_res': sql_res})



def dictfetchall(cursor):
"Return all rows from a cursor as a dict"
columns = [col[0] for col in cursor.description]
return [dict(zip(columns, row)) for row in cursor.fetchall()]