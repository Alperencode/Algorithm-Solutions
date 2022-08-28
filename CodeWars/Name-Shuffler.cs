// Name Shuffler
// https://www.codewars.com/kata/559ac78160f0be07c200005a
public class Kata
{   
  public static string NameShuffler(string str)
  {
    return str.Split(" ")[1]+ " " + str.Split(" ")[0];
  }
}

// Testcases
// name_shuffler('john McClane') - 'McClane john'
// name_shuffler('Mary jeggins') - 'jeggins Mary'
// name_shuffler('tom jerry') - 'jerry tom'

// Status - Passed