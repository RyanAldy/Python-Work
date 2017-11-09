# Number to words

def convert_up_to_twenty(input_num):
    number_dict = {0 : '', 1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four',
                  5 : 'Five', 6 : ' Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine',
                  10 : 'Ten', 11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen',
                  14 : 'Fourteen', 15 : 'Fifteen', 16 : 'Sixteen', 17: 'Seventeen',
                  18 : 'Eighteen', 19 : 'Nineteen'}

    return number_dict.get(input_num)



def convert_tens(input_num):
    tens_dict = {2 : 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6:'Sixty',
                7: 'Seventy', 8 : 'Eighty', 9: 'Ninety'}

    return tens_dict.get(input_num)


def convert_num(input_num):

    output_string = ''

    if input_num >= 1000 and input_num <= 9999:
        output_string += str(convert_up_to_twenty(input_num//1000)) + ' Thousand '
        input_num = input_num - (input_num//1000*1000)
        if input_num < 100 and input_num > 0:
            output_string += 'and '
    if input_num >= 100 and input_num <= 1000:
        output_string += str(convert_up_to_twenty(input_num//100)) + ' Hundred '
        input_num = input_num - (input_num//100*100)
        if input_num < 100 and input_num > 0:
            output_string += 'and '
    if input_num >= 20 and input_num < 100:
        output_string += str(convert_tens(input_num//10)) + ' '
        input_num = input_num - (input_num//10*10)
    if input_num < 20:
        output_string += convert_up_to_twenty(input_num)

    print(output_string)

convert_num(20)
