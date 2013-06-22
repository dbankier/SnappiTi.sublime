import sublime, sublime_plugin, subprocess

def getEnvironment():
	settings = sublime.load_settings("snappiti.sublime-settings")
	return {"PATH": settings.get('path', '/usr/local/bin')}

class SnappitiCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		env = getEnvironment()
		for region in self.view.sel():  
			if not region.empty():  
				# Get the selected text  
				s = self.view.substr(region)  
				print "S: " + s
				# output = subprocess.Popen([node_path, snappiti_path, "compile", s], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
				output = subprocess.Popen(["snappiti", "compile", s], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
				# Replace the selection with transformed text  
				self.view.replace(edit, region, output)

class SnappitiNoStylingCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		env = getEnvironment()
		for region in self.view.sel():  
			if not region.empty():  
				# Get the selected text  
				s = self.view.substr(region)  
				output = subprocess.Popen(["snappiti", "compile", "-s", s], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
				# Replace the selection with transformed text  
				self.view.replace(edit, region, output)
