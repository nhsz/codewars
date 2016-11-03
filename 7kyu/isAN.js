// http://www.codewars.com/kata/isan-value/

function isAN(value) {
  return (typeof value === "number" || value instanceof Number) && !isNaN(value);
}
