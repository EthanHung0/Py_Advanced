from Classes import SpellCheckPlugin,AutoSavePlugin,PluginManager

manager = PluginManager()

spellcheck = SpellCheckPlugin()
autosave = AutoSavePlugin()

manager.register(spellcheck)
manager.register(autosave)

manager.run_all()

