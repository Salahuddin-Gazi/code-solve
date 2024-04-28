// /**
//  * @param {number} num
//  * @return {string}
//  */
// var intToRoman = function (num) {
//   var roman = "";

//   function integerToRomanConverter(step, str) {
//     roman += str;
//     num -= step;
//     // console.log(`📌 ~ integerToRomanConverter ~ step:`, step, roman);
//   }

//   while (num >= 1) {
//     // console.log(`📌 ~ intToRoman ~ num:`, num);

//     switch (true) {
//       case num >= 1000:
//         integerToRomanConverter(1000, "M");
//         break;

//       case num >= 500:
//         integerToRomanConverter(500, "D");
//         break;

//       case num >= 100:
//         integerToRomanConverter(100, "C");
//         break;

//       case num >= 50:
//         integerToRomanConverter(50, "L");
//         break;

//       case num >= 10:
//         integerToRomanConverter(10, "X");
//         break;

//       case num >= 5:
//         integerToRomanConverter(5, "V");
//         break;

//       case num >= 1:
//         integerToRomanConverter(1, "I");
//         break;
//     }
//   }

//   return roman;
// };

// console.log(intToRoman());

/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
  var roman_str = "";

  var roman_value_hash = [
    { key: "M", value: 1000 },
    { key: "D", value: 500 },
    { key: "C", value: 100 },
    { key: "L", value: 50 },
    { key: "X", value: 10 },
    { key: "V", value: 5 },
    { key: "I", value: 1 },
  ];
};

console.log(intToRoman());
