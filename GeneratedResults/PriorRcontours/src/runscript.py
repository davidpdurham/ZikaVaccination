with open("./scriptfile", "w") as out:
	for country in range(34):
		out.write("cd ~/project/Zika/PriorR/; ")
		out.write("math ")
		out.write(str(country+1))
		out.write(" -script GenerateZikaResults.m\n")
