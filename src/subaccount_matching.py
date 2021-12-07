import re

RED = ("RED", 588) #changed from 369 2020-05-20
BCC = ("BCC", 721) #added 2020-12-14
LS = ("Learning Services", 456)
BMM = ("B+MM", 466)
BCOM = ("BCOM", 489)
DAP = ("DAP", 455)
PHD = ("PHD", 457)
COEC = ("COEC", 491)
COMR = ("COMR", 490)
MEL = ("MEL", 463)
MMOR = ("MMOR", 454)
MBAN = ("MBAN", 475) 
FTMBA = ("FTMBA", 486)
PMBA = ("PMBA", 478)
IMBA = ("IMBA", 482)
MMDD = ("MM DD", 469)
MM = ("MM", 472)
PARENT = ("Parent", 454)

#custom list of DAP BUSI courses, all else go to RED 
#last update 2020-05-24
# added BCC 2020-12-14
DAP_COURSE_LIST = ["291", "293", "294", "295", "329", "335", "353", "354", "355", "370", "393", "450", "453", "455", "465", "493"]


def match_course(x):
    """Matches courses to their corresponding sub-accounts when the arguments match a known syntax pattern.
    """
    
    def regex_compare(regex_str, match_str, match=True):
        """Searches for a match between regex_string and match_string 
        
           Args:
                regex_str (string): the string to search for 
                match_str (string): the string to be searched 
                match (boolean): True if regex_str and match_str are known to match
           
           Returns:
                  A match object if a match is found, None otherwise.
        """
        if match == True:
            #compile --> creates a regular expression object which can e used for matching 
            #re.IGNORECASE --> perform a case-insensitive matching

            #match --> If zero or more characters at the beginning of string match regex_str 
            #search --> Scan through string looking for the first location where the regex_str produces a match.
            
            # CHANGE: in return statements, changed re.IGNORECASE to re.I
            return(re.compile(regex_str, re.I).match(match_str))
        else:
            return(re.compile(regex_str, re.I).search(match_str))

    def course_match_account(sub, course, sec):
        """Matches courses to their corresponding sub-accounts using regex pattern comparison
        
           Args (verify):
               sub (string): subject code
               course (string): course number
               sec (string): course section
           
           Returns: 
                a tuple containing the subaccount name and ID that the course is sorted into
        """
        
        if (sub=="COEC" or sub=="COMM"):
            if regex_compare("[5|6][0-9][0-9][a-zA-Z]*", course):
                return(PHD)
            elif sub=="COEC":
                return(COEC)
            elif sub=="COMM":
                if regex_compare("(3|4)8(0|1)", course):
                    return(BCC)
                if regex_compare("MM[0-9]", sec):
                    return(MM)
                elif regex_compare("DD[0-9]", sec):
                    return(BMM)
                else:
                    return(BCOM)
        
        # Addition June 9, 2021            
        if sub=="COMR":
            return(COMR)

        elif sub=="APPP":
            return(MEL)
                
        # if subject is BUSI, and section in DAP_COURSE_LIST, then DAP else RED
        elif sub=="BUSI":
            if course in DAP_COURSE_LIST:
                return(DAP)
            else:
                return(RED)
            
        elif regex_compare("BA[a-zA-Z]{0,2}", sub):
            # APSC courses seem to be very specific... 
            if ((regex_compare("BASC", sub) \
                 and regex_compare("550", course) \
                 and regex_compare("201", sec)) \
               or (regex_compare("580B", sec))):
                return(MEL)
        
            elif regex_compare("DD[0-9]", sec):
                return(MMDD)
            elif regex_compare("BA[0-9]", sec):
                return(MBAN)
            elif regex_compare("00[0-9]", sec):
                return(FTMBA)
            elif regex_compare("3[0-9]{2}", sec):
                return(PMBA)
            elif regex_compare("8[0-9]{2}", sec):
                return(IMBA)
            elif regex_compare("MM[0-9]", sec):
                return(MM)
        
        else:
            return(PARENT)
        
    def course_nomatch_account(x):
        """Sorts courses whose names do not match a known syntax pattern 
        (i.e. course_match == None) into proper subaccounts by using other identifiers
        
        Args: 
            x (string): course code (??)
        """
        if regex_compare(r"\b(learning( *)services|ls|sand( *)box|test)\b", x, False):
            return(LS)
        elif regex_compare(r"\bDAP\b", x, False):
            return(DAP)
        elif regex_compare(r"\b(B\+MM|BMM)\b", x, False):
            return(BMM)
        elif regex_compare(r"\bIMBA\b", x, False):
            return(IMBA)
        elif regex_compare(r"\bPMBA\b", x, False):
            return(PMBA)
        elif regex_compare(r"\bFTMBA\b", x, False):
            return(FTMBA)
        elif regex_compare(r"^MM\b", x, False):
            return(MM)
        elif regex_compare(r"\bMBAN\b", x, False):
            return(MBAN)
        elif regex_compare(r"\bCo-op|Co-operative", x, False):
            return(BCC)
        else:
            return(PARENT)
        
    course_pattern = re.compile(r"((BA[a-zA-Z]{0,2})|COMM|COEC|COMR|BUSI|APPP)( *)([0-9]{3}[a-zA-Z]{0,1})( *)([0-9]{3}|(BA|MM|DD)[0-9]|T[0-9]{2})", flags=re.IGNORECASE)
    course_match = course_pattern.search(str(x))

    if course_match:
        course_str = course_match.group().split(" ", 3)
        out = course_match_account(*course_str)
        return(out)
        print("{}: {}".format(course_str, out))
    else:
        out = course_nomatch_account(x)
        return(out)
        print("{}: {}".format(x, out))