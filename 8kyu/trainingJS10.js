// http://www.codewars.com/kata/training-js-number-10-loop-statement-for/

function pickIt(arr) {
  var odd = [];
  var even = [];
  var n = arr.length;
  
  for (var i = 0; i < n; ++i) {
    if (arr[i] % 2 === 0) {
      even.push(arr[i]);
    } else {
      odd.push(arr[i]);
    }
  }
  
  return [odd, even];
}
