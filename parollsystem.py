def my_split(sentence, sep):
	lst = []
	tmp = ''
	for c in sentence:
		if c == sep:
			lst.append(tmp)
			tmp = ''
		else:
			tmp += c
	if tmp:
		lst.append(tmp)
	return(lst)

def my_join(sent , string) :
	s = ""
	for i in sent :
		if i != sent[len(sent)-1] :
			i = i + string 
			s = s + i
		else :
			s = s + i
	return s 

class Employee:
	def __init__(self, id, name):
		self.id = id
		self.name = name

class SalaryEmployee(Employee):
	def __init__(self, id, name, monthly_salary):
		super().__init__(id,name)
		self.monthly_salary = monthly_salary

	def calculate_payroll(self):
		return self.monthly_salary 

class PayrollSystem:
	def calculate_payroll(self, employees):
		for employee in employees:
			print("Employee Payroll")
			print("================")
			print(f"Payroll for: {employee.id} - {employee.name}")
			print(f"- Check amount: {employee.calculate_salary()}")
			print("")

class Employee:
	def __init__(self, id, name):
		self.id = id
		self.name = name
	def ask_name(self):
		try:
			self.name = str(input("Please enter employee name:"))
		except:
			self.name = ""

class SalaryEmployee(Employee):
	def __init__(self, id, name,monthly_salary):
		super().__init__(id, name)
		self.salary = 'M'
		self.monthly_salary = int(monthly_salary)


	def ask_salary(self):
		try:
			self.monthly_salary = int(input("Please enter monthly salary:"))
		except:
			self.monthly_salary = 0
	
	
	def calculate_salary(self) :
		return self.monthly_salary
            

class HourlyEmployee(Employee) :
	def __init__(self ,id,name,hours_worked,hour_rate):
		super().__init__(id,name)
		self.salary = 'H'
		self.hours_worked = int(hours_worked)
		self.hour_rate = int(hour_rate)	
		
	def ask_salary(self):
		try:
			self.hours_worked = int(input("Please enter hours worked:"))
		except:
			self.hours_worked = 0
		try:
			self.hour_rate = int(input("Please enter hour rate:"))
		except:
			self.hour_rate = 0
	
	def calculate_salary(self) :
		return self.hours_worked * self.hour_rate
	
class CommissionEmployee(SalaryEmployee) :
	def __init__(self ,id,name,monthly_salary,commission):
		super().__init__(id,name,monthly_salary)
		self.salarycommission = 'C'
		self.commission = int(commission)
		
	def ask_salary(self):
		SalaryEmployee.ask_salary(self)
		try:
			self.commission = int(input("Please enter commission:"))
		except:
			self.commission = 0
	
	def calculate_salary(self) :
		return self.commission + self.monthly_salary

salary_employees = []
salary_employees_file = []
id = 1

while True:
	print("(1) Add employee to employees\n(2) Write employees to file\n(3) Read employees from file\n(4) Print payroll\n(0) Quit\n")
	selection = int(input("Please select one: "))
	if selection == 1:
		while True:
			salarytype = int(input("Please enter salary type:\n(1) monthly\n(2) hourly\n(3) commission\n(0) Quit\n"))
			if salarytype == 1 :
				salary = []
				employee = SalaryEmployee(id,'',0)
				SalaryEmployee.ask_name(employee)
				SalaryEmployee.ask_salary(employee)
				salary_employees.append(employee)
				salary.append(employee)
				id += 1
			elif salarytype == 2 :
				hour = []
				employee = HourlyEmployee(id,'',0,0)
				HourlyEmployee.ask_name(employee)
				HourlyEmployee.ask_salary(employee)
				salary_employees.append(employee)
				hour.append(employee)
				id += 1
			elif salarytype == 3:
				comission = [] 
				employee = CommissionEmployee(id,'',0,0)
				CommissionEmployee.ask_name(employee)
				CommissionEmployee.ask_salary(employee)
				salary_employees.append(employee)
				comission.append(employee)
				id += 1
			elif salarytype == 0:
				break
			else:
				print("Incorrect selection.")
	elif selection == 2:
		se = []
		se1 = []
		se2 = []
		stringofse = []
		writefile = open("employee.csv","w")
		for employee in salary_employees :
			if len(salary) != 0:
				for i in salary :
					if i == employee :
						i = str(i.id) +" "+ i.name +" " + str(i.monthly_salary) 
						t = 0
						for v in range(0,len(i)) :
							if i[v] == " " and (i[v-1].isnumeric() == True or i[v+1].isnumeric() == True):
								s = i[t:v]
								se.append(s)
								t = v+1
							elif i[v] != " " and v == len(i) -1 :
								s = i[t:]
								se.append(s)
						se.insert(2, "M")
						String_salary = my_join(se , ",")
						stringofse.append(String_salary)
			if len(hour) != 0:
				for i in hour :
					if i == employee :
						i = str(i.id) +" "+ i.name +" " + str(i.hours_worked)+ " " +str(i.hour_rate)
						t= 0
						for v in range(0,len(i)) :
							if i[v] == " " and (i[v-1].isnumeric() == True or i[v+1].isnumeric() == True):
								s = i[t:v]
								se1.append(s)
								t = v+1
							elif i[v] != " " and v == len(i) -1 :
								s = i[t:]
								se1.append(s)
						se1.insert(2, "H")
						String_hour = my_join(se1 , ",")
						stringofse.append(String_hour)
			if len(comission) != 0:
				for i in comission :
					if i == employee :
						i = str(i.id) +" "+ i.name +" " + str(i.monthly_salary)+ " " +str(i.commission)
						t = 0
						for v in range(0,len(i)) :
							if i[v] == " " and (i[v-1].isnumeric() == True or i[v+1].isnumeric() == True):
								s = i[t:v]
								se2.append(s)
								t = v+1
							elif i[v] != " " and v == len(i) -1 :
								s = i[t:]
								se2.append(s)
						se2.insert(2, "C")
						String_comission = my_join(se2 , ",")
						stringofse.append(String_comission)
		stringofse.append('')
		w = writefile.write(my_join(stringofse , "\n"))
		
		writefile.close()
		print((len(salary)+len(hour) + len(comission)) ," employee(s) added to employee.csv")
	elif selection == 3 :
		readfile = open("employee.csv","r")
		r = readfile.readlines()
		s = []
		s1 = []
		s2 = []
		id = 1
		for i in r :
			t = []
			t = my_split(i ,",")
			for c in range(0,len(t)) :
				if t[2] == 'M' :
					t.pop(2)
					s = t
					tt = 1
					name = s[tt]
					salary = int(s[tt+1])
					salary_employees_file.append(SalaryEmployee(id,name,salary))
					id += 1
				elif t[2] == 'H' :
					t.pop(2)
					s1 = t
					tt = 1
					name = s1[tt]
					hours_worked = int(s1[tt+1])
					hour_rate = int(s1[tt+2])
					salary_employees_file.append(HourlyEmployee(id,name,hours_worked,hour_rate))
					id += 1
				elif t[2] == 'C' :
					t.pop(2)
					s2 = t
					tt = 1
					name = s2[tt]
					salary = int(s2[tt+1])
					commission = int(s2[tt+2])
					salary_employees_file.append(CommissionEmployee(id,name,salary,commission))
					id += 1
		readfile.close()
		print(len(salary_employees_file)," employee(s) read from employee.csv")
	elif selection == 4:
		payroll_system = PayrollSystem()
		payroll_system.calculate_payroll(salary_employees)
	elif selection == 0:
		print("Service shutting down, thank you.")
		break
	else:
		print("Incorrect selection.")