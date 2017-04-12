dc = {100000: "python",
      100001: "java",
      100002: "nodejs"}
print(dc)

dc.update({"others": {100003: "javascript"}})
dc.update({100004: "sikuli"})

print('''
++++++++++++++
{}
'''.format(dc))