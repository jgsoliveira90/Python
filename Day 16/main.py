import prettytable as pt

table =  pt.PrettyTable()
listPokemons = ["Pikachu","Squirtle", "Bulbasaur"]
listTypes = ["Eletric","Water", "Grass"]
table.add_column("Pokemon Name", listPokemons)
table.add_column("Types", listTypes)

table.align = "l"

print(table)