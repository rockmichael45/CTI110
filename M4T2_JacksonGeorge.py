#CTI 110
#M4T2 - Python Exercise
#George Jackson
#10/2/17



#Ask the user for a string
userTag = input('Enter tag ')

# P = Indicates a Paragraph
# H = Header Tag
# B = Bold
# DIV = Division

#If one of the two tags, print what tag is + give example of use

if userTag == 'p':
    print ("Indicates a Paragraph <p>text</p>")
    print ("test")
elif userTag == 'h':
    print ("Header Tag <h>text</h>")
    print ("exam")
elif userTag == 'b':
    print ("Bold <b>/text</h>")
    print ("letters") 
elif userTag == 'div':
    print ("Division <div>text</div>")
    print ("multiply")
else:
    print ("Tag not found") 
    
    
