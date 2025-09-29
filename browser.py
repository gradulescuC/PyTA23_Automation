from seleniumbase import Driver



class Browser():

			driverObject = Driver() # aici am instantiat un obiect din clasa Driver
																	# care se numeste driverObject si care va fi folosit
																	# pentru apelarea tuturor metodelor de interactiune cu browserul

			def maximise_window(self):
					self.driverObject.maximize_window() # atunci cand se deschide browserul el va fi in format minimizat.
												# in cazul asta, multe elemente web pot fi ascunse,
											# iar atunci cand python le va cauta cu selenium nu le va gasi,
											# 	desi ele sunt acolo

			# def spune_ham(self, nume_animal):
			# 		self.nume_animal = nume_animal # self.nume_animal va fi atributul al clasei,
																		# iar nume_animal va fi valoare venita prin argument din afara functiei
			# 		print(f"{self.nume_animal} a facut ham")

			def close_browser(self):
					self.driverObject.quit()
									# care este diferenta dintre metoda close() si metoda quit()?
												# R: metoda quit() inchide tot browserul
										    # metoda close() inchide doar tab-ul activ


# browser = Browser()
# browser.spune_ham("grivei")

			# self este un marcator care anunta faptul ca un element (metoda sau atribut)
						# este parte dintr-o clasa.
			# atunci cand suntem intr-o clasa si scriem self urmat de numele atributului sau numele metodei
						# anuntam sistemul ca ne intereseaza sa accesam un atribut sau o metoda din acea clasa
