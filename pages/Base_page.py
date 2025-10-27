# Base_page este un fisier care contine o clasa in interiorul careia
# 		vom defini metode ce vor fi folosite in mai multe locuri
#  cu alte cuvinte, vor fi folosite in mai multe fisiere de steps cu diverse inputuri
# 		si care nu ar avea sens sa fie redefinite de multe ori in fisierele de tip pages
from browser import Browser


class Base_page(Browser):

		def insert_input(self, input_value, element):
				if(input_value != 'null'):
						self.driverObject.find_element(*element).send_keys(input_value)

		def verify_error_message(self,err,element):
				actual_error_message = self.driverObject.find_element(*element).text
				assert err == actual_error_message, f"Expected error message {err} is different from actual error message {actual_error_message}"

'''
FEATURE FILE: And I insert password "<password_value>"
| standard_user  | null           | Epic sadface: Password is required                                        |

------------------------------------------------------------------
STEP DEFINITION FILE: 
@when('I insert password "{password}"')
def step_impl(context,password):
		context.base_page.insert_input(password,PASSWORD_SELECTOR)
------------------------------------------------------------------
BASE_PAGE
		def insert_input(self, input_value, element):
				if(input_value != 'null'):
						self.driverObject.find_element(*element).send_keys(input_value)
						
DACA(CONDITIE):
		ATUNCI:  EXECUTA LINIE DE COD
		
Daca nu avem instructiune de ELSE e ca si cum am scrie urmatoarea linie de cod:
IF(CONDITIE):
		ATUNCI:  EXECUTA LINIE DE COD
ELSE:
	pass
'''