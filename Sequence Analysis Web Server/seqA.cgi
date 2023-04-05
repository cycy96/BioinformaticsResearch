#! C:\Program Files\Python39\python.exe

print ("Content-type: text/html\r\n\r\n");
print ("<html>");
print ("<head><title>Sequence analysis entry form</title>");

print ("<link type=text/css rel=stylesheet href=/rrr.css>");

print ("</head>");


print ("<body>");

print ("<h1 style=color:black;text-align:center;>Sequence Analysis</h1>");

print ("<form action=http://localhost/cgi-bin/sqf7007/result.cgi method=post>");

print ("<div align=center id=form1>");

print ("<table width=75%>");

print ("<tr>");

print ("<td>");

print ("<form id=formquery>");

print ("<fieldset>");

print ("<legend>Entry Form</legend>");

print ("Moltype: <input type=radio id=mtype name=moltype value=dna>DNA&nbsp;&nbsp;&nbsp;");

print ("<input type=radio id=mtype name=moltype value=protein>Protein<br><br>");

print ("<p>Input sequence: <br><textarea rows=4 cols=50 id=sequence name=seq placeholder ='Please enter a correct DNA or protein sequence'></textarea><br><br></p>");

print ("<input type=submit id=run name=run value=Run onclick=runAnalysis()>&nbsp;&nbsp;&nbsp;");

print ("<input type=button id=reset name=reset value=Reset onclick=location.reload()>&nbsp;&nbsp;&nbsp;"); 

print ("<input type=button id=cancel name=cancel value=Cancel onclick=window.close(); return true;>");

print ("</fieldset>");

print ("</form>");

print ("</td></tr>");

print ("</table>");

print ("</div>");

print ("</body>");
print ("</html>");