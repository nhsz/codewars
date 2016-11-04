// https://www.codewars.com/kata/training-js-number-13-number-object-and-its-properties/

function whatNumberIsIt(n) {
  var answer = "";
  
  if (Number.isNaN(n)) {
    answer = "Input number is Number.NaN";
  } else if (n === Number.MAX_VALUE){
    answer = "Input number is Number.MAX_VALUE";
  } else if (n === Number.MIN_VALUE) {
    answer = "Input number is Number.MIN_VALUE";
  } else if (n === Number.NEGATIVE_INFINITY) {
    answer = "Input number is Number.NEGATIVE_INFINITY";
  } else if (n === Number.POSITIVE_INFINITY) {
    answer = "Input number is Number.POSITIVE_INFINITY";
  } else {
    answer = "Input number is " + n;
  }
  
  return answer;
}
