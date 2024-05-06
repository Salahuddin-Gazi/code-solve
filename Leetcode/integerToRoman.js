/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
  var roman_str = "";

  var roman_value_hash = {
    M: 1000,
    D: 500,
    C: 100,
    L: 50,
    X: 10,
    V: 5,
    I: 1,
  };

  var negate_romans = ["C", "X", "I"];

  function divide_result_finder(divisibleBy) {
    return Math.floor(num / divisibleBy);
  }

  function closest_negate_finder(key) {
    var keys = Object.keys(roman_value_hash);
    var currIndex = keys.indexOf(key);

    if (currIndex < 0) return "";
    var closest_negate = keys.filter(
      (key, index) => index > currIndex && negate_romans.indexOf(key) >= 0
    )?.[0];

    if (!closest_negate) return "";
    return closest_negate;
  }

  function integerToRomanConvert(key) {
    var val = roman_value_hash[key];
    if (num == val) {
      roman_str += key;
      num -= val;
    } else if (num > val) {
      var division_result = divide_result_finder(val);
      roman_str += key.repeat(division_result);
      num -= division_result * val;
    } else {
      var closest_negate = closest_negate_finder(key);

      roman_str += closest_negate + key;
      num -= roman_value_hash[key] - roman_value_hash[closest_negate];
    }
  }

  while (num >= 1) {
    switch (true) {
      case num >= 900 || num >= 1000:
        integerToRomanConvert("M");
        break;
      case num >= 400 || num >= 500:
        integerToRomanConvert("D");
        break;
      case num >= 90 || num >= 100:
        integerToRomanConvert("C");
        break;
      case num >= 40 || num >= 50:
        integerToRomanConvert("L");
        break;
      case num >= 9 || num >= 10:
        integerToRomanConvert("X");
        break;
      case num >= 4 || num >= 5:
        integerToRomanConvert("V");
        break;
      case num >= 1:
        integerToRomanConvert("I");
        break;
    }
  }
  return roman_str;
};
console.log("928", intToRoman(928));
