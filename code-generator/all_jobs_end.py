import json
x = t1_flow.deploy()
s = str(x[0])
s = s.replace("'",'"')
s = s.replace("None",'"None"')
s = s.replace('False','"False"')
s = s.replace("True",'"True"')
s = s.replace("\n",'')
j = json.loads(s)
assert j['successful_smart_folders_count'] == 1 