// http://www.codewars.com/kata/training-js-number-14-methods-of-number-object-tostring-and-tolocalestring/

function pad(value, length) {
  return (value.toString().length < length) ? pad("0" + value, length) : value;
}

function colorOf(r, g, b) {
  return "#" + pad(r.toString(16), 2) + pad(g.toString(16), 2) + pad(b.toString(16), 2);  
}
