with open("./scriptfile", "w") as out:
	for MCMCi in range(5000):
		for country in range(34):
			out.write("cd ~/project/Zika/Uncertainty/; ")
			out.write("math ")
			out.write(str(MCMCi+1))
			out.write(" ")
			out.write(str(country+1))
			out.write(" -script GenerateZikaResults.m\n")
