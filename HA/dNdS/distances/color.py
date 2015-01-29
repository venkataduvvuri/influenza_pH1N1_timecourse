for i in range(10, 26):
    # open the file of new values (just 1 column of numbers, one for each alpha carbon)
    inFile = open("correlations/h1_%s.correlations"%i, 'r')
 
    # create the global, stored array
    stored = []
 
    # read the new B factors from file
    for line in inFile.readlines(): stored.append( float(line) )
 
    # close the input file
    inFile.close()

    max_b = max(stored)
    min_b = min(stored)
 
    # clear out the old B Factors
    cmd.alter("4fnk_SA_bound and n. CA", "b=0.0")
    
    # update the B Factors with new properties
    cmd.alter("4fnk_SA_bound and n. CA", "b=stored.pop(0)")
 
    # color the protein based on the new B Factors of the alpha carbons
    cmd.spectrum("b", "rainbow", "4fnk_SA_bound and n. CA", minimum=-0.21, maximum=0.23)

    cmd.ray("650", "1200")
    cmd.png("images/trimer_0%s.png"%i)