class MonsterDiagnosisAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    # The first parameter to this method is a list of diseases, represented as a
    # list of 2-tuples. The first item in each 2-tuple is the name of a disease. The
    # second item in each 2-tuple is a dictionary of symptoms of that disease, where
    # the keys are letters representing vitamin names ("A" through "Z") and the values
    # are "+" (for elevated), "-" (for reduced), or "0" (for normal).
    #
    # The second parameter to this method is a particular patient's symptoms, again
    # represented as a dictionary where the keys are letters and the values are
    # "+", "-", or "0".
    #
    # This method should return a list of names of diseases that together explain the
    # observed symptoms. If multiple lists of diseases can explain the symptoms, you
    # should return the smallest list. If multiple smallest lists are possible, you
    # may return any sufficiently explanatory list.
    def solve(self, diseases, patient): 
        possible_diseases = []
        vitamin_count = {}
        for diseas in diseases:
            vitamin_difference = 0
            for vitamin in diseases[diseas]:
                if patient[vitamin] != diseases[diseas][vitamin]:
                    vitamin_difference += 1
            
            if vitamin_difference >= 3 and vitamin_difference <= 7:
                possible_diseases.append(diseas)
        print("possible diseases are ", possible_diseases)
        
        patient_data = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, 
                 "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, 
                 "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
        for vitamin in patient:
            if patient[vitamin] == "+":
                patient_data[vitamin] += 1
            elif patient[vitamin] == "-":
                patient_data[vitamin] -= 1
            elif patient[vitamin] == "0":
                patient_data[vitamin] += 0
        print("Patient data is ", patient_data)
        
        disease_data = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, 
            "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, 
            "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
        for disease in possible_diseases:
            for vitamin in diseases[disease]:
                if diseases[disease][vitamin] == "+":
                    disease_data[vitamin] += 1
                elif diseases[disease][vitamin] == "-":
                    disease_data[vitamin] -= 1
                elif diseases[disease][vitamin] == "0":
                    disease_data[vitamin] += 0
        
        print("Disease data is ", disease_data)
                    
        # if the vitamins of patient and diseases difference is betwee between 3 to 6, 
        # that deases is a possible diseaes. 
        pass

