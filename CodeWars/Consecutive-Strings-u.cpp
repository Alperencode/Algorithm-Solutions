// Consecutive strings
// https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/cpp

#include <string>
#include <vector>
#include <iostream>

class LongestConsec{
public:
    static std::string longestConsec(const std::vector<std::string> &strarr, int k){
        unsigned long longest = 0;
        std::string answer;
        for(unsigned long i=0; i<strarr.size()-k; i++){
            std::string new_str = strarr[i];

            for(int j=0; j<k-1; j++){
                new_str += strarr[i+j+1];
            }

            if(new_str.length() >= longest){
                longest = new_str.length();
                answer = new_str;
            }
        }
        return answer;
    }
};

int main(){

    std::cout << LongestConsec::longestConsec({"zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"}, 2);
    
}

// Status - Failed

// Testcase
// arr = {"ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"}, k = 1
// Expected: "oocccffuucccjjjkkkjyyyeehh"
// Actual: "aanlljrrrxx"