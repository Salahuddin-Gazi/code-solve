/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  var roman_hash = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  var value = 0;

  [...s].forEach((str, idx) => {
    var next = s[idx + 1];
    var next_value = roman_hash[next] || 0;
    var curr_value = roman_hash[str];
    console.log(str, curr_value, next_value);
    if (curr_value >= next_value) {
      value += curr_value;
    } else {
      value -= curr_value;
    }
  });

  return value;
};
