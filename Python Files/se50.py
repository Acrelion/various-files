oblast = {'Vraca': 'VR', 'Pleven': 'EN'}
sukr = {'VR': 'Vraca', 'EN': 'Pleven'}
obshtina = {'VR':'Byla Slatina', 'EN': 'Kneja'}

print "Sukrashtenieto za Vraca e %s." % oblast['Vraca']
print "Vraca se sukrashtava na %s." % sukr['VR']
print '-' * 10
print "%s e sukrashtenieto na %s" % (oblast['Vraca'], sukr['VR'])


print '-' * 10
print "%s vkluchva %s." % (
sukr['VR'], obshtina[oblast['Vraca']])

print '-' * 10
print '%s se namira v oblast %s, koqto ima\
 sukrashtenie %s.\n' %(
obshtina[oblast['Vraca']],
sukr[oblast['Vraca']], 
oblast[sukr['VR']] )

print '-' * 10
for a, b in oblast.items():
	print "Oblast %s  ima sukrashtenie\
	%s i v neq se namira %s.\n" % (
	a, b, obshtina[b])

print oblast.get('Vraca')
print oblast['Vraca']