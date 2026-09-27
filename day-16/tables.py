from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Champion", ["Lux", "Viego", "Caitlyn", "Gwen"])
table.add_column("Region", ["Demacia", "Shadow Isles", "Piltover", "Shadow Isles"])

table.align = "l"

print(table)