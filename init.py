from mocha import ui

mocha_widget = ui.get_widgets()
main_window = mocha_widget["MainWindow"]
# grab all widgets (application is globally defined inside mocha)
widgets = application.allWidgets()

mocha_menubar = list(filter(lambda wgt: isinstance(wgt, QMenuBar), widgets))[0]
scripts_menu = mocha_menubar.addMenu('Scripts') #create a new Scripts menu option

from Mocha_export_rendered_shapes_from_layers_or_groups import render_shapes

actions_dict = {
    "Render shapes or groups as png": (scripts_menu, render_shapes),
}

for key, value in list(actions_dict.items()):
    action = QAction(key, value[0])
    action.triggered.connect(value[1])
    value[0].addAction(action)