with open("./scriptfile", "w") as out:
	for clustI in range(34):
		out.write("cd ~/project/Zika/AttackRateCalibration/; ")
		out.write("math ")
		out.write(str(clustI+1))
		out.write(" -script CalibrationAllCountries.m\n")
