#! C:\Program Files\Python39\python.exe

#import regular expression module
import re

# Import modules for CGI handling 
import cgi, cgitb

# Create instance of FieldStorage 
form = cgi.FieldStorage()

# Get data from field
stype = form.getvalue('format')
Inseq = form.getvalue('seq')
formatted_Inseq=str(Inseq)

print ("Content-type: text/html\r\n\r\n");
print ("<html>");
print ("<head>");

print ("</head>");
print ("<body>");       
print ("<h1 class style=color:black;text-align:left;>Online System for Conversion of Sequence File Format</h1>");

#defines a hidden input field, stores what database record that needs to be updated when the form is submitted..
print ("<input type=hidden name=seq value='%s'>"%(formatted_Inseq));

#If the user input is in FASTA format, print the following command
if stype == "fasta":
    print("<h3><b>The input sequence is in <u>FASTA</u> format</b></h3>")
    
    print ("<fieldset>");
    
    #If the user input is in GENBANK format, print the following command
    if re.search(r"LOCUS\s+(.+)\s+",Inseq):
        
        #global vars
        acc = ""
        org = ""
        seq = ""
            
        x = formatted_Inseq
        #Split a string into a list 
        seqlines = x.splitlines()
        
        #to manipulate each items in lines
        #loop is to read each items in seqlines
        #variable line has list string data type
        for line in seqlines:
            
            
            # to extract the value of sequence accession, name and base count by using re.match function
            matchAccess = re.match(r"\s*ACCESSION\s+(.+)", line, re.IGNORECASE)
            
            if matchAccess:
                acc = matchAccess.group(1)  
                
            
            # to extract the value of sequence organism, name and base count by using re.match function
            matchOrganism = re.match(r'\s*ORGANISM\s+(.+)', line, re.IGNORECASE)

            if matchOrganism:
                org = matchOrganism.group(1)

            # to extract sequence lines
            matchSeq = re.match(r"\s+\d+\s+(.+)", line, re.IGNORECASE)
            
            if matchSeq:
                # extract the sequence from group(1) and assign it into a variable named seqLines
                seqline = matchSeq.group(1)

                # to remove " " and replaced with '' using re.sub function
                seqline = re.sub(r" ","", seqline)

                # to concatenate all sequence parts into a single sequence line
                seq += seqline

        if seq:
            #to store the splitted 'seq'
            tempSplittedSeq = []
           
            seqLen = len(seq)
            
            #number of characters to cut off
            cutoff = 120

            #to split a single line 'seq' into multiple lines and store it in a list
            #set for 120 characters per line
            for i in range(0, seqLen, cutoff):
                tempSplittedSeq.append(seq[i:i+cutoff])

            #to format the header line
            head = '>' + acc.strip() + ' | ' + org.strip() + ' | ' + str(seqLen) + 'bp'+ "<br>"
            print(head);
            
            #sequnce lines in 120 characters per line
            for currentLine in tempSplittedSeq:
                print(currentLine)
                
    #If the user input is in EMBL format, print the following command
    if re.search(r"ID\s+(.+)",Inseq):
    
        #global vars
        ID=''
        org=''
        seq=''

        x = formatted_Inseq
        #Split a string into a list 
        seqlines = x.splitlines()
        
        for line in seqlines:
       
            ###to extract value of ID
            matchID = re.match(r'ID\s+(\w+)', line, re.I)

            if matchID:
                ID=matchID.group(1)
                
            
            ###to extract value of organism
            matchOrganism = re.match(r'FT\s+.ORGANISM\=\"(.+)\"', line, re.I)

            #if match
            if matchOrganism:
                org=matchOrganism.group(1)

            ###to extract sequence lines
            matchSeq=re.match(r"(.+)\s+(\d+)$",line)

            #if match
            if matchSeq:
                seqline=matchSeq.group(1)
                seqline=re.sub(r" ","",seqline) #to remove' 'and replace with '',using re.sub function
                seq +=seqline

            ###to print and format the extracted values in Fasta sequence file format
            #(i) on the command prompt, and (ii) write into the external output file

            #seq returns a value:
        if seq:
            tempSplittedSeq=[] 
            seqLen=len(seq)
            cutoff=120 

            #to split a single line 'seq' into multiple lines and store it in a list
            #set for 120 characters per line
            for i in range(0,seqLen,cutoff):
                tempSplittedSeq.append(seq[i:i+cutoff])

            #to format the header line
            head = '>'+ID.strip()+ '|' +'\t'+org.strip()+ '|'+'\t'+str(seqLen)+'bp'+"<br>"
            print(head) #print'head'on the command prompt

            #sequnce lines in 120 characters per line
            for currentLine in tempSplittedSeq:
                print(currentLine)

    print("</fieldset><br>");
    
