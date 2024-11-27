/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  var i = 0;
  var word_hash_s = {};
  var word_hash_t = {};
  function insertIntoWordHash(str, type) {
    if (type == "s") {
      if (!!word_hash_s[str]) {
        word_hash_s[str] += 1;
      } else {
        word_hash_s[str] = 1;
      }
    } else {
      if (!!word_hash_t[str]) {
        word_hash_t[str] += 1;
      } else {
        word_hash_t[str] = 1;
      }
    }
  }
  while (s.length > i || t.length > i) {
    if (s.length > i) {
      insertIntoWordHash(s[i], "s");
    }
    if (t.length > i) {
      insertIntoWordHash(t[i], "t");
    }

    i++;
  }

  var isEqual = true;
  var keys_s = Object.keys(word_hash_s);
  var keys_t = Object.keys(word_hash_t);

  if (keys_s.length !== keys_t.length) return (isEqual = false);

  for (var key of keys_s) {
    if (!word_hash_t[key]) return (isEqual = false);
    else if (word_hash_s[key] != word_hash_t[key]) return (isEqual = false);
  }

  return isEqual;
};

console.log(isAnagram("anagram", "nagaram"));
console.log(isAnagram("rat", "car"));
console.log(isAnagram("aa", "a"));
