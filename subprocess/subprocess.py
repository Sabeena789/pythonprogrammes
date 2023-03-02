import subprocess


#1.single command
#subprocess.run(["ipconfig"])
#subprocess.run("ipconfig")
#2.Syntax for to store command output in a variable:
#output=subprocess.run("ipconfig",capture_output=True)
#output = subprocess.run(["ipconfig"], capture_output=True)
#print(output)
#print(output.stdout.decode())
#print(output.stderr.decode())

#3.Popen()
"""
cmd=["ipconfig"]
output=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)
stdout, stderr = output.communicate()
print("Standard Output:", stdout.decode())


output=subprocess.Popen("ipconfig",stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout, stderr = output.communicate()
print("Standard Output:", stdout.decode())
#print("Standard Error:", stderr.decode())
#output=subprocess.Popen(["ipconfig"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#print(output)
"""
#4.checkoutput()
#res=subprocess.check_output(["ipconfig"])
#print("output",res.decode())

#subprocess.call()
#subprocess.call("ipconfig")
#res=subprocess.call("ipconfig")
#print(res)

#5.subprocess.check_call
subprocess.check_call(["ipconfig"],shell=False)
#subprocess.check_call("ipconfig",shell=True)
