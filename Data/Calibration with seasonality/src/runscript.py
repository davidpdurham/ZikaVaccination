with open("./scriptfile", "w") as out:
	for clustI in range(100):
		out.write("cd ~/project/Zika/CalibrationPR2way/; ")
		out.write("math ")
		out.write(str(clustI+1))
		out.write(" -script CalibrationPuertoRico.m\n")
