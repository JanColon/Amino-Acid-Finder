import acid_combos

print("Amino Acid Finder | A program by JanColon")

## Takes user input and converts it into an uppercase string ##
nc = input("Enter Nucleotide Chain Here - ")
nc_out = nc.upper()

## Compares the user input to every array in 'acid_combos.py' ##
# Also outputs the respective amino acid associated with the chain # 
for i in acid_combos.F:
	if i == nc_out:
		print("Phenylalanine")
	else:
		pass
for i in acid_combos.L:
	if i == nc_out:
		print("Leucine")
	else:
		pass
for i in acid_combos.I:
	if i == nc_out:
		print("Isoleucine")
	else:
		pass
for i in acid_combos.M:
	if i == nc_out:
		print("Methionine")
	else:
		pass
for i in acid_combos.V:
	if i == nc_out:
		print("Valine")
	else:
		pass
for i in acid_combos.S:
	if i == nc_out:
		print("Serine")
	else:
		pass
for i in acid_combos.P:
	if i == nc_out:
		print("Proline")
	else:
		pass
for i in acid_combos.T:
	if i == nc_out:
		print("Threonine")
	else:
		pass
for i in acid_combos.A:
	if i == nc_out:
		print("Alanine")
	else:
		pass
for i in acid_combos.Y:
	if i == nc_out:
		print("Tyrosine")
	else:
		pass
for i in acid_combos.H:
	if i == nc_out:
		print("Histidine")
	else:
		pass
for i in acid_combos.Q:
	if i == nc_out:
		print("Glutamine")
	else:
		pass
for i in acid_combos.N:
	if i == nc_out:
		print("Asparagine")
	else:
		pass
for i in acid_combos.K:
	if i == nc_out:
		print("Lysine")
	else:
		pass
for i in acid_combos.D:
	if i == nc_out:
		print("Aspartic acid")
	else:
		pass
for i in acid_combos.E:
	if i == nc_out:
		print("Glutamic acid")
	else:
		pass
for i in acid_combos.C:
	if i == nc_out:
		print("Cysteine")
	else:
		pass
for i in acid_combos.W:
	if i == nc_out:
		print("Tryptophan")
	else:
		pass
for i in acid_combos.R:
	if i == nc_out:
		print("Arginine")
	else:
		pass
for i in acid_combos.G:
	if i == nc_out:
		print("Glycine")
	else:
		pass
for i in acid_combos.STP:
	if i == nc_out:
		print("Termination")
	else:
		pass
for i in acid_combos.STR:
	if i == nc_out:
		print("Initiation")
	else:
		pass
input()
