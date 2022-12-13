// Sum of odd numbers
// https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/cpp
#include <iostream>
#include <cmath>

long long rowSumOddNumbers(unsigned n){
    long long sum = 0;

    // exponent = n^2
    long long exponent = std::pow(n-1,2);

    for(long long i=0; i<n; i++){
        // n + [(n^2)+i*2)]
        sum += n + (exponent + i*2);
    }
    return sum;

    // Easy way
    return (long long )n*n*n;
}

int main(){
    std::cout << rowSumOddNumbers(5) << std::endl;
}

// Testcases
// 1 - 1
// 5 - 125
// 42 - 74088

// Status - Passed