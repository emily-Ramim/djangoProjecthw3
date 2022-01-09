from django.db import connection
from django.shortcuts import render
from .models import Pokemons

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def index(request):
    return render(request, 'Index.html')


def strongest():
    sql = """
        select Name, poke.Generation
        from Pokemons, (select Generation, MAX(HP+Attack+Defense) as total
            from Pokemons
            group by Generation) poke
        where poke.Generation=Pokemons.Generation and (Pokemons.HP+Pokemons.Attack+Pokemons.Defense)=poke.total and Pokemons.Legendary='true'
        order by Pokemons.Generation;
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return dictfetchall(cursor)

def add_a_pokemon(request):
    if(request.method=='POST' and )
    Type=request.POST['Type']
    Generation=request.POST['Generation']
    Legendary=request.POST['Legendary']
    Hp=request.POST['Hp']
    Attack=request.POST['Attack']
    Defence=request.POST['Defence']
    return render(request, 'add_a_poekmon.html',)








def Query_Results(request):
    strong = strongest()
    dominants = dominant()
    return render(request, 'Query_Results.html', {'strong': strong,
                                                  'dominant': dominants})

def dominant():
    sql= """
    select Name, Pokemons.Type
    from Pokemons, (select Type, MAX(HP) as maxhp
                    from Pokemons
                    group by Type) hpm,
                    (select Type, MAX(Defense) as maxdefence
                    from Pokemons
                    group by Type) defencem,
                    (select Type, MAX(Attack) as maxattack
                    from Pokemons
                    group by Type) attackm
    where Pokemons.Type=hpm.Type and Pokemons.Type=defencem.Type and Pokemons.Type=attackm.Type
    and Pokemons.Attack=attackm.maxattack
    and Pokemons.Defense=defencem.maxdefence and Pokemons.HP=hpm.maxhp
    order by Type;
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return dictfetchall(cursor)


