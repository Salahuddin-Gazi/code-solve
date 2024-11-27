/**
 * @param {number[]} arr
 * @param {number} target_number
 * @return {number[]}
 */
var twoSum = function (arr, target_number) {
    var num_lists = [...arr].sort((a, b) => a - b);
    console.log("num_lists", num_lists);
    var start_index = 0;
    var last_index = num_lists.length - 1;

    while (start_index < last_index) {
        const temp_sum = num_lists[start_index] + num_lists[last_index];

        if (temp_sum === target_number) {
            var original_start_index = arr.findIndex(
                (num) => num == num_lists[start_index]
            );
            var original_last_index = arr.findIndex((num, idx) => {
                if (idx != original_start_index && num == num_lists[last_index]) {
                    return true;
                }
            });

            //   return `Number indices for the number ${target_number} is [${original_start_index}, ${original_last_index}]`;
            return [original_start_index, original_last_index];
        } else if (temp_sum < target_number) {
            start_index++;
        } else {
            last_index--;
        }
    }

    //   return `No such indices found for the number ${target_number}`;
    return [];
};