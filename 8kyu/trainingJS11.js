// http://www.codewars.com/kata/training-js-number-11-loop-statement-break-continue/

function grabDoll(dolls) {
  var bag = [];
  var n = dolls.length;
  
  for (var i = 0; i < n; ++i) {
    if (bag.length === 3) {
      break;
    }
    
    if (dolls[i] === "Hello Kitty" || dolls[i] === "Barbie doll") {
      bag.push(dolls[i]);
    } else {
      continue;
    }
  }
  
  return bag;
}