#If the user input file is in GCG format, print the following command and open the file
if stype == "gcg":
    print("<h3><b>Sequence in <u>GCG</u> format</b></h3>")

    print("<fieldset>");
    
    #If the user input is in GENBANK format, print the following command
    if re.search(r"LOCUS\s+(.+)\s+",Inseq):
        
        #global vars
        singleSeq = ''
        splitSeq = []
        
        x = formatted_Inseq
        #Split a string into a list 
        seqlines = x.splitlines()
        
        for line in seqlines:
            matchID = re.match(r'LOCUS\s+(.+)\s+', line, re.I)
            # If match
            if matchID:
                # extract the value from group(1) and assign it into a variable named acc
                # variable acc has  data type
                ID = matchID.group(1)
                print("ID"+"\t" +ID+"<br>")

            # to extract the value of ORGANISM

            matchAc = re.match(r'Accession\s+(\w+)', line, re.I)

            # IF match
            if matchAc:
                # extract the value and assign it into a variable named org
                AC = matchAc.group(1)
                print("AC"+"\t"+AC+"<br>")

            matchDE = re.match(r'Definition\s+(.+)', line, re.I)

            # IF match
            if matchDE:
                # extract the value and assign it into a variable named org
                DE = matchDE.group(1)
                print("DE"+"\t"+DE+"<br>")
                
            
            # to extract sequence lines
            sequence = re.match(r"\s+\d+\s+(.+)", line, re.I)
        
            # IF match
            if sequence:
                # extract the sequence from group(1) and assign it into a variable named seqLines
                seqLines = sequence.group(1)
                
        
                # to remove " " and replaced with '' using re.sub function
                seqLines = re.sub(" ", "", seqLines)

                # to concatenate all sequence parts into a single sequence line
                singleSeq += seqLines

                # Each line of the sequence is in 60 bp
                n = 60

                # to split a single line 'singleSeq' into multiple lines and append it in a list named 'splitSeq'
                # set for 60 characters per line
                splitSeq = [singleSeq[index: index + n] for index in range(0, len(singleSeq), n)]

        # IF splitSeq returns a value
        if splitSeq:
            # format locus line

            # takes all sequence in splitSeq and joins them into one string
            # assign the string into a variable named seqLine

            seqLine = ''.join(splitSeq)

            # convert letters to uppercase
            seqLine = seqLine.lower()

            # Count the number of bases in the string
            a = seqLine.count('a')
            c = seqLine.count('c')
            g = seqLine.count('g')
            t = seqLine.count('t')

            # print and write the output of base count in external file
            print('SQ'+'\t'+'Sequence '+str(len(seqLine))+'\t'+'BP; ' + str(a) + 'A;\t' + str(c) + 'C;\t' + str(g) + 'G;\t' + str(t) + 'T;<br>')

            # initialise a variable
            cnt = 0

            # for each line of the sequence which is in 60 bp with the cut off of 10 characters and separated by a white space
            for i in splitSeq:
                # create an empty list named tempSplitSeq to store the splitted 'seq'
                tempSubseq = []

                # number of character to cut off is 10
                cutoff = 120

                # to separate the 60bp sequence with cut-off of 10 characters
                for subseq in range(0, len(i), cutoff):
                    tempSubseq.append(i[subseq:subseq + cutoff])

                # join sequence together
                Seqs = ' '.join(tempSubseq)

                # format the numbering of the sequence
                num = "%10d" % (1 + cnt)
                lineSeq = num + ' ' + Seqs.lower()

                #print(lineSeq)
                print ("%s<br>" % (lineSeq));

                # give numbering to the sequence (every 60 bases)
                cnt = cnt + len(i)

            print('//')             
    
    #If the user input is in EMBL format, print the following command
    if re.search(r"ID\s+(.+)",Inseq):
    
        #global vars
        singleSeq = ''
        splitSeq = []
        
        x = formatted_Inseq
        #Split a string into a list 
        seqlines = x.splitlines()
        
        for line in seqlines:
        
            ###to extract value of ID
            matchID = re.match(r'ID\s+(.+)', line, re.I)

            if matchID:
                # extract the value from group(1) and assign it into a variable named acc
                # variable acc has  data type
                ID = matchID.group(1)
                print("ID"+"\t" +ID+"<br>")


            ###to extract value of Accession 
            matchAc = re.match(r'AC\s+(\w+)', line, re.I)

            # IF match
            if matchAc:
                # extract the value and assign it into a variable named org
                AC = matchAc.group(1)
                print("AC"+"\t"+AC+"<br>")

            ###to extract value of definition
            matchDE = re.match(r'DE\s+(.+)', line, re.I)

            # IF match
            if matchDE:
                # extract the value and assign it into a variable named org
                DE = matchDE.group(1)
                print("DE"+"\t"+DE+"<br>")

            # to extract sequence lines
            sequence = re.match(r"(.+)\s+(\d+)$", line, re.I)
        
            # IF match
            if sequence:
                # extract the sequence from group(1) and assign it into a variable named seqLines
                seqLines = sequence.group(1)
        
                # to remove " " and replaced with '' using re.sub function
                seqLines = re.sub(" ", "", seqLines)

                # to concatenate all sequence parts into a single sequence line
                singleSeq += seqLines

                # Each line of the sequence is in 60 bp
                n = 60

                # to split a single line 'singleSeq' into multiple lines and append it in a list named 'splitSeq'
                # set for 60 characters per line
                splitSeq = [singleSeq[index: index + n] for index in range(0, len(singleSeq), n)]

        # IF splitSeq returns a value
        if splitSeq:
            # format locus line

            # takes all sequence in splitSeq and joins them into one string
            # assign the string into a variable named seqLine

            seqLine = ''.join(splitSeq)


            # convert letters to uppercase
            seqLine = seqLine.lower()

            # Count the number of bases in the string
            a = seqLine.count('a')
            c = seqLine.count('c')
            g = seqLine.count('g')
            t = seqLine.count('t')

            # print and write the output of base count in external file
            print('SQ'+'\t'+'Sequence '+str(len(seqLine))+'\t'+'BP; ' + str(a) + 'A;\t' + str(c) + 'C;\t' + str(g) + 'G;\t' + str(t) + 'T;<br>')

            # initialise a variable
            cnt = 0

            # for each line of the sequence which is in 60 bp with the cut off of 10 characters and separated by a white space
            for i in splitSeq:
                # create an empty list named tempSplitSeq to store the splitted 'seq'
                tempSubseq = []

                # number of character to cut off is 10
                cutoff = 120

                # to separate the 60bp sequence with cut-off of 10 characters
                for subseq in range(0, len(i), cutoff):
                    tempSubseq.append(i[subseq:subseq + cutoff])

                # join sequence together
                Seqs = ' '.join(tempSubseq)

                # format the numbering of the sequence
                num = "%10d" % (1 + cnt)
                lineSeq = num + ' ' + Seqs.lower()

                print ("%s<br>" % (lineSeq));
                
                # give numbering to the sequence (every 60 bases)
                cnt = cnt + len(i)

            print('//')
                        
    print("</fieldset><br>");
    
print ("<input type=button value='<<Choose another format' onClick='history.go(-1); return true;'>&nbsp;&nbsp;&nbsp;");
print ("<input type=button value=Exit onClick='window.close(); return true;'>");
print ("</body>");
print ("</html>");