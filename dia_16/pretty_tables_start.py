from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Bulbasaur", "Charmander"])
table.add_column("Pokemon Type", ["Electric", "Water", "Grass", "Fire"])

table.align = "l"

print(table)