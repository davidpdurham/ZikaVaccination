with open("./scriptfile", "w") as out:
	for country in range(34):
		for attR in [0.25]:
			for lag in [0, 10]:
				out.write("cd ~/project/Zika/AgeScenarios/; ")
				out.write("math ")
				out.write(str(country+1))
				out.write(" ")
				out.write(str(attR))
				out.write(" ")
				out.write(str(lag))
				out.write(" -script GenerateZikaResults.m\n")
