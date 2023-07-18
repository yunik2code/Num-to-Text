ones = ['Zero','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
one_tens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen','Twenty']
tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
number=int(input('Enter a number'))
if number<=9:
  print(ones[number])
  
  
elif number<=20:
  print(one_tens[(number-10)])
  
  
elif number<=99:
  number=list(str(number))
  
  print( tens[int(number[0])-2] +' '+ (ones[int(number[1])], ' ') [int(number[1])==0])


elif number<=999:
  number=list(str(number))
  alphabet=ones[int(number[0])] + ' hundred ' +(tens[int(number[1])-2] + ' ', ' ') 
  [int(number[1])==0] + (ones[int(number[2])] + ' ', ' ') [int(number[2])==0]
  print(alphabet)


elif number<=9999:
    number=list(str(number))
    alphabet=ones[int(number[0])] + ' thousand '+ (ones[int(number[1])]+ ' hundred ' ,' ') [int(number[1])==0] +(tens[int(number[2])-2] + ' ', ' ') [int(number[2])==0] + (ones[int(number[3])]+' ', ' ') [int(number[3])==0]
    print(alphabet)
  
else:
  print('sorry number mustn`t exceed 9999')
  
