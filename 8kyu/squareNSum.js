// https://www.codewars.com/kata/square-n-sum/

function listSum(total, number) {
    return total + Math.pow(number, 2);
}

function squareSum(numbers) {  
  return numbers.reduce(listSum, 0);
}
