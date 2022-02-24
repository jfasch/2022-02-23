import pprint

l = []

l.append(42)
l.append(666.7)
l.append([True, False])
l.append('Ein String mit "Doublequotes" und \'Singlequotes\'')
l.append(['eine', 'liste', 'mit', 1, 'zahl'])
l.append((1,))
l.append((1,'zwei', 3.5))
l.append({1, 2, 3})
l.append({'one': 1, 'two': 2})

pprint.pprint(l, indent=4)
