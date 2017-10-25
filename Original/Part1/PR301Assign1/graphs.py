class Graph(metaclass=ABCMeta):

	def draw_graph(self, arg):
		pass


class LineGraph(Graph):

	def draw_graph(self, arg):
		arg = arg.upper()
		
		ages = self.db.get_data("AGE")
		salarys = self.db.get_data("SALARY")
		self.view.age_salary(ages, salarys)


class Line(Graph):

	def draw_graph(self, arg):
		arg = arg.upper()
		
		sales = self.db.get_data("SALES")
		ages = self.db.get_data("AGE")
		self.view.pygal_line_salebased(sales, ages)		

	
class PieGraph(Graph):
	
	def draw_graph(self, arg):
		arg = arg.upper()

		self.db.get_data(arg)
		self.view.plot_pie_gender(self.db.get_data(arg))


class BarGraph(Graph):

	def draw_graph(self, arg):
		arg = arg.upper()
		
		self.db.get_data(arg):
		self.view.plot_bar(self.db.get_data(arg))
	
	
class ScatterGraph(Graph):

	def draw_graph(self, arg):
		arg = arg.upper()
		
		if arg == "SALARY":
			salary = self.db.get_data("SALARY")
			age = self.db.get_data("AGE")
			self.view.age_salary(age, salary)
		elif arg == "SALES":
			sales = self.db.get_data("SALES")
			age = self.db.get_data("AGE")
			self.view.pygal_line_salebased(sales, age)
		else:
			print('The valid options for a scatter graph are salary or sales')
