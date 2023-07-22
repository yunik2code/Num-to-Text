def string(number):

  def convert(number):

    ones = ['Zero','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    one_tens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen','Twenty']
    tens = [' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']

    if number<=9:
      return(ones[number])
      
      
    elif number<=20:
      return one_tens[(number-10)]
      
      
    elif number<=99:
      number=list(str(number))
      
      return tens[int(number[0])-2] +' '+ (ones[int(number[1])], '') [int(number[1])==0]


    elif number<=999:
      number=list(str(number))
      alphabet=ones[int(number[0])] + ' hundred ' +(tens[(int(number[1]))-2] + ' ', '') [int(number[1])==0] + (ones[int(number[2])] + ' ', '') [int(number[2])==0]
      return alphabet


    elif number<=9999:
        number=list(str(number))
        alphabet=ones[int(number[0])] + ' thousand'+ (ones[int(number[1])]+ ' hundred' ,'') [int(number[1])==0] +(tens[int(number[2])-2] + ' ', '') [int(number[2])==0] + (ones[int(number[3])]+' ', '') [int(number[3])==0]
        return alphabet
      
    else:
      return 'sorry number mustn`t exceed 9999'
  
  def float_convert(number):
    ones1 = ['Zero ','One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ']
    number=list(str(number))
    point_index=number.index('.')+1
    numbers_after_point=number[point_index:]
    numbers_before_point=number[:point_index-1]
    integers=''
    for numbers in numbers_before_point:
      integers+=numbers
    integers=int(integers)
    numbers
    output_str=''
    for numbers in numbers_after_point:
      output_str+=ones1[int(numbers)]
    if integers>9999:
      return 'Sorry number must be in range of -9999 to 9999'
    else:
      converted_str=f'{convert(integers)}'
      return converted_str+' point '+output_str
  try:
    float(number)
  except Exception:
    typ=type(number)
    return f'The arguement type of {typ} is not supported'
  else:
    if float(number).is_integer():
      if int(number)<0:
        return 'Negative ' + convert(int(abs(number)))
      else:
        return convert(int(number))
    else:
      if float(number)<0:
        if int(abs(float(number)))>9999:
          return 'Sorry number must be in range of -9999 to 9999'
        else:
          return 'Negative '+ float_convert(abs(float(number)))
      else:

        return float_convert(float(number))
