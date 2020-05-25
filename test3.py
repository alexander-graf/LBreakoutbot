from oosheet import OODoc
doc = OODoc()
doc.dispatch('InsertText', ('Text', 'Hello World'))
doc.dispatch('CenterPara', True)

