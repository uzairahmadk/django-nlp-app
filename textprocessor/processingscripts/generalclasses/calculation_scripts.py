
class MathemeticsCalculation:

    def percentage_calculator(self, score):

        return_result = []

        #check if the number is negative or positive
        if score < 0:
            #convert the number to positive
            score = -(score)

        #zero value polarity returns negative result so if zero then no percentage calculation
        if score != 0:
            score_percentage = (score * 100)
        else:
            score_percentage = 50

        #converting to integer
        score_percentage = int(score_percentage)

        #check if negative or positive
        #range 45 to 55 is calculated a neutral point here
        if score_percentage > 0 and score_percentage < 45:
            negative_percentage = 100 - score_percentage
            neutral_percentage = 55 - score_percentage
            positive_percentage = 100 - negative_percentage

            return_result.append(negative_percentage)
            return_result.append(positive_percentage)
            return_result.append(neutral_percentage)

        elif score_percentage >= 45 and score_percentage <= 55:

            #if maximun negative density
            if score_percentage < 49:
                negative_percentage = 50 - score_percentage
                neutral_percentage = score_percentage
                positive_percentage = 0
            else:
                negative_percentage = 0
                neutral_percentage = score_percentage
                positive_percentage = 56 - score_percentage

            return_result.append(negative_percentage)
            return_result.append(positive_percentage)
            return_result.append(neutral_percentage)

        else:
            negative_percentage = score_percentage - 45
            positive_percentage = 100 - negative_percentage
            neutral_percentage = 100 - score_percentage

            return_result.append(negative_percentage)
            return_result.append(positive_percentage)
            return_result.append(neutral_percentage)

        return return_result

    def dict_items_summation(self, dict):
        total = 0

        for key, value in dict.items():
            total = total + value

        return total
