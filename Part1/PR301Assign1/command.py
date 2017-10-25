import cmd
import sys
import graphs

# noinspection PyUnusedLocal
class Command(cmd.Cmd):
    def __init__(self, new_file_handler, new_db, new_view):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.file_handler = new_file_handler
        self.db = new_db
        self.view = new_view
		
		self.graphs_types = {'LineGraph' : LineGraph()
					   'Line' : Line()
					   'Pie' : PieGraph()
					   'Bar' : Bar()
					   'Scatter' : Scatter()
					   }

    @staticmethod
    def do_quit(arg):
        sys.exit(1)

		
	def do_graph(self, arg):
		arg = arg.upper()
		return self.graph_types[arg].draw_graph(arg)
		

    # Tim
    def help_quit(self):
        print(self.file_handler.open_help('quit'))

    # Tim
    def do_open(self, arg):
        contents = self.file_handler.open(arg)
        if contents:
            self.db.insert(contents)

    # Rosemary
    def help_open(self):
        print(self.file_handler.open_help("open"))


    def help_bar(self):
        print(self.file_handler.open_help("bar"))

    # Tim
    def do_get(self, arg):
        self.db.query(arg)

    # Rosemary
    def help_get(self):
        print(self.file_handler.open_help('get'))


    # Rosemary
    def help_pie(self):
        print(self.file_handler.open_help('pie'))


    # Rosemary
    def help_line(self):
        print(self.file_handler.open_help('line'))


    # Rosemary
    def help_linegraph(self):
        print(self.file_handler.open_help('linegraph'))


    def help_scatter(self):
         print(self.file_handler.open_help('scatter'))

    # Tim
    def do_reload(self, arg):
        self.db.load()

    # Rosemary
    def help_reload(self):
        print(self.file_handler.open_help('reload'))
		

	
