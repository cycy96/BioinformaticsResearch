#! C:\Program Files\Python39\python.exe

# Import modules for CGI handling 
import cgi, cgitb

# Create instance of FieldStorage 
form = cgi.FieldStorage()

# Get data from field
uMoltype = form.getvalue('moltype')
uSeq = form.getvalue('seq')

print ("Content-type: text/html\r\n\r\n");
print ("<html>");
print ("<head>");
print ("<link type=text/css rel=stylesheet href=/rrr.css>");
print ("</head>");


print ("<body>");       
print ("<h1 class style=color:black;text-align:center;>Results of Sequence Analysis</h1>");

print ("<div align=center id=form1>");

print ("<tr>");

print ("<td>");

valid_letter= 'acgt'

def valid_sequence(uSeq):
    for letter in uSeq:
        if any(letter not in valid_letter for letter in uSeq):
            return False    
        return True
        
seqLen = len(uSeq)

print ("<b>Moltype = %s</b><br>" % (uMoltype));
print ("<b>Input sequence = %s</b><br>" % (uSeq));
print ("<b>Length = %d</b><br>" % (seqLen));

if uMoltype == 'dna':
    while not valid_sequence(uSeq):
        print ("<br><b>Note: The input sequence is not a valid DNA sequence. Press 'Back' to enter a correct DNA sequence.</b><br>")
        break
        
    if valid_sequence(uSeq):
       # to count numbers of each nucleotide bases (a,c,g,t) in the sequence 
        cntA=0; cntC=0; cntG=0; cntT=0;

        for char in uSeq:
            if char == 'a':
                    cntA+=1
            elif char == 'c':
                    cntC+=1
            elif char == 'g':
                    cntG+=1
            elif char == 't':
                    cntT+=1
            else:
                    pass        
          
        print ("<b>Number of bases:</b></br>");
        print ("<b>a= %d</b>" % (cntA));
        print ("<b>c= %d</b>" % (cntC));
        print ("<b>g= %d</b>" % (cntG));
        print ("<b>t= %d</b>" % (cntT)); 

        #Create a counter
        GC_Count = 0


        #Loop through all the letters in sequence
        for letter in uSeq:
            if (letter == 'g' or letter == 'c'):
                GC_Count +=1
                GC = round((float(GC_Count)/float(seqLen)*100), 2)
        
        print("<br><b>GC-Content="+str(GC)+"%</b></br>")
        
        def complement(uSeq):
                return uSeq.replace('a','T').replace('t','A').replace('g','C').replace('c','G').casefold()
        comple = complement(uSeq)
                
        print ("<b>Sequence Complement: %s</b><br>" % (comple));
        
        def reverse_complement(uSeq):
                return uSeq.replace('a','T').replace('t','A').replace('g','C').replace('c','G').casefold()[::-1]
        rc_sequence = reverse_complement(uSeq)

        print ("<b>Sequence Reverse Complement: %s</b><br>" % (rc_sequence));

           
        RNA = uSeq.replace('t', 'u').casefold()
        print ("<b>Result of transcription: %s</b><br>" % (RNA));
         
        protein = {"ttt" : "F", "ctt" : "L", "att" : "I", "gtt" : "V",
               "ttc" : "F", "ctc" : "L", "atc" : "I", "gtc" : "V",
               "tta" : "L", "cta" : "L", "ata" : "I", "gta" : "V",
               "ttg" : "L", "ctg" : "L", "atg" : "M", "gtg" : "V",
               "tct" : "S", "cct" : "P", "act" : "T", "gct" : "A",
               "tcc" : "S", "ccc" : "P", "acc" : "T", "gcc" : "A",
               "tca" : "S", "cca" : "P", "aca" : "T", "gca" : "A",
               "tcg" : "S", "ccg" : "P", "acg" : "T", "gcg" : "A",
               "tat" : "Y", "cat" : "H", "aat" : "N", "gat" : "D",
               "tac" : "Y", "cac" : "H", "aac" : "N", "gac" : "D",
               "taa" : "stop", "caa" : "Q", "aaa" : "K", "gaa" : "E",
               "tag" : "stop", "cag" : "Q", "aag" : "K", "gag" : "E",
               "tgt" : "C", "cgt" : "R", "agt" : "S", "ggt" : "G",
               "tgc" : "C", "cgc" : "R", "agc" : "S", "ggc" : "G",
               "tga" : "stop", "cga" : "R", "aga" : "R", "gga" : "G",
               "tgg" : "W", "cgg" : "R", "agg" : "R", "ggg" : "G" 
               }
        
        protein_seq = ""
        for i in range(0, seqLen, 3):
            if protein[uSeq[i:i+3]] == "stop" :
                break 
            protein_seq += protein[uSeq[i:i+3]]
        print ("<b>Result of translation: %s</b><br>" % (protein_seq));
        
        print ("</div>");


valid_aa= 'acdefghiklmnpqrstvwy'        
def valid_protein(uSeq):
    for letter in uSeq:
        if any(letter not in valid_aa for letter in uSeq):
            return False    
        return True

# if moltype is 'protein', then pass
if uMoltype == 'protein':
    while not valid_protein(uSeq):
        print ("<br><b>Note: The input sequence is not a valid protein sequence. Click 'Back' to enter a correct protein sequence.</b></br>")
        break    
        
    if valid_protein(uSeq):
        pass

print ("</div>");

print ("<div align=center>");
print ("<input type=button value=Back onClick='history.go(-1); return true;'>&nbsp;&nbsp;&nbsp;");
print ("<input type=button value=Close onClick='window.close(); return true;'>");
print ("</div>");
print ("</body>");
print ("</html>");