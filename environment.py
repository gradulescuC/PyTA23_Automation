from browser import Browser


# before_all este un marcator care defineste o metoda ce contine cod
						# pe care trebuie sa il ruleze sistemul inainte de a rula primul test din suita de teste (inainte de toate testele)
def before_all(context):
		  # context va fi ca un fel de cutiuta care va stoca toate obiectele instantiate in scopul proiectului
			# toate clasele care vor fi instantiate aici vor trebui sa fie importate
			# atunci cand vrem sa importam o clasa definita in alt fisier putem face hover pe ea
							# adica punem cursorul pe numele ei fara sa dam click

			# intrebare: ce inseamna instantiere?
						  # o instantiere reprezinta procesul de alocarea unui spatiu de memorie
												# care va fi identificat de numele obiectului

			# corolar: - o variabila este o adresa de memorie identificata de numele variabilei, care poate sa stocheze valori ce se pot schimba pe parcursul executiei programului
								# - o constanta este o adresa de memorie identificata de numele constantei, care poate sa stocheze valori ce nu se pot schimba pe parcursul executiei programului
			context.browser = Browser()
			context.browser.maximise_window()


def after_all(context):
			context.browser.close_browser()