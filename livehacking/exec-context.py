import pprint

eine_variable = 666
noch_eine_variable = 'hallo'

#pprint.pprint(globals())


code_str = '''
eine_variable = 2
noch_eine_variable = 3
'''
context = {}

exec(code_str, context)

print('eine_variable:', eine_variable)
print('noch_eine_variable:', noch_eine_variable)

pprint.pprint(context)
