#! C:\Program Files\Python39\python.exe

print ("Content-type: text/html\r\n\r\n");
print ("<html>");
print ("<head><title>Online System for Conversion of Sequence File Format</title>");


print ("</head>");

print ("<body>");

print ("<h1 style=color:black;text-align:left;>Online System for Conversion of Sequence File Format</h1>");

print ("<form action=http://localhost/cgi-bin/test/seqFo.cgi method=post>");

print ("<p><i>Step 1 - Enter the sequence(s)</i></p>");

print ("<textarea rows=10 cols=90 id=sequence name=seq placeholder ='Type your sequence(s) here..'></textarea><br></p>");

print ("<input type=submit id=run name=run value=Submit onclick=runAnalysis()>&nbsp;&nbsp;&nbsp;");

print ("<input type=button id=reset name=reset value=Reset onclick=location.reload()>&nbsp;&nbsp;&nbsp;"); 

print ("<input type=button id=cancel name=cancel value=Exit onclick=window.close(); return true;>");

print ("</body>");
print ("</html>");