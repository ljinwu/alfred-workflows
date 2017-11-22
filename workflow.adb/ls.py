import commands, json

packages = commands.getoutput('source ~/.bash_profile; adb shell pm list packages -3')

items = []
for package in packages.split('\n'):
	item = {'title': package.replace('package:', ''), 'arg': package.replace('package:', '')}
	items.append(item)
print json.dumps({'items':items})
