import sublime, sublime_plugin, subprocess

class SnappitiCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():  
			if not region.empty():  
                # Get the selected text  
				s = self.view.substr(region)  
				print "S: " + s
                output = subprocess.Popen(["/usr/local/bin/node", "/usr/local/bin/snappiti","compile","View#win"], stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
                # Replace the selection with transformed text  
                self.view.replace(edit, region, output)

class SnappitiNoStylingCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():  
			if not region.empty():  
                # Get the selected text  
				s = self.view.substr(region)  
                output = subprocess.Popen(["/usr/local/bin/node", "/usr/local/bin/snappiti","compile","View#win", "-s"], stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
                # Replace the selection with transformed text  
                self.view.replace(edit, region, output)
