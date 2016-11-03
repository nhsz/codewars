// http://www.codewars.com/kata/training-js-number-9-loop-statement-while-and-do-dot-while/

function padIt(str, n) {
  var i = 0;
  while (i < n) {
    if (i % 2 === 0) {
      str = "*" + str;
    } else {
      str += "*";
    }
    ++i;
  }
  
  return str;
}
