import sublime
import sublime_plugin

class ToggleOnlyCommand(sublime_plugin.TextCommand):
  def only_after(self, word, edit):
    point = self.the_text.find(word)
    if (point != -1):
      point = point + self.line_start + len(word)
      self.view.insert(edit, point, '.only')
      return True
    return False

  def run(self, edit):
    the_line = self.view.line(self.view.sel()[0])
    self.line_start = the_line.begin()
    self.the_text = self.view.substr(the_line)

    point = self.the_text.find('.only')
    if (point != -1):
      the_only = sublime.Region(point + self.line_start, point + self.line_start + len('.only'))
      self.view.erase(edit, the_only)
      return

    if (self.only_after('describe', edit)):
      return
    if (self.only_after('it', edit)):
      return
    
