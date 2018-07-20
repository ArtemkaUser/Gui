def init_menu_bar(self):
    menu_bar = self.menuBar()
    file_menu = menu_bar.addMenu('File')
    file_menu.addAction(self.add_cell_in_bar('&New', 'Create new project',
                                             qApp.quit, 'Ctrl+N', 'icons/new.png'))
    file_menu.addAction(self.add_cell_in_bar('&Open', 'Open project',
                                             qApp.quit, 'Ctrl+O', 'icons/open.png'))
    file_menu.addAction(self.add_cell_in_bar('&Save', 'Save project',
                                             qApp.quit, 'Ctrl+S', 'icons/save.png'))
    file_menu.addAction(self.add_cell_in_bar('&Save as', 'Save as project',
                                             qApp.quit, 'Ctrl+Shift+S', 'icons/save-as.png'))
    file_menu.addAction(self.add_cell_in_bar('&Exit', 'Exit application',
                                             qApp.quit, 'Ctrl+Q', 'icons/exit.png'))

def init_tool_bar(self):
    toolbar = self.addToolBar('Tool Bar')
    toolbar.addAction(self.add_cell_in_bar('&Exit', 'Exit application',
                                           qApp.quit, '', 'icons/exit.png'))

def add_cell_in_bar(self, name, status_tip, trigger, short_cut, icon):
    """ the method fills the data into QAction and return object"""
    cell = QAction(QIcon(icon), name, self)
    cell.setStatusTip(status_tip)
    cell.triggered.connect(trigger)
    cell.setShortcut(short_cut)
    return cell
