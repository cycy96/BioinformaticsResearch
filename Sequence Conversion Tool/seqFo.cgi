#! C:\Program Files\Python39\python.exe

# Import modules for CGI handling 
import cgi, cgitb

#import regular expression module
import re

# Create instance of FieldStorage 
form = cgi.FieldStorage()

# Get data from field
Inseq = form.getvalue('seq')
formatted_Inseq=str(Inseq)

print ("Content-type: text/html\r\n\r\n");
print ("<html>");
print ("<head>");
print ("</head>");
print ("<body>");       
print ("<h1 style=color:black;text-align:left;>Online System for Conversion of Sequence File Format</h1>");

print("<form action=http://localhost/cgi-bin/test/seqCo.cgi method=post>");

#defines a hidden input field, stores what database record that needs to be updated when the form is submitted..
print ("<input type=hidden name=seq value='%s'>"%(formatted_Inseq));

#If the user input file is in Genbank format, print the following command and open the file
if re.search(r"LOCUS\s+(.+)\s+",Inseq):
    print("<h3><b>The input sequence is in <u>Genbank</u> format</b></h3>");
        
#If the user input file is in EMBL format, print the following command and open the file
if re.search(r"ID\s+(.+)",Inseq):
    print("<h3><b>The input sequence is in <u>EMBL</u> format</b></h3>");
        
print("<i>Step 2 - Select a sequence format</i><br>");

print("<br><input type=radio style='margin-left: 10; margin-right: 10' id=stype name=format value=fasta>FASTA&nbsp;&nbsp;&nbsp;");

print("<br><input type=radio style='margin-left: 10; margin-right: 10' id=stype name=format value=gcg>GCG<br><br>");

print("<input type=submit id=run name=run value=Convert onclick=runAnalysis()>&nbsp;&nbsp;&nbsp;");

print ("<input type=button value=Back onClick='history.go(-1); return true;'>&nbsp;&nbsp;&nbsp;");

print("<button type=button onclick=window.close(); return true;>Exit</button></p>");

print ("</form>");

print ("</body>");
print ("</html>");