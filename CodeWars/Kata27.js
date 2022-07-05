// Name Shuffler
// https://www.codewars.com/kata/559ac78160f0be07c200005a
function nameShuffler(str){
    return str.split(" ")[1]+ " " + str.split(" ")[0];
}

// Testcases
// name_shuffler('john McClane') - 'McClane john'
// name_shuffler('Mary jeggins') - 'jeggins Mary'
// name_shuffler('tom jerry') - 'jerry tom'

// Status - Passed