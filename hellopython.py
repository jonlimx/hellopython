__author__ = 'Jonathan Lim'

"""Return the sum result of the number array"""
def sumArray(nums):
    index = 0
    result = 0
    while index < len(nums):
        result += nums[index]
        index += 1

    return result


def avgArray(nums):
    sum = sumArray(nums)

    return float(sum) / len(nums)



astr = ''

nums = [1, 2.4, 5, 7, 6.5]

while astr != 'X':
    astr = input('Please choose:')
    if astr == '1':
        print('Sum of array: %f' % sumArray(nums))
    elif astr == '2':
        print('Average of array: %f' % avgArray(nums))
    elif astr == 'X':
        print('Calculation finished!')
    else:
        print('Invalid input, please try again!')
